FROM python:3

COPY ./myproject /myproject

WORKDIR /myproject

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "manage.py", "runserver" ] 
