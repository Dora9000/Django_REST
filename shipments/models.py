from django.db import models
from django.utils import timezone

class Country(models.Model):
    """
    id: int not Null - Primary Key
    name: string
    """
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Shipment(models.Model):
    """
    id: int not Null - Primary Key
    to: Country.id
    from: Country.id
    date of departure: date
    date of arrival: date
    """
    country_to = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='country_to')
    country_from = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='country_from')
    date_of_departure = models.DateField(blank=True, null=True)
    date_of_arrival = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Shipment from {self.country_from} to {self.country_to}. Scheduled ' \
               f'to {self.date_of_departure}-{self.date_of_arrival}'
