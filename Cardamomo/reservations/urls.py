from django.urls import path

from reservations.views import list_reservations, create_reservation




urlpatterns = [
    path('create-reservation/', create_reservation),
    path('list-reservations/', list_reservations),
]