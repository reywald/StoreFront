from django.shortcuts import render
from django.db.models import Value, F, ExpressionWrapper, DecimalField
from store.models import Product


def say_hello(request):

    discounted_price = ExpressionWrapper(
        F("unit_price") * 0.8, output_field=DecimalField())

    result = Product.objects.annotate(
        discounted_price=discounted_price
    )

    return render(request, "hello.html", {"name": "Ikechukwu Agbarakwe", "result": result})
