"""{{ pitaya }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from emailsadd import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^emailsadd/', include('emailsadd.urls'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout, {'next_page': '/emailsadd'}),
    url(r'^register/$', views.register, name='register'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^invitehome$', views.invitehome, name='invitehome'),
    #url(r'^reminder', views.reminder, name='reminder'),
    # url(r'^invitation', views.invitation, name='invitation'),
    # url(r'^invite_survey', views.invite_survey, name='invite_survey')

]



