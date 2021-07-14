from django.urls import path

from templates_advanced.pythons_auth.views import login_view, logout_user, register_user

urlpatterns = [
    path('register/', register_user, name = 'register user'),
    path('login/', login_view, name='login view'),
    path('logout/', logout_user, name='logout user'),
]