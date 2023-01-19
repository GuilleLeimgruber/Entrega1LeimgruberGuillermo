from django.urls import path

from deliveries.views import list_deliveries, create_delivery




urlpatterns = [
    path('create-delivery/', create_delivery),
    path('list-deliveries/', list_deliveries),
]