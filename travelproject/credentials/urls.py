from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about')
]
