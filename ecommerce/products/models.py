from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    image = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    reviews = models.IntegerField(default=0)
        
    def __str__(self):
        return self.name
