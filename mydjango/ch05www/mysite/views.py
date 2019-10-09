from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.





def homepage(reqeust):
    return HttpResponse('Hello World!')



def about(request, date_num):
    return HttpResponse('Here\'s my {} Home!'.format(date_num))
