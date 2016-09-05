from . import views
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.invitehome, name='invitehome'),
    url(r'^register/$', views.register, name='register'),
    # url(r'^invitation', views.invitation, name='invitation'),
    # url(r'^postform/$', views.postform, name='addform'),
    url(r'^login/$', 'django.contrib.auth.views.login'),


]

#  url(r'^invitehome$', views.invitehome, name='invitehome'),
#  url(r'^reminder', views.reminder, name='reminder'),
#  url(r'^invite_survey', views.invite_survey, name='invite_survey')