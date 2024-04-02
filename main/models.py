from django.db import models


class Lights(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)


class Temperatures(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)


class Humidities(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)


class Pressures(models.Model):
    value = models.FloatField("Значение")
    datetime = models.DateTimeField("Время")

    def __str__(self):
        return str(self.value)
