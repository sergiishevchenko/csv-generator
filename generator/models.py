from django.db import models
from datetime import datetime


class NewSchema(models.Model):
    schema_name = models.CharField(max_length=30, verbose_name='Schema name', unique=True)
    column_separator = models.CharField(max_length=30, verbose_name='Column separator')
    string_character = models.CharField(max_length=30, verbose_name='String character')

class ColumnNewSchema(models.Model):
    TYPE_LIST = [
        ('FN', 'Full name'),
        ('E', 'Email'),
        ('DN', 'Domain name'),
        ('PN', 'Phone number'),
        ('CN', 'Company name'),
        ('T', 'Text'),
        ('A', 'Address'),
        ('D', 'Date'),
    ]
    schema_id = models.ForeignKey(NewSchema, to_field="id", on_delete=models.CASCADE)
    column_name = models.CharField(max_length=30, verbose_name='Column name')
    type_name = models.CharField(max_length=30, choices=TYPE_LIST, verbose_name='Type name')
    from_field = models.CharField(max_length=10, verbose_name='From')
    to_field = models.CharField(max_length=10, verbose_name='To')
    order = models.CharField(max_length=10, verbose_name='Order')

class DataSchemas(models.Model):
    name = models.ForeignKey(NewSchema, to_field="schema_name", on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
