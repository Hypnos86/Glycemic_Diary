from django.db import models

# Create your models here.
class TimeOfDay(models.Model):
    class Meta:
        verbose_name = 'Posiłek'
        verbose_name_plural = 'Posiłki'

    meal = models.CharField('Posiłek', max_length=50)

    def __str__(self):
        return f'{self.meal}'


class GlucoseRange(models.Model):
    class Meta:
        verbose_name = 'Zakres glukozy'
        verbose_name_plural = 'Zakresy glukozy'

    glucose_range = models.IntegerField('Zakres glikozy')

    def __str__(self):
        return f'{self.glucose_range}'


class Diary(models.Model):
    class Meta:
        verbose_name = 'Dziennik'
        verbose_name_plural = 'Dziennik'

    date = models.DateField('Data pomiaru', auto_now_add=True)
    time = models.TimeField('Czas pomiaru', auto_now_add=True)
    time_of_day = models.ForeignKey(TimeOfDay, related_name='Diary', verbose_name='Rodzaj posiłku',
                                    on_delete=models.CASCADE)
    measurement = models.IntegerField('Pomiar glukozy')
    information = models.TextField('Informacje', null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='Diary', verbose_name='Użytkownik', )

    def __str__(self):
        return f'Pomiar z dnia {self.date} (godzina: {self.time}) - posiłek: {self.time_of_day}, pomiar glukozy: {self.measurement}'
