from django.contrib import admin
from .models import TimeOfDay, GlucoseRange, Diary

# Register your models here.
admin.site.register(TimeOfDay)
admin.site.register(GlucoseRange)


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'time_of_day', 'measurement', 'user']
