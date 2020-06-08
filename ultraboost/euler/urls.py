from django.urls import path

from . import views

app_name = 'euler'
urlpatterns = [
    path('', views.index, name='index'),
]
