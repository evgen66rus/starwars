FROM python:3.8

RUN mkdir -p /var/ubuntu/starwars/
ENV DockerHOME=/var/ubuntu/starwars/
WORKDIR $DockerHOME
RUN apt-get update -y && apt-get install -y python3-pip python3-dev stress
RUN rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip3 install --upgrade pip
RUN pip3 install django
RUN pip3 install uwsgi
RUN pip3 install requests
RUN pip3 install psycopg2-binary
RUN pip3 install python-dotenv
WORKDIR $DockerHOME

COPY ./starwars.ini /etc/uwsgi/sites/starwars.ini
COPY . /var/ubuntu/starwars/

RUN mkdir /var/log/uwsgi
RUN touch /var/log/uwsgi/starwars.log
RUN chmod 755 /var/log/uwsgi/starwars.log

RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py makemigrations --noinput
#RUN python3 manage.py migrate --noinput
EXPOSE 8000

CMD uwsgi /etc/uwsgi/sites/starwars.ini
