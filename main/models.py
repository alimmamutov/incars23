from email.mime import image
from hashlib import blake2s
from tokenize import Triple
from django.db import models


# Create your models here.
class Countries(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "country"
        verbose_name = "Страну"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.name  # Отображение имени страны в админке


class Products(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название",
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name="URL",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to="product_images", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.PositiveIntegerField(default=0, verbose_name="Цена")
    country = models.ForeignKey(to=Countries, on_delete=models.PROTECT)

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
