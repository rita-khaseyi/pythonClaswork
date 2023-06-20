from django.contrib import admin

# Register your models here.
from.models import cart

class add_to_cartAdmin(admin.ModelAdmin):
    list_display=('product','totalprice','totalprice')

admin.site.register(cart,add_to_cartAdmin)    
