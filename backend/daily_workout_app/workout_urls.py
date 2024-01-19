from django.urls import path
from .views import A_workout, All_workouts

urlpatterns = [
    path("", All_workouts.as_view(), name="all_workouts"),
    path("<int:id>/", A_workout.as_view(), name='a_workout'),
]
