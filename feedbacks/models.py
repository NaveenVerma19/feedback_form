from django.db import models


# Create your models here.

class TourFeedback(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    tour_start_date = models.DateField(null=True)
    vehicle_condition = models.FloatField()
    driver_support = models.FloatField()
    guide_support = models.FloatField()
    hotels_chosen = models.FloatField()
    ground_support_team = models.FloatField()
    destination_rating = models.FloatField()
    tour_services_rating = models.FloatField()
    improve_services = models.TextField()
    
    def __str__(self):
        return self.first_name
    
