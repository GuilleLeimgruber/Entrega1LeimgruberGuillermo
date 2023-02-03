from django.urls import path

from menus.views import list_menus, create_menu, create_category, list_categories, update_menu




urlpatterns = [
    path('create-menu/', create_menu),
    path('list-menus/', list_menus),
    path('create-category/', create_category),
    path('list-categories/', list_categories),
    path('update-menu/<int:id>/', update_menu),
]