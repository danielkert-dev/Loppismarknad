from django.contrib.auth.models import User
from django.db import models

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
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=True, null=True,)
    status = models.ForeignKey(Status, related_name='items', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name',]
        verbose_name_plural = 'Items'
    def __str__(self):
        return self.name