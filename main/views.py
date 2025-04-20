from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse

# from main.content import products

from main.models import Countries, Employee, Products, Leads


# products.sort(key=lambda x: x["price"])


# Create your views here.
def index(request):
    countries = Countries.objects.all()
    products = Products.objects.all().order_by("price")
    employees = Employee.objects.filter(is_active=True).order_by("order")
    # Группируем по 3 сотрудника для карусели
    grouped_employees = []
    temp_group = []
    for i, emp in enumerate(employees, 1):
        temp_group.append(emp)
        if i % 3 == 0:
            grouped_employees.append(temp_group)
            temp_group = []
    if temp_group:
        grouped_employees.append(temp_group)
    context = {
        "products": products,
        "countries": countries,
        "employee_groups": grouped_employees,
    }

    return HttpResponse(render(request, "main/index.html", context))


def contact_form(request):
    error_message = None  # Переменная для хранения сообщений об ошибках

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        summ = request.POST.get("summ")
        city = request.POST.get("city")

        # Проверка наличия обязательных полей
        if not all([name, phone, summ, city]):
            error_message = "Заполните все поля формы."
        else:
            try:
                # Преобразуем сумму в число
                summ = int(summ) if summ else None

                # Создаем запись в базе данных
                Leads.objects.create(
                    name=name,
                    phone=phone,
                    price=summ,
                    city=city,
                )
                return redirect("contact_success")  # Редирект на страницу успеха
            except Exception as e:
                error_message = f"Ошибка: {str(e)}"

    # Отображаем страницу с формой и сообщением об ошибке
    return render(request, "main/contact_form.html", {"error_message": error_message})
