# Generated by Django 4.2.20 on 2025-04-20 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_leads'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('image', models.ImageField(upload_to='employees/', verbose_name='Фото')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['order'],
            },
        ),
    ]
