from django.db import models


# Create your models here.

class TourFeedback(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    tour_start_date = models.DateField(null=True)
    vehicle_condition = models.FloatField()
    # driver_support = models.IntegerField()
    # guide_support = models.IntegerField()
    # hotels_chosen = models.IntegerField()
    # ground_support_team = models.IntegerField()
    # destination_rating = models.IntegerField()
    # tour_services_rating = models.IntegerField()
    # improve_services = models.TextField()
    
    def __str__(self):
        return self.first_name
    
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name
    
class Account(models.Model):
    customer_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.customer_name        
 
    
class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  #in this Product Modele is not define
    user = models.ForeignKey(Account, on_delete=models.CASCADE) #in this Account Modele is not define
    subject =  models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject