from django.contrib import messages, auth

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Watch
from .forms import WatchForm

# from app.form import*
# Create your views here.


def index(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'index.html',data)

# def home(request):
#     return render(request,'index.html')


