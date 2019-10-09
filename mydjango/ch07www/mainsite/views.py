from django.shortcuts import render
from django.template.loader import get_template, TemplateDoesNotExist
from django.http import HttpResponse, Http404


from .models import *

# Create your views here.




def index(request):
    template = get_template('index.html')
    products = Product.objects.all()

    html = template.render(locals())

    return HttpResponse(html)

def detail(request, id):
    try:
        product = Product.objects.get(id=id)
        images = PPhoto.objects.filter(product=product)

    except:
        pass

    template = get_template('detail.html')
    html = template.render(locals())
    return HttpResponse(html)


