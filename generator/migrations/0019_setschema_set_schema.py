# Generated by Django 3.1.3 on 2020-11-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0018_remove_setschema_name_schema'),
    ]

    operations = [
        migrations.AddField(
            model_name='setschema',
            name='set_schema',
            field=models.CharField(default=True, max_length=30, verbose_name='Name of schema'),
        ),
    ]