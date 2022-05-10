# Generated by Django 4.0.3 on 2022-04-24 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_thumbnail_delete_productimagealbum_product_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='product',
            name='main_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='product/thumbnail'),
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_thumbnail', to='product.product'),
        ),
    ]