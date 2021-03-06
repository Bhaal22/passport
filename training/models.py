from django.db import models

class RaceType(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name
 
class Race(models.Model):
    name = models.CharField(max_length=128, unique=True)
    type = models.ForeignKey(RaceType)

    def __unicode__(self):
        return "[{0}] {1}".format (self.type, self.name)

class RaceInstance(models.Model):
    race = models.ForeignKey(Race)
    date = models.DateField()
    class Meta:
        unique_together = ("race", "date")
        index_together = [["race", "date"]]

    def __unicode__(self):
        return "{0} on {1}".format(self.race.name, self.date)
    
    
class RunRaceInstance(models.Model):
    raceInstance = models.ForeignKey(RaceInstance)
    time = models.TimeField(auto_now=True)
    
    def __unicode__(self):
        return "{0} in {1}".format(self.raceInstance.race.name, self.time)

class Profile(models.Model):
    name = models.CharField(max_length=64, unique=True)
    fc_max_run = models.IntegerField()
    fc_max_bike = models.IntegerField()
    fc_rest = models.IntegerField()
    races = models.ManyToManyField("RunRaceInstance")

    def __unicode__(self):
        return self.name

    def fc_run(self, percent):
        return (self.fc_max_run - self.fc_rest) * percent + self.fc_rest

    def fc_bike(self, percent):
        return (fc_max_bike - fc_rest) * percent + fc_rest
