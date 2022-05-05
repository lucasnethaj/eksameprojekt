from django.db import models


class Opskrifter(models.Model):
    Overskrift = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Opskrift(models.Model):
    Titel = models.CharField()
    ingredienser = models.ForeignKeyr(Ingredienser
 

class Koeleskab(models.Model):
    indhold = models.DateField()
    bruger = models.CharField(max_length=200)

    def __str__(self):
        return self.headline
