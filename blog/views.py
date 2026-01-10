from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse


blogs = [
    {
        'id': 1,
        'title': 'Python Functions',
        'content': 'Python dasturlash tilida function yaratish def kalit so‘zi orqali amalga oshiriladi.',
        'likes': 10
    },
    {
        'id': 2,
        'title': 'Django Models',
        'content': 'Django ORM yordamida database modellarini oson va tez yaratish mumkin.',
        'likes': 25
    },
    {
        'id': 3,
        'title': 'REST API nima?',
        'content': 'REST API client va server o‘rtasida ma’lumot almashish uchun ishlatiladi.',
        'likes': 18
    },
    {
        'id': 4,
        'title': 'Python List Comprehension',
        'content': 'List comprehension yordamida kodni qisqa va tushunarli yozish mumkin.',
        'likes': 30
    },
    {
        'id': 5,
        'title': 'Django Views',
        'content': 'Django views HTTP requestlarni qabul qilib, response qaytaradi.',
        'likes': 22
    },
    {
        'id': 6,
        'title': 'Class-based Views',
        'content': 'CBV yordamida kodni qayta ishlatish va strukturalash osonlashadi.',
        'likes': 15
    },
    {
        'id': 7,
        'title': 'Python Virtual Environment',
        'content': 'Virtual environment loyihalar orasida dependency konfliktini oldini oladi.',
        'likes': 40
    },
    {
        'id': 8,
        'title': 'PostgreSQL bilan Django',
        'content': 'PostgreSQL — Django uchun eng tavsiya etiladigan production database.',
        'likes': 35
    },
    {
        'id': 9,
        'title': 'Gunicorn va Nginx',
        'content': 'Gunicorn Django appni run qiladi, Nginx esa reverse proxy vazifasini bajaradi.',
        'likes': 28
    },
    {
        'id': 10,
        'title': 'Celery Background Tasks',
        'content': 'Celery yordamida background tasklarni async tarzda bajarish mumkin.',
        'likes': 50
    }
]


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def about_view(request: HttpRequest) -> HttpResponse:
    data = {
        'first_name': 'Ali',
        'last_name': "Valiyev",
        'phone': '+998991231212',
        'email': 'alijon@gmail.com'
    }
    return render(request, 'about.html', context=data)


def blog_view(request: HttpRequest) -> HttpResponse:
    data = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context=data)


def blog_detail_view(request: HttpRequest, blog_id: int) -> HttpResponse:
    for blog in blogs:
        if blog_id == blog['id']:
            data = {
                'blog': blog
            }
            return render(request, 'blog_detail.html', context=data)
        
    data = {
        'blogs': blogs,
        'error': 'Bunday blog mavjud emas!'
    }
    return render(request, 'blog.html', context=data)


def contact_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')
