from django.db import models

# Create your models here.




class Providers(models.Model):

    CHOICES = (
        ('Resposable Inscripto', 'Responsable Inscripto'), 
        ('Monotributista', 'Monotributista'), 
    )


    name = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=20)
    tax_category = models.CharField(max_length=50, choices = CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Provedor'
        verbose_name_plural = 'Provedores'
