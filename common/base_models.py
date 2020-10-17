from os import listdir
from os.path import join, isfile, exists
from typing import Dict

from django.conf import settings
from django.db import models
from django.db.models import Model, PositiveIntegerField, SlugField, AutoField, DateTimeField
from django.forms import MultiValueField, FileField, MultiWidget, Select, ClearableFileInput, CharField
from django.utils import timezone

from common.utils import get_upload_path


class SelectUploadImageWidget(MultiWidget):
    template_name = 'common/widgets/multiwidget.html'
    media_root = settings.MEDIA_ROOT
    files_dir = ''

    def __init__(self, attrs: Dict = None):
        path = join(self.media_root, self.files_dir)
        files = [(None, '------------')]
        if exists(path):
            files_list = [(f, f) for f in listdir(path) if isfile(join(path, f))]
            files_list.sort()
            files += files_list
        widgets = [
            Select(attrs=attrs, choices=files),
            ClearableFileInput(attrs=attrs),
        ]
        super().__init__(widgets, attrs)

    def get_context(self, name, value, attrs: Dict):
        ClearableFileInput.template_name = 'common/widgets/clearable_file_input.html'
        context = super(SelectUploadImageWidget, self).get_context(name, value, attrs)
        return context

    def decompress(self, value):
        return [None, value]


class SelectUploadFileFormField(MultiValueField):
    widget = SelectUploadImageWidget

    def __init__(self, files_dir='', media_root: str = settings.MEDIA_ROOT, **kwargs):
        self.widget.media_root = media_root
        self.widget.files_dir = files_dir

        fields = (CharField(required=False), FileField(**kwargs))
        super().__init__(fields, require_all_fields=False, required=False)

    def compress(self, data_list):
        if not data_list:
            return None
        if not data_list[1]:
            file_path = join(self.widget.files_dir, data_list[0])
            return file_path
        return data_list[1]


class SelectUploadFileModelField(models.ImageField):
    def contribute_to_class(self, cls, name, **kwargs):
        super(SelectUploadFileModelField, self).contribute_to_class(cls, name, **kwargs)
        if cls._meta.abstract:
            return

        self.files_dir = self.files_dir % {
            'class': cls.__name__.lower(),
            'model_name': cls._meta.model_name.lower(),
            'app_label': cls._meta.app_label.lower(),
            'verbose_name': cls._meta.verbose_name.lower().replace(' ', '_'),
            'verbose_name_plural': cls._meta.verbose_name_plural.lower().replace(' ', '_')
        }

    def __init__(self, files_dir='', media_root=settings.MEDIA_ROOT, verbose_name=None, name=None, width_field=None,
                 height_field=None, **kwargs):
        self.media_root, self.files_dir = media_root, files_dir
        self.width_field, self.height_field = width_field, height_field
        super().__init__(verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        return super().formfield(form_class=SelectUploadFileFormField, files_dir=self.files_dir,
                                 media_root=self.media_root, **kwargs)


class IdModel(Model):
    id = AutoField(primary_key=True, editable=False, db_index=True)

    class Meta:
        abstract = True


class CreatedUpdatedModel(IdModel):
    created = DateTimeField('creat', default=timezone.now)
    updated = DateTimeField('ultima modificare', default=timezone.now)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        self.updated = timezone.now()
        return super(CreatedUpdatedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['created']


class BaseModel(CreatedUpdatedModel):
    name = models.CharField('nume', max_length=500, default=None, db_index=True)
    slug = SlugField('alias', max_length=100, null=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class OrderableModel(Model):
    order_index = PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        abstract = True
        ordering = ['order_index']


class WithImageField(Model):
    image = SelectUploadFileModelField(files_dir='%(verbose_name_plural)s', upload_to=get_upload_path, default=None, blank=True)

    class Meta:
        abstract = True
