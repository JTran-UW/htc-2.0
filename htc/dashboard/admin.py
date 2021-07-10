from django.contrib import admin
from .models import RideOffer, RideRequest

# Register your models here.

class OfferAdmin(admin.ModelAdmin):
    readonly_fields = ("driver", "date_created", "date_to_end", "description")

class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ("business", "date_created", "date_to_end", "description")

admin.site.register(RideOffer, OfferAdmin)
admin.site.register(RideRequest, RequestAdmin)
