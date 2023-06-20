from django.contrib import admin

# Register your models here.


from.models import Order_request

class Order_requestAdmin(admin.ModelAdmin):
    list_display = ('total_amount', 'order_date','name')


admin.site.register(Order_request, Order_requestAdmin)
