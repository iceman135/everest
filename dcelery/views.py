from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
#test 
from .tasks import celery_task

def celery_view(request):
    for counter in range(2):
        celery_task.delay(counter)
    return HttpResponse("FINISH PAGE LOAD")
