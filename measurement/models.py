from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.CharField(max_length=100, verbose_name='Описание', default='датчик в доме')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='temperatures')
    temperature = models.IntegerField()
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Показание'
        verbose_name_plural = 'Показания'

    # def __str__(self):
    #     return self.temperature
