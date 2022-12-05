from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):

    contenttype = ContentType.objects.get_for_model(Product)

    result = TaggedItem.objects \
            .select_related("tag") \
            .filter(content_type=contenttype, object_id=1)

    return render(request, "hello.html", {"name": "Ikechukwu Agbarakwe", "result": result})
