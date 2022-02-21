from django.forms import ModelForm, DateInput, TimeInput
from diary.models import Diary


class DateField(DateInput):
    input_type = 'date'


class TimeField(TimeInput):
    input_type = 'time'


class DiaryForm(ModelForm):
    class Meta:
        model = Diary

        fields = ['date', 'time', 'time_of_day', 'measurment', 'information', 'user']

        field_order = ['date', 'time', 'time_of_day', 'measurment', 'information']

        labels = {'date': 'Data pomiaru', 'time': 'Czas pomiaru', 'time_of_day': 'Posiłek',
                  'measurement': 'Pomiar glukozy', 'information': 'Informacje'}

        exclude = ['user']

        widgets = {'date': DateField(), 'time': TimeField()}
