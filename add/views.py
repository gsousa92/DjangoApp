from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib import messages

from .models import User
from .forms import UserForm

def AddPage(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', 'Wrong Name/Email format, try again please')
            email = request.POST.get('email',  'Wrong Name/Email format, try again please')
            user = User(name = name, email = email)
            user.save()

            return HttpResponseRedirect('..')
    else:
        form = UserForm()

    return render(request, 'add.html', context=None)