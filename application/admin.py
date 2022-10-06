from django.contrib import admin
from application.models import IT_Inventory
from application.models import Design_Inventory
# Register your models here.
class ITInventoryAdmin(admin.ModelAdmin):
    list_display = ["item_category", "item_description", "item_model", "p_in", "p_out", "branch", "status", "image", "date"]

class Design_InventoryAdmin(admin.ModelAdmin):
    list_display = ["item_category", "item_description", "item_model", "p_in", "p_out", "branch", "status", "image", "date"]

admin.site.register(IT_Inventory, ITInventoryAdmin)
admin.site.register(Design_Inventory, Design_InventoryAdmin)
