from django.core.management.base import BaseCommand, CommandError

import tarfile

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


