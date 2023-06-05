FROM python:3.9-slim

RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

RUN apt-get update && apt-get install -y nodejs
RUN npm install -g @vue/cli

RUN mkdir /code
WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY client/. ./client/

WORKDIR /code/client
RUN npm install

RUN npm run build

WORKDIR /code

COPY server/. ./server/

WORKDIR /code/server

EXPOSE 5000

CMD python run.py