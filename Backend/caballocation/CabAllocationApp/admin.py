from django.contrib import admin
from .models import UserModel, DriverModel, RideDetailsModel



@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display =('username', 'date_created', 'date_modified')
    
    
@admin.register(DriverModel)
class DriverModel(admin.ModelAdmin):
    list_display =('drivername','date_created', 'date_modified')

@admin.register(RiderDetails)
class RiderDetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'drivername', 'ride_created', 'status')


