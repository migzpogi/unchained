from django.shortcuts import render
from django.http import HttpResponse
from .lib.ilan import Ilan


def index(request):
    if request.method == 'POST':
        data = request.POST.get('textfield', None)
        clean_data = Ilan().is_string_number_valid(data)

        if clean_data:
            x = Ilan().get_qty(float(clean_data), 10000)
            context = {
                # always convert to int
                'amount': x,
                'rows': range(x),
                'amount_text': f"{x} Ultraboost(s) 'yan!"
            }
            return render(request, 'ilan/index.html', context)

    return render(request, 'ilan/index.html')
