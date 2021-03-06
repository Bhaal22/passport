from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.utils import trailing_slash
from tastypie.http import HttpGone
from training.models import Profile

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


class ProfileResource(ModelResource):
    class Meta:
        queryset = Profile.objects.all()
        allowed_methods = ['get']
        resource_name = 'profile'

class HeartFC(ModelResource):
    class Meta:
        queryset = Profile.objects.all()
        list_allowed_methods = []
        detail_allowed_methods = ['post']
        resource_name = 'heartfc'

    def prepend_urls(self):
        """ Add the following array of urls to the GameResource base urls """
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\d+)/fc_run%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('fc_run'), name="api_fc_run"),

            url(r"^(?P<resource_name>%s)/fc_run%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('fc_run_list'), name="api_fc_run_list"),

            url(r"^(?P<resource_name>%s)/(?P<pk>\d+)/fc_bike%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('fc_bike'), name="api_fc_bike"),
        ]
        
    # def fc_run_list(self, request, **kwargs):
    #      """ proxy for the profile_fc_run method """  

    #      # you can do a method check to avoid bad requests
    #      self.method_check(request, allowed=['get'])

    #      try:
    #          basic_bundle = self.build_bundle(request=request)
    #          # using the primary key defined in the url, obtain the profile
    #          profiles = self.cached_obj_get_list(basic_bundle,
    #                                        **self.remove_api_resource_names(kwargs))

    #          # Return what the method output, tastypie will handle the serialization
    #          #return self.create_response(request, profile.fc_run(0.2))
    #          return HttpGone("list working! %d" % profiles.count())
    #      except ObjectDoesNotExist:
    #          return HttpGone("does not exist !")
    #      except MultipleObjectsReturned:
    #          return HttpMultipleChoices("More than one resource is found at this URI.")

    def fc_run(self, request, **kwargs):
         """ proxy for the profile_fc_run method """  

         # you can do a method check to avoid bad requests
         self.method_check(request, allowed=['post'])

         try:
             basic_bundle = self.build_bundle(data={'pk': kwargs['pk']}, request=request)
             # using the primary key defined in the url, obtain the profile
             profile = self.cached_obj_get(basic_bundle,
                                           **self.remove_api_resource_names(kwargs))

             # Return what the method output, tastypie will handle the serialization
             #return self.create_response(request, profile.fc_run(0.2))
             rate = float(request.POST.get('rate', ''))

             return self.create_response(request, profile.fc_run(rate))
         except ObjectDoesNotExist:
             return HttpGone("does not exist !")
         except MultipleObjectsReturned:
             return HttpMultipleChoices("More than one resource is found at this URI.")
