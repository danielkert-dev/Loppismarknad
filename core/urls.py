from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views
from .forms import LoginForm
from core.views import ChangePasswordView


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/' , views.profile, name='profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]