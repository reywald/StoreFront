from urllib.parse import urlencode

from django.contrib import admin, messages
from django.db.models import Count
from django.http import HttpRequest
from django.urls import reverse
from django.utils.html import format_html

from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']
    search_fields = ['title']

    @admin.display(ordering="product_count")
    def product_count(self, collection):
        url = (reverse("admin:store_product_changelist") +
               "?" +
               urlencode({
                   "collection__id": collection.id
               })
               )
        return format_html("<a href='{}'>{}</a>", url, collection.product_count)

    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).annotate(
            product_count=Count("product")
        )


class InventoryFilter(admin.SimpleListFilter):
    title = "inventory"
    parameter_name = "inventory"

    def lookups(self, request, model_admin):
        return [
            ("<10", "Low")
        ]

    def queryset(self, request, queryset):
        if self.value() == "<10":
            return queryset.filter(inventory__lt=10)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    actions = ["clear_inventory"]
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_filter = ["collection", "last_update", InventoryFilter]
    list_per_page = 10

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory_status')
    def inventory_status(self, product):
        return "Low" if product.inventory < 10 else "OK"

    @admin.action(description="Clear inventory")
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request=request,
            message=f"{updated_count} products were successfully updated.",
            level=messages.INFO
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ["first_name__istartswith", "last_name__istartswith"]

    @admin.display(ordering="order")
    def orders_count(self, customer):
        url = (
            reverse("admin:store_order_changelist") +
            "?" +
            urlencode({
                "customer__id": customer.id
            })
        )
        return format_html("<a href='{}'>{}</a>", url, customer.orders_count)

    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).annotate(
            orders_count=Count("order")
        )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ["customer"]
    list_display = ['id', 'placed_at', 'customer']
    list_per_page = 10
    ordering = ['id']
