from django.db.models import CharField, DateTimeField, CASCADE, ForeignKey, Index, SlugField, Model, \
    AutoField
from django.utils import timezone


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
    name = CharField('nume', max_length=500, default=None, db_index=True)
    slug = SlugField('alias', max_length=100, null=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class County(BaseModel):
    class Meta:
        ordering = ['name']
        verbose_name = 'judeţ'
        verbose_name_plural = 'judeţe'


class Locality(BaseModel):
    county = ForeignKey(County, related_name='localities', related_query_name='locality', on_delete=CASCADE, null=True,
                        verbose_name='judeţ', db_index=True)

    class Meta:
        ordering = ['name']
        indexes = [Index(fields=('county', 'id'))]
        verbose_name = 'localitate'
        verbose_name_plural = 'localităţi'
