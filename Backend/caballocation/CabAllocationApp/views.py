from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404


class UserViewsets(viewsets.ModelViewSet):

    '''To list all the user.'''

    def list(self, request):
        queryset = UserModel.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    '''To retrieve a particular user.'''

    def retrieve(self, request, pk=None):
        queryset = UserModel.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    '''To create a new user.'''

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DriverViewSets(viewsets.ModelViewSet):

   '''To list all the drivers.'''

    def list(self, request):
        queryset = DriverModel.objects.all()
        serializer = DriverSerializer(queryset, many=True)
        return Response(serializer.data)

    '''To retrieve a specific user.'''

    def retrieve(self, request, pk=None):
        queryset = DriverModel.objects.all()
        driver = get_object_or_404(queryset, pk=pk)
        serializer = DriverSeriazlizer(driver)
        return Response(serializer.data)

    '''To create a new driver'''

    def create(self, request):
        serializer = DriverSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RideDetailsViewSets(viewsets.ModelViewSets):

    '''To list all the ride details and its status'''

    def list(self, request):
        queryset = RideDetailsModel.objects.all()
        user = request.GET.get('user', None)
        driver = request.GET.get('driver', None)
        status = request.GET.get('status', None)
        if user is not None:
            queryset = queryset.filter(user__username=user)
        if driver is not None:
            queryset = queryset.filter(driver__driver=driver)
        if status is not None:
            queryset = queryset.filter(status=status)
        serializer = RideDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print("This is Create start", request.data)
        try:
            user = UserModel.objects.get(id=request.data['user'])
            print("Try block", user)
        except UserModel.DoesNotExist:
            print("Except block")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        requested = RideDetails.objects.filter(user=user).filter(status='RE').count()
        accepted = RideDetails.objects.filter(user=user).filter(status='AC').count()
        if requested > 0:
            return Response("Already Requested", status=status.HTTP_226_IM_USED)
        if accepted > 0:
            return Response("Ride is ongoing", status=status.HTTP_403_FORBIDDEN)
        serializer = RideCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        ride = RideDetails.objects.get(id=pk)
        status = request.data.get('status', None)
        if status == 'AC' or status == 'DO':
            # This ensures only valid states are set, invalid states are ignored
            ride.status = status
        if status == 'AC':
            # Driver is set only while accepting the ride and at no other point
            driver_name = request.data.get('driver', None)
            if driver_name is not None:
                try:
                    driver = DriverModel.objects.get(drivername=driver_name)
                    ride.driver = driver
                except DriverModel.DoesNotExist:
                    return Response("Driver doesnot exist", status=status.HTTP_400_BAD_REQUEST)
        ride.save()
        
        
            
    
