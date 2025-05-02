from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Reservation
from .forms import ReservationForm
from datetime import date

def home(request):
    rooms = Room.objects.all()
    return render(request, 'reservations/home.html', {'rooms': rooms})

@login_required
def make_reservation(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.room = room
            reservation.save()
            return redirect('my_reservations')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form, 'room': room})

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/my_reservations.html', {'reservations': reservations})
