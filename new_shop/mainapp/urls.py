from django.conf import settings
from django.urls import path

from mainapp.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('products', MainProduct.as_view(), name='prod_page'),
    path('contacts', contacts, name='contacts'),
    path('category/<slug:category_slug>/', CategoryProductsList.as_view(), name='category'),
    # path('product/<int:prod_id>/', name='product')
]
