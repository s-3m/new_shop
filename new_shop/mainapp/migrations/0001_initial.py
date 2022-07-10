# Generated by Django 4.0.5 on 2022-07-04 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True, verbose_name='Имя категории')),
                ('description', models.TextField(verbose_name='Описание категории')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Наименование товара')),
                ('img', models.ImageField(upload_to='prod_photo', verbose_name='Изображение')),
                ('short_desc', models.CharField(max_length=255, verbose_name='Краткое описание')),
                ('full_desc', models.CharField(max_length=500, verbose_name='Полное описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
        ),
    ]
