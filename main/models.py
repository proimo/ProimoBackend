from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    name = models.CharField('Nume', max_length=500, default=None)
    created = models.DateTimeField('Creat', default=timezone.now)
    updated = models.DateTimeField('Ultima modificare', default=timezone.now)

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
