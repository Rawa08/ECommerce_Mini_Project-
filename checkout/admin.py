from django.contrib import admin
from .models import Order, OrderLineItem  #adding to be able editing thru admin panel
# Register your models here.


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )   

admin.site.register(Order, OrderAdmin)    