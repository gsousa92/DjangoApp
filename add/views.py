from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib import messages



from .models import User

from add.models import User
from add.forms import UserForm

def AddPage(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            user = User(name = name, email = email)
            user.save()

            return HttpResponseRedirect('..')
    else:
        form = UserForm()

    return render(request, 'add.html', context=None)