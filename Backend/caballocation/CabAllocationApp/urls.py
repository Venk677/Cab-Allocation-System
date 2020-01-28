from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import UserViewSets, DriverViewSets, RideDetailsViewSets

router = DefaultRouter()
router.register(r'users',UserViewSets, basename="users")
router.register(r"drivers", DriverViewSets, basename="drivers")
router.register(r'ridedetails', RideDetailsViewSets, basename="ride-details")
urlpatterns = router.urls