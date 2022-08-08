from unicodedata import name
from django.contrib import admin

# Register your models here.
from .models import Airport, Flight, Booking


class AirportAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "airport_code")
    search_fields = ("name", "country")
    list_filter = ("airport_code",)


class FlightAdmin(admin.ModelAdmin):
    list_display = ("aeroplane", "departure", "destination", "departure_datetime", "arrival_datetime", "max_passenger", "dollar_amount", "duration")
    search_fields = ("aeroplane",)
    list_filter = ("departure_datetime",)
    readonly_fields = ("duration",)

    def dollar_amount(self, obj):
        return "$ %s" % obj.price if obj.price else ""


class BookingAdmin(admin.ModelAdmin):
    list_display = ("reference_no", "passenger_first_name", "passenger_last_name", "flight", "booking_datetime")
    search_fields = ("passenger_first_name", "passenger_last_name")


admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Booking, BookingAdmin)