# Generated by Django 3.1.3 on 2020-11-18 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0025_auto_20201118_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='setschema',
            name='set_id',
            field=models.CharField(default=True, max_length=30, verbose_name='Set id'),
        ),
    ]
