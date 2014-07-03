from django.conf.urls import patterns, url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tastypie.api import Api
from training.api.resources import ProfileResource, HeartFC

from training.views import IndexView


v1_api = Api(api_name='v1')
v1_api.register(ProfileResource())
v1_api.register(HeartFC())

#url(r'^profile/(?P<profile_id>\d+)/$', views.detail, name='detail'),
urlpatterns = patterns('', 
                       url(r'^$', IndexView.as_view (), name='index'),
                       url(r'^api/', include(v1_api.urls)))

urlpatterns += staticfiles_urlpatterns()

#urlpatterns = patterns('',
#  # ...more URLconf bits here...
#  # Then add:
#  (r'^api/', include(v1_api.urls)),
#)
