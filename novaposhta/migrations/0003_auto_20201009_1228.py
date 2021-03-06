# Generated by Django 2.2 on 2020-10-09 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novaposhta', '0002_model_translation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Area')),
                ('ref', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Ref')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='warehouse',
            options={'ordering': ['id'], 'verbose_name': 'Warehouse', 'verbose_name_plural': 'Warehouses'},
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='address_af',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='title_af',
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(db_index=True, max_length=255, null=True, verbose_name='City')),
                ('area', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Area')),
                ('area_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='city', to='novaposhta.Area', verbose_name='Area')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='warehouse',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='warehouse', to='novaposhta.City', verbose_name='City'),
        ),
    ]
