from django.contrib import admin
from .models import UserModel, DriverModel, RideDetailsModel



@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display =('username', 'date_created', 'date_modified',)
    
    
@admin.register(DriverModel)
class DriverAdmin(admin.ModelAdmin):
    list_display =('drivername','date_created', 'date_modified',)

@admin.register(RideDetailsModel)
class RiderDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'driver', 'ride_created', 'status',)


