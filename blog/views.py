from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def blog_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog.html')


def blog_detail_view(request: HttpRequest, blog_id: int) -> HttpResponse:
    return render(request, 'blog_detail.html')


def contact_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')
