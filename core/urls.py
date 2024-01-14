from django.urls import path
from core.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('profile/', editprofile, name='profile'),
    path('login/', auth_views.LoginView.as_view(
        template_name='core/login.jinja'
    ), name='login')
]