from django.db import models


# Create your models here.

class Field(models.Model):
    name = models.CharField(max_length=20, blank=False)


class Type(models.Model):
    t_field = models.ForeignKey('Field', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=False)
    example = models.CharField(max_length=100, blank=True)


class Intent(models.Model):
    i_type = models.ForeignKey('Type', on_delete=models.CASCADE)
    content = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=20, blank=True)
    is_valid = models.BooleanField(default=False)
    create_date = models.DateTimeField()
