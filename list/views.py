from django.shortcuts import render
from django.template.response import TemplateResponse

from add.models import User

def ListPage(request):
    user = User.objects.all()
    return TemplateResponse(request, 'list.html', { "user" : user})
