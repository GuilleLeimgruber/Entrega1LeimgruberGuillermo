from django.db import models

# Create your models here.




class Deliveries(models.Model):

    CHOICES = (
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'), 
        ('Transferencia', 'Transferencia'),
    )
        
    
    client = models.CharField(max_length=100)
    menu = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=13, choices=CHOICES)


    def __str__(self):
        return  f'{self.client} - {self.menu}'

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliverys'
