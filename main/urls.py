from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('temperatures', views.temperatures_chart, name='temperatures'),  # Статистика температур
    path('humidities', views.humidities_chart, name='humidities'),  # Статистика влажности
    path('pressures', views.pressures_chart, name='pressures'),  # Статистика давления
    path('lights', views.lights_chart, name='lights'),  # Статистика освещенности

    # Датчик освещенности (в реальном времени)
    path('light_sensor', views.light_sensor, name='light_sensor'),
    # Датчик температуры (в реальном времени)
    path('temperature_sensor', views.temperature_sensor, name='temperature_sensor'),
]
