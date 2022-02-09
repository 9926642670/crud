from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Persondetail)
class Persondetailadmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'mob_no', 'gender', 'images']