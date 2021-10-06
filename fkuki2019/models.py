from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.

class Materi(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    kuliahpakar = HTMLField(default='')
    praktikum = HTMLField(default='')
    keterampilanmedis = HTMLField(default='')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Materi, self).save()
    
    def get_absolute_url(self):
        return reverse('materi_detail', args=[str(self.slug)])

class Nilai(models.Model):
    title = models.CharField(max_length=255, default='')
    content = HTMLField(default='')
    
    def __str__(self):
        return self.title

class Jadwal(models.Model):
    title = models.CharField(max_length=255, default='')
    content = HTMLField(default='')
    
    def __str__(self):
        return self.title