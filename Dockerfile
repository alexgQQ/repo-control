FROM python:3.7

WORKDIR /app

RUN apt-get -yq update
RUN apt-get -yq install postgresql

RUN pip install --upgrade pip
RUN pip install pipenv
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/
