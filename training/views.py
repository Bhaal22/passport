from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from django.template import RequestContext, loader

from training.models import Profile

# Create your views here.
def index(request):
    profiles = Profile.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
            'profiles': profiles,
        })
    return HttpResponse(template.render(context))
    


def detail(request, profile_id):
    profiles = Profile.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
            'profiles': profiles,
        })
    return HttpResponse(template.render(context))


class IndexView(ListView):
    model = Profile
    template_name = "index.html"

