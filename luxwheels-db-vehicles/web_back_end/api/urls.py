from django.urls import path
from . import views

urlpatterns = [
    path('vehicle/', views.getVehicle),
    path('user/', views.getCreateUser),
    path('reservation/', views.getPostReservation),
]
