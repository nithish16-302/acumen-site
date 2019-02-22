from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#participant-model
class Participant(models.Model):
    #name, college, year, branch, email, contactno
    I = 'I'
    II = 'II'
    III = 'III'
    IV = 'IV'
    
    YEAR_CHOICES=((I,'I'),(II,'II'),(III,'III'),(IV,'IV'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=128)
    year = models.CharField(max_length = 3, choices = YEAR_CHOICES, default = "I")
    branch = models.CharField(max_length=128)
    contact = models.CharField(max_length=15)
    payment_id = models.CharField(max_length=256)
    paid = models.BooleanField(default=False)
    

#team-model
class Team(models.Model):
    NGO_APPLICATIONS = 'NGO APPLICATIONS'
    XR = 'XR - AR/MR/VR'
    SMART_CITY = 'SMART CITY'
    WOMEN_SAFETY = 'WOMEN SAFETY'
    EDUTAINMENT = 'EDUTAINMENT'
    IAPPS = 'INTELLIGENTS APPLICATIONS'

    THEME_CHOICES = (
                        (NGO_APPLICATIONS, 'NGO APPLICATIONS'), 
                        (XR, 'XR - AR/MR/VR'), 
                        (SMART_CITY, 'SMART CITY'), 
                        (WOMEN_SAFETY, 'WOMEN SAFETY'), 
                        (EDUTAINMENT, 'EDUTAINMENT'), 
                        (IAPPS, 'INTELLIGENTS APPLICATIONS')
                    )
    
    participants = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    project_link = models.CharField(max_length=1024)
    theme = models.CharField(max_length=64, choices=THEME_CHOICES)