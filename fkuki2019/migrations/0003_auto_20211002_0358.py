# Generated by Django 3.2.7 on 2021-10-01 20:58

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('fkuki2019', '0002_nilai'),
    ]

    operations = [
        migrations.AddField(
            model_name='nilai',
            name='content',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AlterField(
            model_name='nilai',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
