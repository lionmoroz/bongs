# Generated by Django 2.2 on 2021-01-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Главное фото')),
            ],
        ),
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefits_title', models.CharField(max_length=250, verbose_name='Преимущества-заголовок')),
                ('benefits_description', models.TextField(verbose_name='Преимущества-описание')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_about', models.TextField(blank=True, null=True, verbose_name='Краткое описание')),
                ('adress', models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес')),
                ('phone_one', models.CharField(blank=True, max_length=250, null=True, verbose_name='Телефон 1')),
                ('phone_two', models.CharField(blank=True, max_length=250, null=True, verbose_name='Телефон 2')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('question', models.TextField(verbose_name='Описание вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=200, verbose_name='Акции')),
            ],
        ),
    ]