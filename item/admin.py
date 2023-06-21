from django.contrib import admin

from .models import CategoryGroup ,Category, Item, Status

admin.site.register(CategoryGroup)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Status)