import datetime

import django
from django.db import models



class PokemonTrainer(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()


    def __str__(self): return self.first_name + " " + self.last_name

class Pokemon(models.Model):
    CHOICES = (
        ('e', 'Electro'),
        ('f', 'Fire'),
        ('g', 'Grass'),
        ('w', 'Water')
    )

    name = models.TextField()
    type = models.CharField(max_length=1, choices=CHOICES)
    level = models.IntegerField()
    catch_date = models.DateField(default=datetime.date.today())
    trainer = models.ForeignKey(PokemonTrainer, on_delete=models.CASCADE, null=True)
    def __str__(self): return self.name



