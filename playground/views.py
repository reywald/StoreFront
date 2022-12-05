from django.shortcuts import render
from django.db.models import Value, F
from store.models import Product, OrderItem



def say_hello(request):
    result = OrderItem.objects.annotate(sub_total=F("unit_price") * F("quantity"))
    return render(request, "hello.html", {"name": "Ikechukwu Agbarakwe", "result": result})