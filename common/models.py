from django.db.models import CASCADE, ForeignKey, Index

from common.base_models import BaseModel


class County(BaseModel):
    class Meta:
        ordering = ['name']
        verbose_name = 'judeţ'
        verbose_name_plural = 'judeţe'


class Locality(BaseModel):
    county = ForeignKey(County, related_name='localities', related_query_name='locality', on_delete=CASCADE, null=True, verbose_name='judeţ',
                        db_index=True)

    class Meta:
        ordering = ['name']
        indexes = [Index(fields=('county', 'id'))]
        verbose_name = 'localitate'
        verbose_name_plural = 'localităţi'
