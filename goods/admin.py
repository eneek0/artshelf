from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products, Tags, Favorite

# admin.site.register(Categories)
# admin.site.register(Products)
admin.site.register(Tags)

admin.site.register(Favorite)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}