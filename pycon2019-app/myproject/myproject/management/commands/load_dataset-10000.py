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

        movies = {}
        actors = {}
        roles = {}

        self.stdout.write(self.style.SUCCESS('Loading movies' ))

        with open('/movies-dataset/movies.json') as movies_file:
            for line in movies_file.readlines():
                movie_json = json.loads(line)
                movies[movie_json['id']] = movie_json
                #self.stdout.write(self.style.SUCCESS('Loading %s (%s)' % (movie_json['title'], movie_json['release_date'])))

        self.stdout.write(self.style.SUCCESS('Loading actors' ))

        with open('/movies-dataset/actors.json') as actors_file:
            for line in actors_file.readlines():
                actor_json = json.loads(line)
                actors[actor_json['id']] = actor_json
                #self.stdout.write(self.style.SUCCESS('Loading %s' % actor_json['name']))
        
        self.stdout.write(self.style.SUCCESS('Loading roles' ))
        with open('/movies-dataset/roles.json') as roles_file:
            for line in roles_file.readlines()[:5000]:
                role_json = json.loads(line)

                #roles[roles_json['id']] = roles_json
                self.stdout.write(self.style.SUCCESS('Loading %s (movie id: %s)' % (role_json['role_name'], role_json['movie_id'])))

                try:
                    movie_json = movies[role_json['movie_id']]
                    movie = Movie(
                        id=movie_json['id'],
                        title=movie_json['title'],
                        release_date=movie_json['release_date'],
                        overview=movie_json['overview'],
                        genre=movie_json['genre'],
                        tagline=movie_json['tagline'],
                        original_language=movie_json['original_language'],
                        runtime=float(movie_json['runtime']) if movie_json['runtime'] is not '' else 0
                    )
                    self.stdout.write(self.style.SUCCESS('Loading %s (%s)' % (movie_json['title'], movie_json['release_date'])))
                    movie.save()

                    actor_json = actors[role_json['actor_id']]
                    actor = Actor(id=actor_json['id'], name=actor_json['name'])
                    self.stdout.write(self.style.SUCCESS('Loading %s' % actor_json['name']))
                    actor.save()

                    r = Role(role_name=role_json['role_name'], movie=movie, actor=actor)
                    self.stdout.write(self.style.SUCCESS('Loading [%s] (movie id: %s)' % (role_json['role_name'], role_json['movie_id'])))
                    r.save()
                except Exception as e:
                    self.stdout.write(self.style.ERROR('%s' % e))


            
