# Generated by Django 3.2.7 on 2021-10-03 03:06

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('fkuki2019', '0003_auto_20211002_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('content', tinymce.models.HTMLField(default='')),
            ],
        ),
    ]
