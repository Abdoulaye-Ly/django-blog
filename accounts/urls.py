from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from blog.forms import UserRegisterForm

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]