from django.core.management.base import BaseCommand, CommandError
from myproject.models import Actor, Movie, Role
import tarfile
import os
import json
import requests
import time


class Command(BaseCommand):

    def handle(self, *args, **options):

        while(True):
            random_actor = Actor.objects.order_by('?').first()
            requests.get('http://localhost:8000?search_box%s'%random_actor.name)
            time.sleep(1)
