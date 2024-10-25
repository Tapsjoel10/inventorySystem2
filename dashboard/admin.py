from django.contrib import admin
from .models import *

admin.site.site_header = 'JoelInventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category')
    list_filter = ('category', 'name')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)