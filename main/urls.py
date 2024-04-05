"""
URL configuration for kangmark project.

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
from django.urls import path, include
from main import views

urlpatterns = [
    # path('', views.data),
    path('users/', views.user_list),
    path('me/', views.me),
    path('courses/', views.courses), #메인페이지 강의 보여주기
    path('schedule/courses/', views.schedule), #스케쥴 페이지
    path('duration_time/', views.duration_time), #이용현황 페이지  
    path('duration_time/subjects/', views.subjects), 
    path('courses/due_date/', views.due_date), 
    path('kangmark/', views.kangmark) 

]
