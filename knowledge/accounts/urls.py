from django.urls import path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'accounts'
urlpatterns = [

url(r'^home/$', accounts_views.home, name='home'),
url(r'^register/$', accounts_views.register, name='register'),
url(r'^login/$', accounts_views.login_user, name='login'),
url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
url(r'^dashboard/$', accounts_views.dashboard, name='dashboard'),

]

