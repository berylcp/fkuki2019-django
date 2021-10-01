from django.db import models
from django.utils.text import slugify
from django.urls import reverse 
from tinymce.models import HTMLField

# Create your models here.

class Materi(models.Model):
    thumbnail = models.ImageField(upload_to='images/', default='images/default.png', null=True)
    judul = models.CharField(max_length=255, default='')
    deskripsi = models.CharField(max_length=255, default='', blank=True)
    kuliahpakar = HTMLField(default='')
    praktikum = HTMLField(default='')
    skillslab = HTMLField(default='')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.judul
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul)
        super(Materi, self).save()

    def get_absolute_url(self):
        return reverse('materi_detail', args=[str(self.slug)])
