from email.mime import image
from hashlib import blake2s
from tokenize import Triple
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html


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
        upload_to="products_images", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.PositiveIntegerField(default=0, verbose_name="Цена")
    country = models.ForeignKey(to=Countries, on_delete=models.PROTECT)

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name}"


class Leads(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    summ = models.PositiveIntegerField(
        verbose_name="Желаемый бюджет", null=True, blank=True
    )
    city = models.CharField(max_length=100, verbose_name="Город")
    is_processed = models.BooleanField(
        default=False, verbose_name="Обработана ли заявка"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = "leads"
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ("-created_at",)  # Сортировка по дате создания (от новых к старым)

    def __str__(self):
        return f"{self.name} - {self.phone}"


class Employee(models.Model):
    name = models.CharField("ФИО", max_length=100)
    position = models.CharField("Должность", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    image = models.ImageField("Фото", upload_to="employees/")
    is_active = models.BooleanField("Активный", default=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["order"]

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return format_html('<img src="{}" width="100" />', self.image.url)
        return "Нет фото"

    image_tag.short_description = "Превью"

    def phone_link(self):
        return format_html('<a href="tel:{0}">{0}</a>', self.phone)

    phone_link.short_description = "Телефон"
