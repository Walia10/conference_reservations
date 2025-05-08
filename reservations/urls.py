from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import home_redirect_view
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

#
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('reserve/<int:room_id>/', views.make_reservation, name='make_reservation'),
#     path('my-reservations/', views.my_reservations, name='my_reservations'),
#     path('available-rooms/', views.available_rooms, name='available_rooms'),
#
# ]

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('available_rooms/', views.available_rooms, name='available_rooms'),
#     path('reserve/<int:room_id>/', views.make_reservation, name='make_reservation'),
#     path('my_reservations/', views.my_reservations, name='my_reservations'),
# ]



urlpatterns = [

    path('', views.home, name='home'),
    path('available_rooms/', views.available_rooms, name='available_rooms'),
    path('confirm_booking/<int:room_id>/', views.confirm_booking, name='confirm_booking'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('adminpanel/', views.admin_dashboard, name='admin_dashboard'),
    path('adminpanel/rooms/', views.manage_rooms, name='manage_rooms'),
    path('adminpanel/rooms/add/', views.add_room, name='add_room'),
    path('adminpanel/rooms/edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('adminpanel/rooms/delete/<int:room_id>/', views.delete_room, name='delete_room'),
    path('adminpanel/reservations/', views.manage_reservations, name='manage_reservations'),
    path('adminpanel/users/', views.manage_users, name='manage_users'),
    path('dashboard/', home_redirect_view, name='dashboard'),
    path('admin-dashboard/', login_required(TemplateView.as_view(template_name="reservations/admin_dashboard.html")),
         name='admin-dashboard'),
    path('user-dashboard/', login_required(TemplateView.as_view(template_name="reservations/user_dashboard.html")),
         name='user-dashboard'),
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),

]
