from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def about_view(request: HttpRequest) -> HttpResponse:
    data={
        'first_name': 'Azizbek',
        'last_name': 'Juraqulov',
        'phone': '+998-94-566-58-66',
        'email': 'juraqulovazizbek@gmail.com',
    }
    return render(request, 'about.html', context=data)


def blog_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog.html')


def blog_detail_view(request: HttpRequest, blog_id: int) -> HttpResponse:
    return render(request, 'blog_detail.html')


def contact_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')
