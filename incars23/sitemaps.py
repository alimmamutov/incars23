from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from main.models import Products


class StaticViewSitemap(Sitemap):
    priority = 1.0  # Приоритет в поиске (0.1-1.0)
    changefreq = "daily"  # Как часто обновляется ('always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never')

    def items(self):
        # Возвращает список URL или объектов
        return [
            "index",  # Имя URL из urls.py
        ]

    def location(self, item):
        return reverse(item)  # Генерирует полный URL


# class CarSitemap(Sitemap):
#     changefreq = "daily"
#     priority = 0.7

#     def items(self):
#         return Products.objects.all()  # Только опубликованные авто
