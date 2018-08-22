

from django.urls import path

from . import views
from django.conf.urls import handler404

urlpatterns = [

    path('', views.index, name='homepage'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('process', views.process, name='process'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('<str:keyword>/', views.project_detail, name='project_detail'),

]

#handler404 = views.error404