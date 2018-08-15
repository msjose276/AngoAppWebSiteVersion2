

from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='homepage'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('process', views.process, name='process'),
    path('portfolio', views.portfolio, name='portfolio'),
]