from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reserve/<int:room_id>/', views.make_reservation, name='make_reservation'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),

]
