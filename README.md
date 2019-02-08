### Elastic APM Workshop - PyCon 2019 - Bogotá

#### Run the django app with `docker-compose`:

```shell
docker-compose build
docker-compose up
```

```python
ELASTIC_APM = {
   'SERVICE_NAME': 'pycon2019',
   'DEBUG': True,
   'SERVER_URL': '<apm-server-url-from-elastic-cloud>',
   'SECRET_TOKEN': '<secret-token-from-elastic-cloud>'
}
```

#### Creating our `models.py`

Movies dataset with the following structure:

```python
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
```


Create the database migrations:
```
docker exec -it djangoapp python manage.py makemigrations myproject
```

Apply the migrations:
```
docker exec -it djangoapp python manage.py migrate
```

Load the database dump:
```
docker exec -it djangoapp python manage.py loaddata db.json
```

Access the admin interface at http://localhost:8000/admin
```
username: admin
password: admin
```