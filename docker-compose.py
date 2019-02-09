version: "2.2"
services:
  djangoapp:
    container_name: djangoapp
    build: ./pycon2019-app
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./pycon2019-app/myproject:/myproject
      - ./pycon2019-app/movies-dataset:/movies-dataset
    ports:
      - "8000:8000"
    environment:
      SERVER_URL: changeme
      SECRET_TOKEN: changeme
      SERVICE_NAME: pycon2019