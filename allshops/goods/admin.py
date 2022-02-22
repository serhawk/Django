from django.contrib import admin
from goods.models import product
from goods.models import product,category


@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','genre')
    list_filter=('date',)
    search_fields=('name','genre')

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
        list_display = ('productcategory', 'productsubcategory')
        list_filter = ('stockfield','productcategory')
        search_fields = ('stockfield', 'productcategory','productsubcategory')

# Register your models here.
