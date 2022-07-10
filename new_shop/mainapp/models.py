from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True, verbose_name='Имя категории')
    description = models.TextField(verbose_name='Описание категории')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL', default=None)
    is_active = models.BooleanField(verbose_name='Активна', default=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование товара')
    img = models.ImageField(verbose_name='Изображение', upload_to='prod_photo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_desc = models.CharField(max_length=255, verbose_name='Краткое описание')
    full_desc = models.CharField(max_length=500, verbose_name='Полное описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField(verbose_name='Количество', default=0)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    class Meta:
        verbose_name = 'Список товаров'
        verbose_name_plural = 'Список товаров'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'prod_id': self.pk})

    def get_active(self):
        return Product.objects.filter(is_active=True).order_by('category', 'name')
