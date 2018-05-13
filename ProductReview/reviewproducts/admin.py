from django.contrib import admin

# Register your models here.
from reviewproducts.models import Product
from reviewproducts.models import Review

admin.site.register(Product)
admin.site.register(Review)