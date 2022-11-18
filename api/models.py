from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Meal(models.Model):
    title= models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Rating(models.Model):
    meal = models.ForeignKey(Meal, related_name='meal_reating', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_rating', on_delete=models.CASCADE)
    start = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])

    def __str__(self):
        return self.meal.title

    class Meta:
        unique_together = (('meal','user'))
        index_together = (('meal','user'))