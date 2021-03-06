# Generated by Django 3.1.3 on 2020-11-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0004_auto_20201116_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='newschema',
            name='column_name',
            field=models.CharField(default=True, max_length=30, verbose_name='Column name'),
        ),
        migrations.AddField(
            model_name='newschema',
            name='column_order',
            field=models.CharField(default=True, max_length=30, unique=True, verbose_name='Column order'),
        ),
        migrations.AddField(
            model_name='newschema',
            name='column_type',
            field=models.CharField(default=True, max_length=30, verbose_name='Column type'),
        ),
    ]
