from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.invitehome, name='invitehome'),
    # url(r'^$', views.ListBookerView.as_view(), name='invitehome'),
    # url(r'^edit/(?P<pk>\d+)/$', views.UpdateBookerView.as_view(), name='invitehome'),
]