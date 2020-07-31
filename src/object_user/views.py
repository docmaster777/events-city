from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from .forms import *

def create(request):
    user_request_id = request.user.id

    if (user_request_id):
        if request.method == 'POST':
            form = ObjectUserCreateForm(request.POST)

            if form.is_valid():
                object_user = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                object_user.user_id = user.id
                object_user.save()

                return redirect('/')
        else:
            form = ObjectUserCreateForm()

        return render(request, 'object_user/create.html', {'form': form})
    else:
        context = {}
        context.update(csrf(request))
        return render(request, '403.html', context=context)




