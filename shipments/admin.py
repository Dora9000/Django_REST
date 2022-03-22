from django.contrib import admin
from .models import Country, Shipment


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_editable = ()
    list_filter = ('id', 'name')


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_to', 'country_from', 'date_of_departure', 'date_of_arrival')
    list_display_links = ('id', 'country_to')
    search_fields = ('id', 'country_to', 'country_from', 'date_of_departure', 'date_of_arrival')
    list_editable = ('date_of_departure', 'date_of_arrival')
    list_filter = ('country_to', 'country_from', 'date_of_departure', 'date_of_arrival')


admin.site.register(Country, CountryAdmin)
admin.site.register(Shipment, ShipmentAdmin)
