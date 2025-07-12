from django.db import models

class TBCarsWeb(models.Model):
    carname = models.TextField()
    carbrand = models.TextField()
    carmodel = models.TextField()
    carprice = models.TextField()

    def __str__(self):
        return self.carname