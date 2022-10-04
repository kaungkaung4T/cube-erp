from django.db import models

# Create your models here.



class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1050)
    image = models.ImageField(upload_to="inventory_image")
    date = models.DateField(auto_now_add=True)
