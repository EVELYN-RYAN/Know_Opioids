# Generated by Django 3.2.8 on 2021-12-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dontoverdose', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescriber',
            old_name='ispioidprescriber',
            new_name='isopioidprescriber',
        ),
        migrations.AlterField(
            model_name='prescriber',
            name='credentials',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterModelTable(
            name='prescriber',
            table='pd_prescriber_info',
        ),
    ]
