# Generated by Django 3.1.7 on 2021-08-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tanggal_lahir',
        ),
        migrations.AddField(
            model_name='profile',
            name='foto_profil',
            field=models.ImageField(default='images/user-default.png', null=True, upload_to='images/'),
        ),
    ]
