from django.shortcuts import render

from django.http import HttpResponse

import datetime

from reservations.models import Reservations


# Create your views here.

def create_reservation(request):
    Reservations.objects.create(name = 'Carolina Gimenez', dinner = 10, reservation_date = "2023-01-19")

    return HttpResponse('Se creo una nueva reserva')



def list_reservations(request):

    all_reservations = Reservations.objects.all()
    context = {'reservations': all_reservations}

    return render(request, 'reservations/list_reservations.html', context=context)
