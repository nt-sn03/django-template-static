from django.urls import path

from .views import home_page , projects_page , inbox_page , analytics_page , settings_page


urlpatterns = [
    path('', home_page, name='home_page'),
    path('projects/', projects_page , name='projects_page'),
    path('inbox/', inbox_page, name='inbox_page'),
    path('analytics/', analytics_page, name='analytics_page'),
    path('settings/', settings_page, name='settings_page')
]