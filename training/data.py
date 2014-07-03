from models import profile, race

john = profile (name = "John", 
                fc_max_run = 190, fc_max_bike = 180,
                fc_rest = 45)

john.save()


prom_classic = race("Prom Classic")
prom_classic.save()

ironman_nice = race("Prom Classic")
ironman_nice.save()

marathon_paris = race("Marathon de Paris")
marathon_paris.save()


