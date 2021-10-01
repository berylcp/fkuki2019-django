from django.contrib import admin

from fkuki2019.models import Materi

# Register your models here.

class MateriAdmin(admin.ModelAdmin):
    list_display = ('judul',)
    prepopulated_fields = {'slug': ('judul',)}

admin.site.register(Materi, MateriAdmin)