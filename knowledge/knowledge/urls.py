"""knowledge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from accounts import views as accounts_views
from quiz import views as quiz_views
from django.contrib.auth import views as auth_views

urlpatterns = [
url(r'^home/$', accounts_views.home, name='home'),
url(r'^register/$', accounts_views.register, name='register'),
url(r'^login/$', accounts_views.login_user, name='login'),
url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
url(r'^dashboard/$', accounts_views.dashboard, name='dashboard'),
url(r'^quiz/$', quiz_views.question_single, name='quiz'),
url(r'^quiz/result$', quiz_views.answer_result, name='answer_result'),
path('admin/', admin.site.urls),
]
