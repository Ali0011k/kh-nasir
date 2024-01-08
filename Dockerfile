FROM python:3.11.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD a@123456

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt



CMD python manage.py makemigrations --noinput &&\
    python manage.py migrate --noinput &&\
    python manage.py createsuperuser --user arshia --email arshia123@gmail.com --noinput ;\
    python manage.py collectstatic --noinput&&\
    python manage.py runserver 0.0.0.0:8000
