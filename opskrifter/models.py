from django.db import models


class Opskrift(models.Model):
    titel = models.CharField(max_length=100)
    instrukser = models.CharField(max_length=1000)
    ingredienser = models.ManyToManyField('Ingrediens',)

    def __str__(self):
        return self.titel


class Ingrediens(models.Model):
    # antal = models.IntegerField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     koeleskab = models.ForeignKey('koeleskab', )


# class Koeleskab(models.Model):
#     ingredienser = models.ManyToManyField('Ingrediens', on_delete=models.CASCADE)
