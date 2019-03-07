from django.contrib import admin
from .models import Profile,Event,EventDetails,Organizer,Team,Otpgenerator
admin.site.register(Profile)
admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(EventDetails)
admin.site.register(Otpgenerator)

# Register your models here.
