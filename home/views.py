# from django.http import HttpResponse

from django.shortcuts import render


def HomePage(request):
    return render(request, './index.html', context=None)
