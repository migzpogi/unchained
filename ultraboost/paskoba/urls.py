from django.urls import path

from . import views

app_name = 'paskoba'
urlpatterns = [
    path('', views.index, name='index'),
    path('quarantine/', views.quarantine, name='quarantine'),
    path('christmas/', views.christmas, name='christmas'),
]