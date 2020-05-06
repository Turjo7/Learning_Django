from django.contrib import admin
from .models import Product, Offer

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock','image_url')


# Register your models here.
# Adding the product module to the admin panel provided by Django
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
