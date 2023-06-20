from django.contrib import admin

# Register your models here.
from.models import new_user

class UserAdmin(admin.ModelAdmin):
    list_display=('username', 'firstname', 'lastname', 'email', 'phonenumber' )


admin.site.register(new_user, UserAdmin)



