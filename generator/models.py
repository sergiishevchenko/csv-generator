from django.db import models
from datetime import datetime


class NewSchema(models.Model):

    schema_name = models.CharField(max_length=30, verbose_name='Schema name', unique=True)
    column_separator = models.CharField(max_length=30, verbose_name='Column separator')
    string_character = models.CharField(max_length=30, verbose_name='String character')
    user_id = models.CharField(max_length=30, verbose_name='User id')
    date = models.DateTimeField(default=datetime.now, blank=True)

class SetSchema(models.Model):

    schema_id = models.ForeignKey(NewSchema, to_field="id", on_delete=models.CASCADE, default=True)
    column_name = models.CharField(max_length=30, verbose_name='Column name', default=True)
    column_type = models.CharField(max_length=30, verbose_name='Column type', default=True)
    column_order = models.CharField(max_length=30, verbose_name='Column order', default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
