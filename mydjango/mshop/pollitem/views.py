from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import messages
from cart.cart import Cart\

import datetime
from .models import *
from .forms import *
# Create your views here.

def index(request, cat_id=None):

    all_product = None
    all_cateories = Category.objects.all()

    if cat_id is not None:
        try:
            category = Category.objects.get(id=int(cat_id))
        except:
            category = None
        if category is not None:
            all_product = Products.objects.filter(category=category)
    if all_product is None:
        all_product  = Products.objects.all().order_by('-sku')

    pagiator = Paginator(all_product, 4)
    p = request.GET.get('page')
    try:
        products = pagiator.page(p)
    except PageNotAnInteger:
        products = pagiator.page(1)
    except EmptyPage:
        products = pagiator.page(pagiator.num_pages)


    temprate = get_template('index.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = temprate.render(request_content)

    return HttpResponse(html)

def product(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
    except:
        product_id = None


    template = get_template('product.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)

def add_to_cart(request, product_id, quantity):
    product = Products.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity=quantity)
    return redirect('/')

def remove_from_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

    return redirect('/cart/')
