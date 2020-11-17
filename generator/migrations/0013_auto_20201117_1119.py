# Generated by Django 3.1.3 on 2020-11-17 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0012_auto_20201116_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setschema',
            name='schema_id',
        ),
        migrations.AddField(
            model_name='setschema',
            name='name_schema',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='SetSchema', to='generator.newschema'),
        ),
        migrations.AlterField(
            model_name='newschema',
            name='column_separator',
            field=models.CharField(choices=[('Comma(.)', '.'), ('Semicolon(;)', ';'), ('Colon(:)', ':'), ('Dash(-)', '-')], max_length=30, verbose_name='Column separator'),
        ),
        migrations.AlterField(
            model_name='newschema',
            name='string_character',
            field=models.CharField(choices=[('Double-quote', '"'), ('One-quote', "'")], max_length=30, verbose_name='String character'),
        ),
        migrations.AlterModelTable(
            name='newschema',
            table='NewSchema',
        ),
        migrations.AlterModelTable(
            name='setschema',
            table='SetSchema',
        ),
    ]