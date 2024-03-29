# Generated by Django 4.1.7 on 2023-06-21 12:26

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='contact_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63),
        ),
    ]
