from django.db import models

# Create your models here.
# one model for each table


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    # property
    # origin = models.CharField(max_length=64)
    # models.CASCADE means on deleting airport from airport
    # table also delete corresponding flights from the flight table
    # related_name is for making relationship in reverse order
    # , from airport to flight
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.\
        ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        """ string representation of object """
        return f"{self.id}: {self.origin} to {self.destination}"


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # blank , to allow the possiblity to be not on any flight
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
