from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('light_sensor', views.light_sensor, name='light_sensor'),
]
