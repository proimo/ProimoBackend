from django.db import models
from django.db.models import CharField, DateTimeField, CASCADE, ForeignKey
from django.utils import timezone


class BaseModel(models.Model):
    name = CharField('nume', max_length=500, default=None)
    slug = CharField(max_length=500, default=None, null=True, db_index=True)
    created = DateTimeField('creat', default=timezone.now)
    updated = DateTimeField('ultima modificare', default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['created']


class County(BaseModel):
    class Meta:
        verbose_name = 'judeţ'
        verbose_name_plural = 'judeţe'


class Locality(BaseModel):
    county = ForeignKey(County, related_name='localities', related_query_name='locality', on_delete=CASCADE, null=True,
                        verbose_name='judeţ')

    class Meta:
        verbose_name = 'localitate'
        verbose_name_plural = 'localităţi'
