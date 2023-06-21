from django.contrib.auth.models import User
from django.db import models

from location_field.models.plain import PlainLocationField

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name',]
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
    
    def get_item_count(self):
        return self.items.all().count()
    
class Status(models.Model):
    status = models.CharField(max_length=255)

    class Meta:
        ordering = ['status',]
        verbose_name_plural = 'Status'
    
    def __str__(self):
        return self.status
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    city = models.CharField(max_length=255, blank=True, null=True,)
    location = PlainLocationField(based_fields=['city'])
    status = models.ForeignKey(Status, related_name='items', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name',]
        verbose_name_plural = 'Items'
    def __str__(self):
        return self.name