from django.shortcuts import render
from django.db.models import Value, F, Func, Count
from django.db.models.functions import Concat
from store.models import Product, Customer


def say_hello(request):
    # result = Customer.objects.annotate(
    #     full_name = Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )

    result = Customer.objects.annotate(
        full_name=Concat('first_name', Value(
            ' '), 'last_name'), orders_count=Count('order')
    )

    return render(request, "hello.html", {"name": "Ikechukwu Agbarakwe", "result": result})
