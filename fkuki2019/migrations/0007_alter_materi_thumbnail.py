# Generated by Django 3.2.6 on 2021-08-04 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fkuki2019', '0006_materi_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materi',
            name='thumbnail',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
    ]
