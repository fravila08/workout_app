from django.db import models
from user_app.models import User
from django.utils import timezone
# Create your models here.
class Day(models.Model):
    date = models.DateField(blank= False,  null=False, default=timezone.now().date())
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='days')

class Workout(models.Model):
    name = models.CharField(blank= False,  null=False)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='workouts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')

