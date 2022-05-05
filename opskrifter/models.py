from django.db import models

# Hver class svarer til en tabel i vores sql database
# Derfor nedarver den fra 'models.Model'
class Opskrift(models.Model):

    # Opskriften har to streng felter
    titel = models.CharField(max_length=100)
    instrukser = models.CharField(max_length=1000)

    # En opskrift kan have mange forskellige ingrdienser
    # Derfor dannes en relation til mange ingrdienser.
    ingredienser = models.ManyToManyField('Ingrediens',)

    # Display værdien af table entry.
    def __str__(self):
        return self.titel


# En tabel med alle de forskellige ingredienser,
# som opskrifteren ellere brugerne referer til
class Ingrediens(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     koeleskab = models.ForeignKey('koeleskab', )


# class Koeleskab(models.Model):
#     ingredienser = models.ManyToManyField('Ingrediens', on_delete=models.CASCADE)
