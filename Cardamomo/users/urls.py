from django.contrib.auth.views import LogoutView

from django.urls import path

from users.views import view_login, view_signup, update_user, update_user_profile


urlpatterns = [
    path('login/', view_login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('signup/', view_signup, name = 'singup'),
    path('update/', update_user, name = 'update_user'),
    path('update/profile/', update_user_profile, name = 'update_user_profile'),
    
]
   