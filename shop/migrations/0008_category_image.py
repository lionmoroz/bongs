# Generated by Django 2.2 on 2021-02-01 10:10

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_delete_instagrammedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.Category.image_directory_path, verbose_name='Главное фото'),
        ),
    ]
