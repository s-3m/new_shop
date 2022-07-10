# Generated by Django 4.0.5 on 2022-07-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории товаров', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Список товаров', 'verbose_name_plural': 'Список товаров'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None, unique=True, verbose_name='URL'),
        ),
    ]
