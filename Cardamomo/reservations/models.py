from django.db import models

# Create your models here.




class Reservations(models.Model):
    name = models.CharField(max_length=100)
    dinner = models.IntegerField()
    reservation_date = models.DateField()
   
    def __str__(self):
        return self.name