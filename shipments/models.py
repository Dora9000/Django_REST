from django.db import models


class Country(models.Model):
    """
    id: int not Null - Primary Key
    name: string
    """
    name = models.CharField(max_length=150)


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
    date_of_departure = models.DateField(blank=True)
    date_of_arrival = models.DateField(blank=True)
