from urllib import request
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest) -> HttpResponse:
    data = {
        'user': {
            'name': 'juraqulov Azizbek'
        },
        'dashboard': {
            'total_revenue': 30_450.00
        }
    }
    return render(request=request, template_name='index.html', context=data)

def projects_page(request: HttpRequest) -> HttpResponse:
        data = {
        'user': {
            'name': 'juraqulov Azizbek'
        }
    }
        return render(request=request, template_name='projects.html', context=data)

def inbox_page(request: HttpRequest) -> HttpResponse:
        data = {
        'user': {
            'name': 'juraqulov Azizbek'
        }
    }

        return render(request=request, template_name='inbox.html', context=data)

def analytics_page(request: HttpRequest) -> HttpResponse:
        data = {
        'user': {
            'name': 'juraqulov Azizbek'
        }
    }

        return render(request=request, template_name='analytics.html',context=data)
    
def settings_page(request: HttpRequest) -> HttpResponse:
        data = {
        'user': {
            'name': 'juraqulov Azizbek'
        }
    }

        return render(request=request, template_name='settings.html', context=data)