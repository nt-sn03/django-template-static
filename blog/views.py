from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse


blogs = [
    {
        "id": 1,
        "title": "Advanced Django ORM: Optimization Techniques",
        "slug": "advanced-django-orm-optimization-techniques",
        "excerpt": "Deep dive into query optimization strategies for Django applications. Master select_related, prefetch_related, database indexing, and query analysis to build high-performance database layers that scale.",
        "author": "DevBlog Author",
        "published_date": "2026-01-05",
        "reading_time": "10 min read",
        "categories": ["Django", "Performance"],
        "tags": ["Django", "ORM", "Performance", "Optimization", "Database", "Python"],
        "featured_image_gradient": "from-indigo-500 to-purple-600"
    },
    {
        "id": 2,
        "title": "Designing Microservices with Domain-Driven Design",
        "slug": "designing-microservices-with-domain-driven-design",
        "excerpt": "Explore how Domain-Driven Design principles can guide the architecture of scalable microservices. Learn about bounded contexts, aggregates, and how to establish clear service boundaries that align with your business domain.",
        "author": "DevBlog Author",
        "published_date": "2026-01-08",
        "reading_time": "8 min read",
        "categories": ["Architecture", "Microservices"],
        "tags": ["Microservices", "DDD", "Architecture", "Software Design", "Backend"],
        "featured_image_gradient": "from-blue-500 to-blue-600"
    },
    {
        "id": 3,
        "title": "Testing Strategies for Python Backend Applications",
        "slug": "testing-strategies-python-backend-applications",
        "excerpt": "Comprehensive guide to building confidence in your Python backend through effective testing. Explore unit testing, integration testing, mocking strategies, and test organization patterns that scale with your codebase.",
        "author": "DevBlog Author",
        "published_date": "2026-01-02",
        "reading_time": "12 min read",
        "categories": ["Testing", "Best Practices"],
        "tags": ["Testing", "Python", "Unit Tests", "Integration Tests", "pytest", "TDD"],
        "featured_image_gradient": "from-emerald-500 to-teal-600"
    },
    {
        "id": 4,
        "title": "RESTful API Design: Principles and Best Practices",
        "slug": "restful-api-design-principles-best-practices",
        "excerpt": "Learn the fundamental principles of designing clean, intuitive RESTful APIs. From resource naming conventions to proper HTTP method usage, versioning strategies, and error handling patterns that make your APIs a joy to consume.",
        "author": "DevBlog Author",
        "published_date": "2025-12-28",
        "reading_time": "9 min read",
        "categories": ["API Design", "Best Practices"],
        "tags": ["REST", "API", "HTTP", "Web Services", "Backend", "Design Patterns"],
        "featured_image_gradient": "from-orange-500 to-red-600"
    },
    {
        "id": 5,
        "title": "Containerizing Django Applications with Docker",
        "slug": "containerizing-django-applications-with-docker",
        "excerpt": "Step-by-step guide to dockerizing your Django applications for development and production. Learn about multi-stage builds, environment configuration, docker-compose orchestration, and deployment strategies that ensure consistency across environments.",
        "author": "DevBlog Author",
        "published_date": "2025-12-24",
        "reading_time": "11 min read",
        "categories": ["DevOps", "Docker"],
        "tags": ["Docker", "DevOps", "Django", "Containers", "Deployment", "CI/CD"],
        "featured_image_gradient": "from-pink-500 to-rose-600"
    },
    {
        "id": 6,
        "title": "Building Scalable Task Queues with Celery and Redis",
        "slug": "building-scalable-task-queues-celery-redis",
        "excerpt": "Master asynchronous task processing in Python applications. Learn how to implement distributed task queues using Celery and Redis, handle long-running operations, schedule periodic tasks, and monitor worker performance.",
        "author": "DevBlog Author",
        "published_date": "2025-12-20",
        "reading_time": "13 min read",
        "categories": ["Architecture", "Performance"],
        "tags": ["Celery", "Redis", "Task Queue", "Async", "Python", "Scalability"],
        "featured_image_gradient": "from-cyan-500 to-blue-600"
    },
    {
        "id": 7,
        "title": "Implementing JWT Authentication in Django REST Framework",
        "slug": "implementing-jwt-authentication-django-rest-framework",
        "excerpt": "Comprehensive guide to securing your Django APIs with JSON Web Tokens. Understand JWT structure, implement token-based authentication, handle token refresh, and follow security best practices for modern web applications.",
        "author": "DevBlog Author",
        "published_date": "2025-12-15",
        "reading_time": "10 min read",
        "categories": ["Security", "Django"],
        "tags": ["JWT", "Authentication", "Security", "Django REST", "API", "OAuth"],
        "featured_image_gradient": "from-violet-500 to-purple-600"
    },
    {
        "id": 8,
        "title": "PostgreSQL Performance Tuning for Django Applications",
        "slug": "postgresql-performance-tuning-django-applications",
        "excerpt": "Optimize your PostgreSQL database for Django workloads. Learn about connection pooling, query planning, indexing strategies, EXPLAIN ANALYZE, vacuum operations, and configuration tuning that can 10x your database performance.",
        "author": "DevBlog Author",
        "published_date": "2025-12-10",
        "reading_time": "14 min read",
        "categories": ["Database", "Performance"],
        "tags": ["PostgreSQL", "Database", "Performance", "Django", "SQL", "Optimization"],
        "featured_image_gradient": "from-sky-500 to-indigo-600"
    },
    {
        "id": 9,
        "title": "Clean Code Principles for Python Developers",
        "slug": "clean-code-principles-python-developers",
        "excerpt": "Write maintainable, readable Python code that your team will thank you for. Explore naming conventions, function design, code organization, documentation practices, and refactoring techniques that lead to sustainable codebases.",
        "author": "DevBlog Author",
        "published_date": "2025-12-05",
        "reading_time": "7 min read",
        "categories": ["Best Practices", "Python"],
        "tags": ["Clean Code", "Python", "Code Quality", "Refactoring", "PEP 8", "Best Practices"],
        "featured_image_gradient": "from-green-500 to-emerald-600"
    },
    {
        "id": 10,
        "title": "Event-Driven Architecture with Python and Kafka",
        "slug": "event-driven-architecture-python-kafka",
        "excerpt": "Build resilient, scalable systems using event-driven patterns. Learn how to implement event sourcing, CQRS, and message streaming with Apache Kafka and Python. Understand when to use events vs traditional request-response patterns.",
        "author": "DevBlog Author",
        "published_date": "2025-11-30",
        "reading_time": "15 min read",
        "categories": ["Architecture", "Distributed Systems"],
        "tags": ["Kafka", "Event-Driven", "Architecture", "Python", "Microservices", "Messaging"],
        "featured_image_gradient": "from-amber-500 to-orange-600"
    }
]


def home_view(request: HttpRequest) -> HttpResponse:
    data = {
        'blogs': blogs[-3:]
    }
    return render(request, 'home.html', context=data)


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
        'blogs': blogs[-3:]
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