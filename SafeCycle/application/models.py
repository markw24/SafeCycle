from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator
# Create your models here.

class Reviews(models.Model):
    author = models.TextField()

    #PUT CHOICES FOR ROADS HERE
    ROAD_CHOICES = [('T1','T1'),('T2','T2'),('T3','T3')]
    given_road = models.TextField(choices = ROAD_CHOICES, blank = True)
    text = models.TextField(blank=True, validators=[MaxLengthValidator(400)])
    number_rating = models.DecimalField(max_digits=2, decimal_places=0,validators = [MaxValueValidator(10),MinValueValidator(0)])

    def __str__(self):
        return self.author


class Road(models.Model):
    name = models.TextField()
    rating = models.DecimalField(default=7,max_digits=2, decimal_places=0, blank=False, validators = [MaxValueValidator(10),MinValueValidator(0)])
    given_reviews = models.ManyToManyField(Reviews,blank=True)

    def __str__(self):
        return self.name


