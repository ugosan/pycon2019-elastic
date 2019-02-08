from django.core.management.base import BaseCommand, CommandError
from myproject.models import Actor, Movie, Role
import tarfile
import os
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Unpacking dataset (movies)...'))

        tar = tarfile.open('/movies-dataset/movies.json.tar.gz', "r:gz")
        tar.extractall('/movies-dataset/')
        tar.close()

        self.stdout.write(self.style.SUCCESS('Unpacking dataset (actors)...'))

        tar = tarfile.open('/movies-dataset/actors.json.tar.gz', "r:gz")
        tar.extractall('/movies-dataset/')
        tar.close()

        self.stdout.write(self.style.SUCCESS('Unpacking dataset (roles)...'))

        tar = tarfile.open('/movies-dataset/roles.json.tar.gz', "r:gz")
        tar.extractall('/movies-dataset/')
        tar.close()


        with open('/movies-dataset/movies.json') as movies_file:
            for line in movies_file.readlines():
                movie_json = json.loads(line)
                self.stdout.write(self.style.SUCCESS('Loading %s (%s)' % (movie_json['title'], movie_json['release_date'])))
                
                try:
                    m = Movie(
                        id=movie_json['id'], 
                        title=movie_json['title'],
                        release_date=movie_json['release_date'],
                        overview=movie_json['overview'],
                        genre=movie_json['genre'],
                        tagline=movie_json['tagline'],
                        original_language=movie_json['original_language'],
                        runtime=float(movie_json['runtime']) if movie_json['runtime'] is not '' else 0
                    )
                    m.save()
                except Exception as e:
                    self.stdout.write(self.style.ERROR('Error Loading %s (%s): %s' % (movie_json['title'], movie_json['release_date'], e)))
                    

        with open('/movies-dataset/actors.json') as actors_file:
            for line in actors_file.readlines():
                actor_json = json.loads(line)
                self.stdout.write(self.style.SUCCESS('Loading %s' % actor_json['name']))
                actor = Actor(id=actor_json['id'], name=actor_json['name'])
                actor.save()

         with open('/movies-dataset/roles.json') as roles_file:
            for line in roles_file.readlines():
                roles_json = json.loads(line)
                self.stdout.write(self.style.SUCCESS('Loading %s (movie id: %s)' % (roles_json['role_name'], roles_json['movie_id'])))
                try:
                    movie = Movie.objects.get(id=roles_json['movie_id'])
                    actor = Actor.objects.get(id=roles_json['actor_id'])
                    r = Role(role_name=roles_json['role_name'], movie=movie, actor=actor)
                    r.save()
                except Exception as e:
                    self.stdout.write(self.style.ERROR('%s' % e))
