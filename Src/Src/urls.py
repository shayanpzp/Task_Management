"""
URL configuration for Src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import all_tasks, search_tasks, view_task, add_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_tasks, name='all_tasks'),
    path('search/', search_tasks, name='search_tasks'),
    path('task/<int:task_id>/', view_task, name='view_task'),
    path('add_task/', add_task, name='add_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]
