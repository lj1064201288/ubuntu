from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import User
from .forms import UserFrom
# Create your views here.



def register(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserFrom(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = User()
            user.user_full_name = cleaned_data['user_full_name']
            user.user_sex = cleaned_data['user_sex']
            user.user_email = cleaned_data['user_email']
            user.user_age = cleaned_data['user_age']
            user.user_card = cleaned_data['user_card']
            user.user_phone_number = cleaned_data['user_phone_number']
            user.createby = cleaned_data['createby']
            # user.createtime = cleaned_data['createtime']
            # user.img_url = cleaned_data['img_url']
            # user.updateby = cleaned_data['updateby']
            user.user_password = cleaned_data['user_password']
            user.user_name = cleaned_data['user_name']
            user.is_active = cleaned_data['is_active']
            user.save()
            return HttpResponseRedirect(reverse('register'))

    else:
        form = UserFrom()

    context = {
        'users' : users,
        'form' : form,
    }

    return render(request, 'register.html', context=context)