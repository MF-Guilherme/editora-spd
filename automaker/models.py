from django.db import models


class Assembly(models.Model):
    name = models.CharField(max_length=50)
    parts = models.ManyToManyField('Part', related_name='assemblies')

    def __str__(self):
        return self.name


class Part(models.Model):
    part_number = models.CharField(max_length=50)

    def __str__(self):
        return self.part_number
