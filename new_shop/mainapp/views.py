from random import choice

from django.shortcuts import render
from django.views.generic import *
from mainapp.models import *
from mainapp.utils import DataPageMixin

top_main_menu = [
    {'name': 'Главная', 'href': 'home'},
    {'name': 'Продукты', 'href': 'prod_page'},
    {'name': 'Контакты', 'href': 'contacts'},
]

category_menu = [
    {'name': 'Диваны', 'href': 'sofas'},
    {'name': 'Кровати', 'href': 'beds'},
    {'name': 'Кресла', 'href': 'armchairs'},
    {'name': 'Стулья', 'href': 'chairs'},
]

class HomePage(DataPageMixin, ListView):
    model = Product
    template_name = 'mainapp/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_context = self.get_context(title='Супер-мебель')  # Передаем доп контекст, используя созданный mixin
        return dict(list(context.items()) + list(mix_context.items()))  # Объединяем два словаря


class MainProduct(DataPageMixin, ListView):
    model = Product
    template_name = 'mainapp/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        hot_prod = self.get_hot_product()
        same_prod = Product.objects.filter(category=hot_prod.category)
        mix_content = self.get_context(title='Товары', category=category, hot_prod=hot_prod, same_prod=same_prod)
        return dict(list(context.items()) + list(mix_content.items()))

    def get_hot_product(self):
        hot_prod = choice(Product.objects.all())
        return hot_prod

# def main_products(request):
#     context = {'top_main_menu': top_main_menu}
#
#     return render(request, 'mainapp/products.html', context=context)


def contacts(request):
    context = {'top_main_menu': top_main_menu}
    return render(request, 'mainapp/contact.html', context=context)
