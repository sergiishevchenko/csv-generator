# Generated by Django 3.1.3 on 2020-11-16 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0008_auto_20201116_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='newschema',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
