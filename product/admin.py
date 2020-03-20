from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	model = Product
	list_display = ['id', 'name', 'weight', 'price', 'created_at', 'updated_at']
	search_fields = ['name', 'weight', 'price']

admin.site.register(Product, ProductAdmin)
