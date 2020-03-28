from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .lib.araw import Araw


def index(request):
    context = {
        'sample_text': Araw().get_simple_date()
    }
    return render(request, 'paskoba/index.html', context)