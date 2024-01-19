from django.urls import path
from .views import A_day, All_Days

urlpatterns = [
    path("", All_Days.as_view(), name='all_days'),
    path('<str:date>/', A_day.as_view(), name='a_day'),
]