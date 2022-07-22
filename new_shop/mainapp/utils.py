top_main_menu = [
    {'name': 'Главная', 'href': 'home'},
    {'name': 'Продукты', 'href': 'prod_page'},
    {'name': 'Контакты', 'href': 'contacts'},
]


class DataPageMixin:
    def get_context(self, **kwargs):
        context = kwargs
        # context['top_menu'] = top_main_menu
        return context
