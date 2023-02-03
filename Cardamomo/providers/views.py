from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import ListView

from providers.models import Providers

from providers.forms import ProviderForm

# Create your views here.








def list_providers(request):

    providers = Providers.objects.filter(is_active = True)
       
    context = {'providers': providers}

    return render(request, 'providers/list_providers.html', context=context)

class ProvidersListView(ListView):

    model = Providers
    template_name = 'providers/list_providers.html'
    queryset = Providers.objects.filter(is_active = True)



def create_provider(request):

    if request.method == 'GET':

        context = {'form': ProviderForm()}
        
        return render(request, 'providers/create_provider.html', context=context)


    elif request.method == 'POST':

        form = ProviderForm(request.POST)
        if form.is_valid():

            Providers.objects.create(
                name = form.cleaned_data['name'], 
                address = form.cleaned_data['address'], 
                phone = form.cleaned_data['phone'], 
                tax_category = form.cleaned_data['tax_category'],
            )
            context = {'message': 'Proveedor creado'}
          
        else:
                context = {
                    'form_errors': form.errors, 
                    'form': ProviderForm()
                }
        return render(request, 'providers/create_provider.html', context=context)

def update_provider(request, id):
    provider = Providers.objects.get(id=id)

    if request.method == 'GET':
        
        context = {
            'form': ProviderForm(
                initial={
                    'name': provider.name, 
                    'address': provider.address,
                    'phone': provider.phone,
                    'tax_category': provider.tax_category,
                }
            )
        }
        
        return render(request, 'providers/update_provider.html', context=context)


    elif request.method == 'POST':

        form = ProviderForm(request.POST)
        if form.is_valid():

            provider.name = form.cleaned_data['name'], 
            provider.address = form.cleaned_data['address'], 
            provider.phone = form.cleaned_data['phone'], 
            provider.tax_category = form.cleaned_data['tax_category'],
            provider.save()
            
            context = {'message': 'Proveedor actualizado'}
          
        else:
                context = {
                    'form_errors': form.errors, 
                    'form': ProviderForm()
                }
        return render(request, 'providers/update_provider.html', context=context)
      

      
