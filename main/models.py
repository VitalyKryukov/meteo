from django.db import models


# Модель для хранения данных с датчика освещенности
class Lights(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)

    # Функция вывода форматированного времени
    def time(self):
        return self.datetime.strftime('%d.%m %H:%M')


# Модель для хранения данных с датчика температуры
class Temperatures(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)

    # Функция вывода форматированного времени
    def time(self):
        return self.datetime.strftime('%d.%m %H:%M')


# Модель для хранения данных с датчика влажности
class Humidities(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)

    # Функция вывода форматированного времени
    def time(self):
        return self.datetime.strftime('%d.%m %H:%M')


# Модель для хранения данных с датчика давления
class Pressures(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)

    # Функция вывода форматированного времени
    def time(self):
        return self.datetime.strftime('%d.%m %H:%M')
