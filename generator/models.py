from django.db import models
from datetime import datetime
from model_utils import Choices


Separator = Choices(
    (".", "."), (";", ";"),
    (":", ":"), ("-", "-")
)

StringCharacter = Choices(
    ('"', '"'), ("'", "'")
)

class NewSchema(models.Model):
    schema_name = models.CharField(max_length=30, verbose_name='Schema name', unique=True)
    column_separator = models.CharField(max_length=30, choices=Separator, verbose_name='Column separator')
    string_character = models.CharField(max_length=30, choices=StringCharacter, verbose_name='String character')
    user_id = models.CharField(max_length=30, verbose_name='User id')
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.schema_name

    class Meta:
        db_table = "NewSchema"

class SetSchema(models.Model):
    column_name = models.CharField(max_length=30, verbose_name='Column name', default=True)
    column_type = models.CharField(max_length=30, verbose_name='Column type', default=True)
    column_order = models.CharField(max_length=30, verbose_name='Column order', default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    set_schema = models.CharField(max_length=30, verbose_name='Name of schema', default=True)
    # id_set = 

    def __str__(self):
        return self.column_name

    class Meta:
        db_table = "SetSchema"
