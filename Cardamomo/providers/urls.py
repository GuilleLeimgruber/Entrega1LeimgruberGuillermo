from django.urls import path

from providers.views import list_providers, create_provider, update_provider, ProvidersListView






urlpatterns = [
    path('list-providers/', ProvidersListView.as_view()),
    path('create-provider/', create_provider),
    path('update-provider/<int:id>/', update_provider)
    
]