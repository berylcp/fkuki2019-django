from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nim = models.CharField(max_length=255, default='', null=True, blank=True)
    nomor_hp = models.CharField(max_length=255, default='', null=True, blank=True)
    foto_profil = models.ImageField(upload_to='images/', default='images/user-default.png', null=True)

    def __str__(self):
        return self.nim

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()