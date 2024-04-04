from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('temperatures', views.temperatures_chart, name='temperatures'),
    path('humidities', views.humidities_chart, name='humidities'),
    path('pressures', views.pressures_chart, name='pressures'),
    path('lights', views.lights_chart, name='lights'),

    path('light_sensor', views.light_sensor, name='light_sensor'),
    path('temperature_sensor', views.temperature_sensor, name='temperature_sensor'),
]
