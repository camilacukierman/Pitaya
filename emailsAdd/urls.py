from . import views
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout



urlpatterns = [
    url(r'^$', views.invite_home, name='invite_home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', logout, {'next_page': '/invite_home'}),
    url(r'^user_invitation/', views.user_invitation, name='user_invitation'),
    url(r'^user_reminder/$', views.user_reminder, name='user_reminder'),
    url(r'^invite_survey/$', views.invite_survey, name='invite_survey'),
    url(r'^postform/$', views.postform, name='addform'),
]

