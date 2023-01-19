from django.shortcuts import render

from django.http import HttpResponse

from deliveries.models import Deliveries

# Create your views here.


def create_delivery(request):
   

    Deliveries.objects.create(client = 'Emilia Leimgruber', menu = 'Cochinita pibil', create_time =(), payment_method = 'card')

    return HttpResponse('Se creo un nuevo pedido')


def list_deliveries(request):

    all_deliveries = Deliveries.objects.all()
    context = {'deliveries': all_deliveries}

    return render(request, 'deliveries/list_deliveries.html', context=context)





