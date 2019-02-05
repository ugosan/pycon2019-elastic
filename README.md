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

aaa
```
