from django.db import models

#{
#    "genre": "Adventure",
#    "id": "710",
#    "original_language": "en",
#    "overview": "James Bond must unmask the mysterious head o...",
#    "production_companies": "[{'name': 'United Artists', 'id': 60}, {'name': 'Eon Productions', 'id': 7576}]",
#    "release_date": "1995-11-16",
#    "runtime": "130.0",
#    "tagline": "No limits. No fears. No substitutes.",
#    "title": "GoldenEye"
#}
class Movie(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=128)
    original_language = models.CharField(max_length=3)
    overview = models.TextField()
    release_date = models.DateField()
    runtime = models.DecimalField(max_digits=10, decimal_places=2)
    tagline = models.CharField(max_length=255)

class Actor(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Role(models.Model):
    role_name = models.CharField(max_length=100)
    actor = models.ForeignKey('Actor',on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie',on_delete=models.CASCADE)
    

      