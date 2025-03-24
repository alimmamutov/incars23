# main/management/commands/load_products.py

from django.core.management.base import BaseCommand
from main.models import Countries, Products


class Command(BaseCommand):
    help = "Загружает продукты из content.py в базу данных"

    def handle(self, *args, **kwargs):
        # Словарь соответствия названий стран их pk
        country_mapping = {
            "Georgia": 6,
            "Korea": 2,
            "Japan": 4,
            "China": 3,
            "Europe": 5,
            "USA": 7,
        }

        # Данные продуктов из content.py
        products_data = [
            # Грузия (Georgia)
            {
                "title": "BMW 330I",
                "description": "2021 год, 32 тысяч пробег",
                "price": 3350000,
                "country": "Georgia",
            },
            {
                "title": "BMW 40i",
                "description": "2021 год, 42 тысяч пробег",
                "price": 5450000,
                "country": "Georgia",
            },
            {
                "title": "MB GLE450",
                "description": "2022 год, 38 тысяч пробег",
                "price": 8300000,
                "country": "Georgia",
            },
            {
                "title": "MB GLE 53 COUPE",
                "description": " 2022 год, 42 тысяч пробег",
                "price": 9300000,
                "country": "Georgia",
            },
            # Корея (Korea)
            {
                "title": "BMW 3 серии 320d",
                "description": "2021 год",
                "price": 3800000,
                "country": "Korea",
            },
            {
                "title": "Kia Mohave",
                "description": " 2022 год",
                "price": 4100000,
                "country": "Korea",
            },
            {
                "title": "Mercedes Benz E220d",
                "description": " 2021 год",
                "price": 4100000,
                "country": "Korea",
            },
            {
                "title": "Kia Carnival IV",
                "description": " 2021 год",
                "price": 3200000,
                "country": "Korea",
            },
            # Япония (Japan)
            {
                "title": "Toyota Tank",
                "description": " 2020 год",
                "price": 9900000,
                "country": "Japan",
            },
            {
                "title": "Honda Stepwgn Spada",
                "description": " 2017 год",
                "price": 1880000,
                "country": "Japan",
            },
            {
                "title": "Subaru Levorg",
                "description": " 2021 год, 42 тысяч пробег",
                "price": 1950500,
                "country": "Japan",
            },
            # Китай (China)
            {
                "title": "Changan UNI-V",
                "description": "2022 год, 25 тысяч пробег",
                "price": 1868900,
                "country": "China",
            },
            {
                "title": "Volkswagen Golf R",
                "description": " 2021 год, 32 тысяч пробег",
                "price": 2100000,
                "country": "China",
            },
            {
                "title": "BMW X3",
                "description": "2021 год",
                "price": 4400000,
                "country": "China",
            },
            # Европа (Europe)
            {
                "title": "Mercedes-Benz GLE 300 d AMG-Line",
                "description": " 2022 год",
                "price": 7500000,
                "country": "Europe",
            },
            {
                "title": "BMW X7 xDrive 40 d M Sport",
                "description": "2023 год",
                "price": 7500000,
                "country": "Europe",
            },
            {
                "title": "Porsche Cayenne E-Hybrid Coupe Platinum Edition",
                "description": "2022 год",
                "price": 7500000,
                "country": "Europe",
            },
            # США (USA)
            {
                "title": "Chevrolet Trailblazer",
                "description": "2021 год, 59 тысяч пробег",
                "price": 1750000,
                "country": "USA",
            },
            {
                "title": "Chevrolet Camaro",
                "description": "2020 год, 70 тысяч пробег",
                "price": 2780000,
                "country": "USA",
            },
            {
                "title": "Ford Mustang",
                "description": " 2022 год, 52 тысяч пробег",
                "price": 2930000,
                "country": "USA",
            },
        ]

        # Загрузка данных в базу
        for product_data in products_data:
            country_name = product_data["country"]
            price = product_data["price"]
            title = product_data["title"]
            description = product_data["description"]

            # Находим страну по имени
            try:
                country_id = country_mapping[country_name]
                country = Countries.objects.get(pk=country_id)
            except KeyError:
                self.stdout.write(
                    self.style.ERROR(f'Страна "{country_name}" не найдена')
                )
                continue
            except Countries.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"Страна с ID {country_id} не существует")
                )
                continue

            # Создаем или обновляем продукт
            product, created = Products.objects.update_or_create(
                name=title,
                defaults={
                    "price": price,
                    "country": country,
                    "description": description,
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Продукт "{title}" успешно создан')
                )
            else:
                self.stdout.write(self.style.WARNING(f'Продукт "{title}" обновлен'))

        self.stdout.write(self.style.SUCCESS("Все продукты загружены в базу данных"))
