from django.http import HttpResponse
from django.template import loader
from myproject.models import Actor, Role, Movie
import requests
import json


def index(request):
    search_query = request.GET.get('search_box', None)
    template = loader.get_template('index.html')
    context = {}

    if request.method == 'GET' and search_query is not None: 

        actor = Actor.objects.get(name__icontains=search_query)
        roles = Role.objects.get(actor=actor)
        
        r = requests.get('https://api.duckduckgo.com/?q=%s&format=json'%search_query)
        response = json.loads(r.text)

        context = {
            'actor': actor,
            'actor_image': response['Image'],
            'roles': roles
        }

    return HttpResponse(template.render(context, request))
