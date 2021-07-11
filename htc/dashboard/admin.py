from django.contrib import admin
from .models import RideOffer, RideRequest

# Register your models here.

class OfferAdmin(admin.ModelAdmin):
    readonly_fields = ('driver', 'date_created', 'vehicle_type', 'location', 'begin_date', 'end_date', 'pricing_model', 'price', 'max_load', 'size', 'description')

class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ('business', 'date_created', 'vehicle_type', 'location', 'begin_date', 'end_date', 'pricing_model', 'price', 'max_load', 'size', 'description')

admin.site.register(RideOffer, OfferAdmin)
admin.site.register(RideRequest, RequestAdmin)
