from django.shortcuts import render
# from .lib.euler_001 import hello


def index(request):
    return render(request, 'euler/index.html')