from django.contrib import admin

# Register your models here.
from gestionPedidos.models import Clients, Articles, Orders

class ClientsAdmin(admin.ModelAdmin):
  list_display = ("name","direction", "telephone") # Columns to display
  search_fields = ('name', 'telephone')

class ArticlesAdmin(admin.ModelAdmin):
  list_display = ("name","section", "price") # Columns to display
  list_filter = ("section",)

class OrdersAdmin(admin.ModelAdmin):
  list_display = ("number","date", "delivered") # Columns to display
  list_filter = ("date",)
  date_hierarchy = "date"

admin.site.register(Clients, ClientsAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Orders, OrdersAdmin)