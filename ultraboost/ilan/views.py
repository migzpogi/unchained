from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        data = request.POST.get('textfield', None)
        x = compute(int(data), 10000)
        context = {
            # always convert to int
            'amount': x,
            'rows': range(x),
            'amount_text': f"{x} Ultraboost(s) 'yan!"
        }
        return render(request, 'ilan/index.html', context)

    return render(request, 'ilan/index.html')


def compute(dividend, divisor):
    return round(dividend/divisor)