from django.db import models

# Create your models here.




class Menus(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

class Categories(models.Model):
    name = models.CharField(max_length=60, unique=True)





