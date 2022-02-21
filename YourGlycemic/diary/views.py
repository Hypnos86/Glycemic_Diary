from django.shortcuts import render
from diary.models import Diary


# Create your views here.
def list_of_measurements(request):
    diary = Diary.objects.all()
    context = {'diary_list': diary}
    return render(request, 'diary_list.html', context)
