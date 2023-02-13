from django.shortcuts import render
from django.http import HttpResponse

from .models import Code

# Create your views here.


def home(request):
    latest_code = Code.objects.filter(is_visible=True).last()
    if latest_code:
        return render(request, 'home.html', {'code': latest_code})
    else:
        return render(request, 'home.html', {'message': 'Revenez plus tard'})
