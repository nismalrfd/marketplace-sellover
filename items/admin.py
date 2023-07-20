from django.contrib import admin

from items.models import Category, Item

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)