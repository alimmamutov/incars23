# Generated by Django 4.2.20 on 2025-04-20 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_special_offer',
            field=models.BooleanField(default=False, verbose_name='Спецпредложение'),
        ),
    ]
