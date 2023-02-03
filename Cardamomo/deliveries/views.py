from django.shortcuts import render

from django.http import HttpResponse

from deliveries.models import Deliveries

from deliveries.forms import DeliveryForm

# Create your views here.


def create_delivery(request):

    if request.method == 'GET':

        context = {'form': DeliveryForm()}
        
        return render(request, 'deliveries/create_delivery.html', context=context)


    elif request.method == 'POST':

        form = DeliveryForm(request.POST)
        if form.is_valid():

            Deliveries.objects.create(
                client = form.cleaned_data['client'], 
                menu = form.cleaned_data['menu'], 
                payment_method = form.cleaned_data['payment_method'],
            )
            context = {'message': 'Delivery creado'}
            return render(request, 'deliveries/create_delivery.html', context=context)

        else:
                context = {
                    'form_errors': form.errors, 
                    'form': DeliveryForm()
                }
                return render(request, 'deliveries/create_delivery.html', context=context)
      




def list_deliveries(request):

    all_deliveries = Deliveries.objects.all()
    context = {'deliveries': all_deliveries}

    return render(request, 'deliveries/list_deliveries.html', context=context)





