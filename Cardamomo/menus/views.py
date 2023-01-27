from django.shortcuts import render

from django.http import HttpResponse

from menus.models import Menus, Categories

from menus.forms import MenuForm

# Create your views here.


def create_menu(request):

    if request.method == 'GET':

        context = {'form': MenuForm()}
        
        return render(request, 'menus/create_menu.html', context=context)


    elif request.method == 'POST':

        form = MenuForm(request.POST)
        if form.is_valid():

            Menus.objects.create(name = form.cleaned_data['name'], price =form.cleaned_data['price'], stock = form.cleaned_data['stock'],)
            context = {'message': 'Menu creado'}
            return render(request, 'menus/create_menu.html', context=context)

        else:
                context = {'form_errors': form.errors, 'form': MenuForm()}
                return render(request, 'menus/create_menu.html', context=context)
      


def list_menus(request):

    if 'search' in request.GET:
        search = request.GET['search']

        menus = Menus.objects.filter(name__contains=search)
    
    else:

        menus = Menus.objects.all()
    context = {'menus': menus}

    return render(request, 'menus/list_menus.html', context=context)


def create_category(request):

    return HttpResponse('Se creo una nueva categoria')



def list_categories(request):

    all_categories = Categories.objects.all()
    context = {'categories': all_categories}

    return render(request, 'categories/list_categories.html', context=context)   



