from django.contrib import admin

from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'created', 'modified']
	search_filds = ['name', 'slug']
	list_filter = ['created', 'modified']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'category', 'created', 'modified']
	search_filds = ['name', 'slug', 'category__name']
	

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
