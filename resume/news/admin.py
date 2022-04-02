from django.contrib import admin
from . models import (Resume, Products)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'products')


admin.site.register(Resume)
admin.site.register(Products)