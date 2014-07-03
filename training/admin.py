from django.contrib import admin
from training.models import Profile, Race, RaceInstance, RunRaceInstance

# Register your models here.
admin.site.register(Profile)
admin.site.register(Race)
admin.site.register(RaceInstance)
admin.site.register(RunRaceInstance)
