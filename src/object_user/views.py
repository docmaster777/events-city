from django.shortcuts import render, redirect
from .forms import *

def create(request):
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


    return render(request, 'object_user/create.html', {'form': form })
