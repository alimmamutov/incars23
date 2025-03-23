from django.contrib import admin

# Register your models here.

from main.models import Countries, Products

# admin.site.register(Countries)
# admin.site.register(Products)


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
