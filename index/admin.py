from django.contrib import admin

# Register your models here.

from . models import Mensaje, Musico

admin.site.register(Mensaje)
admin.site.register(Musico)
