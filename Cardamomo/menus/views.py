from django.shortcuts import render

from django.http import HttpResponse

from menus.models import Menus, Categories

# Create your views here.


def create_menu(request):

    Menus.objects.create(name = 'Cochinita Pibil', price = 1400, stock = True)

    return HttpResponse('Se creo un nuevo menu')



def list_menus(request):

    all_menus = Menus.objects.all()
    context = {'menus': all_menus}

    return render(request, 'menus/list_menus.html', context=context)


def create_category(request):

    return HttpResponse('Se creo una nueva categoria')



def list_categories(request):

    all_categories = Categories.objects.all()
    context = {'categories': all_categories}

    return render(request, 'categories/list_categories.html', context=context)   



