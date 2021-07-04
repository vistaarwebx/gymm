from django.contrib import admin
from .models import *

@admin.register(contactss)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','subject','Email','message']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['heading','category','date']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','discription']

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name','discription']