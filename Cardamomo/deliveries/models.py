from django.db import models

# Create your models here.




class Deliveries(models.Model):

    CHOICES = {
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Transfer', 'Transfer'),
    }

    client = models.CharField(max_length=100)
    menu = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=CHOICES, max_length=8)