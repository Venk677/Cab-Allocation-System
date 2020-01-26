from rest_framework import serializers
from .models import UserModel,DriverModel,RideDetailsModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','username',)
    
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverModel
        fields = ('id','drivername',)
        
class RideDetailsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    driver = serializers.ReadOnlyField(source='driver.drivername')
    class Meta:
        model = RideDetailsModel
        fields =('id','user','driver','ride_created','status',)
        
class RideCreateDetailsSerialziers(serializers.ModelSerializer):
    user = UserModel()
    class Meta:
        model = RideDetailsModel
        fields = ('user','status',)

class RideUpdateDetailsSerializers(serializers.ModelSerializer):
    driver = DriverModel()
    class Meta:
        model = RideDetailsModel
        fields = ('driver','status',) 