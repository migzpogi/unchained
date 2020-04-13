from django.shortcuts import render
from django.http import HttpResponse
from .lib.araw import Araw


def christmas_context():
    christmas = Araw().is_today_christmas()
    return {
        'status': 'Hindi.',
        'accuracy': f'{christmas[1]}% accurate'
    }


def quarantine_context():
    acc = round((31/365) * 100, 2)
    return {
        'status': 'Hindi.',
        'accuracy': f'{acc}% accurate'
    }


def index(request):
    return HttpResponse('Hello.')


def quarantine(request):
    context = quarantine_context()
    return render(request, 'paskoba/quarantine.html', context)


def christmas(request):
    context = christmas_context()
    return render(request, 'paskoba/christmas.html', context)