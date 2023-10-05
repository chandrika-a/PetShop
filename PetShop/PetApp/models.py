from django.db import models

pet_type_choices = (
    ("Dog", "Dog"),
    ("Cat", "Cat")
)

class Pet(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=pet_type_choices)
    color = models.CharField(max_length=10)
    weight = models.FloatField()
    age = models.PositiveIntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    star = models.IntegerField()
    comment = models.TextField()