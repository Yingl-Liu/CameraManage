from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    url(r'^camerainfo/$', views.snippet_list),
    url(r'^camerainfo/(?P<pk>[0-9]+)$', views.snippet_detail),
    url(r'^camerainfo/search/(?P<x1>(-?\d+)(\.\d+)?),(?P<y1>(-?\d+)(\.\d+)?)/(?P<x2>(-?\d+)(\.\d+)?),(?P<y2>(-?\d+)(\.\d+)?)/(?P<x3>(-?\d+)(\.\d+)?),(?P<y3>(-?\d+)(\.\d+)?)/(?P<x4>(-?\d+)(\.\d+)?),(?P<y4>(-?\d+)(\.\d+)?)/$', views.snippet_search),
    # url(r'^image/$', views.image_list),
    # url(r'^image/(?P<pk>[0-9]+)$', views.image_detail),
    url(r'^recombinationnode/$', views.mat_list),
    url(r'^recombinationnode/(?P<pk>[0-9]+)$', views.mat_detail),
   ]

