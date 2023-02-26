from django.shortcuts import render
from .models import *

from django.contrib import admin
from django.shortcuts import redirect

from admin_views.admin import AdminViews


# Create your views here.

def pie_chart(request):
    labels = []
    data = []

    queryset = Category.objects.all()[:5]
    
    for cat in queryset:
        labels.append(cat.title)
        data.append(2332134)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })



def index(request):
    return render(request,"index.html");
    

