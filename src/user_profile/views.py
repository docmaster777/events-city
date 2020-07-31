from pprint import pprint

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.views.generic import FormView
from django.template.context_processors import csrf


from .forms import  *

def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('user_profile_view', user.id)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'user_profile/sign_in.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'], password=cd['password1'])
            user = authenticate(username=cd['username'], password=cd['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('user_profile_view', user.id)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserCreationForm()
    return render(request, 'user_profile/sign_up.html', {'form': form})




def view(request, user_id):
    user_request_id = request.user.id

    if(user_request_id):
        user = get_object_or_404(User, id=user_request_id)

        return render(request, 'user_profile/view.html', {'user': user})
    else:
        context = {}
        context.update(csrf(request))
        return render(request, '403.html', context=context)