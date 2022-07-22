from django.db import models

from mainapp.models import Product


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
    time = models.DateTimeField(verbose_name='Дата и время добавления в корзину', auto_now_add=True)

    def get_total_cost(self):
        items = Cart.objects.filter(user=self.user)
        total_cost = sum(list(map(lambda x: x.item.price, items)))
        return total_cost
