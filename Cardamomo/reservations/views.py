from django.shortcuts import render

from django.http import HttpResponse

import datetime

from reservations.models import Reservations

from reservations.forms import ReservationsForm


# Create your views here.

def create_reservation(request):

    if request.method == 'GET':
        context = {'form': ReservationsForm()}

        return render(request, 'reservations/create_reservation.html', context=context) 

    elif request.method == 'POST':

        form = ReservationsForm(request.POST)
        if form.is_valid():

            Reservations.objects.create(
                name = form.cleaned_data['name'], 
                dinner = form.cleaned_data['dinner'], 
                reservation_date = form.cleaned_data['reservation_date'],
            )
            context = {'message': 'Reserva creada'}
            return render(request, 'reservations/create_reservation.html', context=context)

        else:
                context = {
                    'form_errors': form.errors, 
                    'form': ReservationsForm()
                }
                return render(request, 'reservations/create_reservation.html', context=context)



def list_reservations(request):

    all_reservations = Reservations.objects.all()
    context = {'reservations': all_reservations}

    return render(request, 'reservations/list_reservations.html', context=context)
