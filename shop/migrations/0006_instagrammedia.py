# Generated by Django 2.2 on 2020-11-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_product_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_url', models.TextField()),
                ('shortcode', models.TextField()),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
