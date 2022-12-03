from django.shortcuts import render
from django.db.models.aggregates import Count, Min
from store.models import Product



def say_hello(request):
    result = Product.objects.aggregate(count=Count("id"), min=Min("unit_price"))
    return render(request, "hello.html", {"name": "Ikechukwu Agbarakwe", "result": result})