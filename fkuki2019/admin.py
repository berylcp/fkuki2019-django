from django.contrib import admin
from fkuki2019.models import Materi, Nilai, Jadwal

# Register your models here.

class MateriAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Materi, MateriAdmin)
admin.site.register(Nilai)
admin.site.register(Jadwal)