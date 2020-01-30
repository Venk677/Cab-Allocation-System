from django.db import models


'''An user model for the user login to the application with an unique name.'''
class UserModel(models.Model):
    username = models.CharField(max_length = 50,unique=True,help_text="Please enter your name")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
'''An driver model fro the respective drivers to login in order to accept the rides requested by the users,also with an unique name'''
class DriverModel(models.Model):
    drivername = models.CharField(max_length=50,unique=True,help_text="Please enter your name")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.drivername
    
    
'''Ride details of the ride with user and driver details.'''
class RideDetailsModel(models.Model):
    REQUESTED = "RE"
    ACCEPTED = "AC"
    DONE = "DO"
    RIDE_CHOICES = [
        (REQUESTED, "Requested"),
        (ACCEPTED, "Accepted"),
        (DONE, "Done")
    ]
    user = models.ForeignKey(UserModel ,on_delete=models.CASCADE,help_text="Select the User")
    driver = models.ForeignKey(DriverModel ,on_delete=models.CASCADE,help_text="Select the Driver", blank=True, null=True)
    ride_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=RIDE_CHOICES,default=DONE,max_length=2,help_text="Select your operation to view your user in that status")  
    
    def __str__(self):
        return "Ride of {}  the drivername is {}".format(self.user, self.driver)