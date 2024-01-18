from django.urls import path
from .views import Register, Actions, Log_in, Log_out

urlpatterns = [
    path('', Register.as_view(), name='register'),
    path('info/', Actions.as_view(), name='info'),
    path('login/', Log_in.as_view(), name='login'),
    path('logout/', Log_out.as_view(), name='logout'),
]
