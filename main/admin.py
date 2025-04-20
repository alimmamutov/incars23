from django.contrib import admin

# Register your models here.

from main.models import Countries, Employee, Leads, Products

# admin.site.register(Countries)
# admin.site.register(Products)


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("pk", "name", "slug")
    ordering = ("pk",)
    search_fields = ("name",)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    list_display = (
        "pk",
        "name",
        "slug",
        "price",
        "country",
    )
    ordering = ("pk",)
    list_filter = ("country",)
    search_fields = ("name",)
    list_per_page = 15

    # Указываем пользовательский шаблон
    change_list_template = "main/admin_product_list.html"


@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "summ", "city", "is_processed", "created_at")
    list_filter = ("is_processed", "created_at")  # Фильтры по статусу и дате
    search_fields = ("name", "phone", "city")  # Поиск по имени, телефону и городу
    list_editable = ("is_processed",)  # Возможность редактировать статус прямо в списке
    date_hierarchy = "created_at"  # Иерархия по дате создания
    ordering = ("-created_at",)  # Сортировка по дате создания


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "phone_link", "image_tag", "is_active", "order")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "position")
    readonly_fields = ("image_tag",)
