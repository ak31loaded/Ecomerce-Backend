# Generated by Django 5.0.6 on 2024-07-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_remove_product_image_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
