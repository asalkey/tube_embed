from django.conf.urls import patterns, include, url
from tube.views import index,List,show

urlpatterns = patterns('',
    url(r'^$', index.as_view()),
    url(r'^list/', List.as_view() , name='list'),
    url(r'^show/(?P<pk>[-_\w]+)/$', show.as_view(), name='show-detail'),
)
