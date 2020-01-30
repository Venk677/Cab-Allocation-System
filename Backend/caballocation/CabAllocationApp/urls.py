# <<<<<<< HEAD

# =======
# >>>>>>> c552c98b3cc05cb771a7336b56f2fcfae0f1bbee
from django.urls import path

from rest_framework.routers import DefaultRouter

# <<<<<<< HEAD
from .views import UserViewSets, DriverViewSets, RideDetailsViewSets


# =======

router = DefaultRouter()
router.register(r'users',UserViewSets, basename="users")
router.register(r"drivers", DriverViewSets, basename="drivers")
router.register(r'ridedetails', RideDetailsViewSets, basename="ride-details")
# >>>>>>> c552c98b3cc05cb771a7336b56f2fcfae0f1bbee
urlpatterns = router.urls