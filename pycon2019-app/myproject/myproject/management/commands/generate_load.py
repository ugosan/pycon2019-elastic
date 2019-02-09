from django.core.management.base import BaseCommand, CommandError
from myproject.models import Actor, Movie, Role
import tarfile
import os
import json
import requests
import time
import elasticapm
import random

class Command(BaseCommand):
    
    @elasticapm.capture_span()
    def handle(self, *args, **options):

        while(True):
            random_actor = Actor.objects.order_by('?').first()
            requests.get('http://localhost:8000?search_box=%s'%random_actor.name)
            time.sleep(random.uniform(0.1,1))
