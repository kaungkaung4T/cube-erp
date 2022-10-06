from django.db import models

# Create your models here.





choice = (
    ("Good", "Good"),
    ("Bad", "Bad"),
    ("blank", "blank"),
)

class IT_Inventory(models.Model):
    item_category = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    item_model = models.CharField(max_length=255)

    p_in = models.IntegerField(null=True, blank=True)
    p_out = models.IntegerField(null=True, blank=True)
    branch = models.IntegerField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=choice, default="Good")
    image = models.ImageField(upload_to="inventory_image", null=True, blank=True)
    date = models.DateField(auto_now_add=True)


class Design_Inventory(models.Model):
    item_category = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    item_model = models.CharField(max_length=255)

    p_in = models.IntegerField(null=True, blank=True)
    p_out = models.IntegerField(null=True, blank=True)
    branch = models.IntegerField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=choice, default="Good")
    image = models.ImageField(upload_to="inventory_image", null=True, blank=True)
    date = models.DateField(auto_now_add=True)
