from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^$', views.invite_home, name='invite_home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', logout, {'next_page': '/invite_home'}),
    url(r'^user_invitation/', views.user_invitation, name='user_invitation'),
    url(r'^my_events/', views.events, name='events'),
    url(r'^user_reminder/$', views.user_reminder, name='user_reminder'),
    url(r'^invite_survey/$', views.invite_survey, name='invite_survey'),
    url(r'^status/(?P<eid>\w+)/$', views.event_status, name='event_status'),
    url(r'^approved/(?P<pid>\w+)/$', views.approved, name='approved'),
    url(r'^survey/(?P<pid>\w+)/$', views.survey, name='survey'),
    url(r'^event_feedback/$', views.event_feedback, name='event_feedback'),
    url(r'^survey_complete/$', views.survey_complete, name='survey_complete'),
    url(r'^postsurvey/$', views.postsurvey, name='postsurvey'),
    url(r'^postform/$', views.postform, name='postform'),

]

