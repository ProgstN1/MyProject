from django.shortcuts import render
from django.http import HttpResponse

def reg_page(request):
    return render(request, 'register_app/reg_page.html')
