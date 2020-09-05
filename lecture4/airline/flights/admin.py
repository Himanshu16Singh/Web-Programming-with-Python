from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
# to modify django admin


class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")


class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)  # be a tuple


# it will tell django that i want to use admin
# app to manipulate Airport and Flight model
admin.site.register(Airport)
# admin.site.register(Flight)
admin.site.register(Flight, FlightAdmin)  # register Flight with FlightAdmin modification
# admin.site.register(Passenger)
admin.site.register(Passenger, PassengerAdmin)
