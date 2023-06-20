from django.contrib import admin

# Register your models here.
from.models import Trader

class TraderAdmin(admin.ModelAdmin):
    list_display = ('name','phone','adress')


admin.site.register(Trader, TraderAdmin)
