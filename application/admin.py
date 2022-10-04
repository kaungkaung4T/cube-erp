from django.contrib import admin
from application.models import Inventory
# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "image", "date"]


admin.site.register(Inventory, InventoryAdmin)
