from django.shortcuts import render
from .lib.araw import Araw

def christmas_context():
    christmas = Araw().is_today_christmas()
    return {
        'status': 'Hindi.',
        'accuracy': f'{christmas[1]}% accurate'
    }


def index(request):
    context = christmas_context()
    return render(request, 'paskoba/index.html', context)