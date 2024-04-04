import datetime

from django.db import models


class Lights(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)

    def time(self):
        return self.datetime.strftime('%d.%m %H:%M')


class Temperatures(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)

    def time(self):
        return self.datetime.strftime('%d.%m %H:%M')


class Humidities(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)

    def time(self):
        return self.datetime.strftime('%d.%m %H:%M')


class Pressures(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)

    def time(self):
        return self.datetime.strftime('%d.%m %H:%M')
