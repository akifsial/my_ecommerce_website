from django.contrib import admin
from store.models import Product, Category, Order


class AdminProduct(admin.ModelAdmin):
  list_display = ["name", "price", "category"]
  search_fields = ("name",)
  list_per_page = 10


class AdminCategory(admin.ModelAdmin):
  list_display = ["name"]

class AdminOrder(admin.ModelAdmin):
  list_display = ["customer", "product", "quantity", "price", "phone", "address", "date"]
  search_fields = ("customer",)
  list_per_page = 10


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order, AdminOrder)