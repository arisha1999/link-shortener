# set base image (host OS)
FROM python:3.9-slim

# Install Node.js and Vue CLI
RUN apt-get update && apt-get install -y nodejs
RUN npm install -g @vue/cli

# set the working directory in the container
RUN mkdir /code
WORKDIR /code

# copy the server requirements file to the working directory
COPY requirements.txt .

# install server dependencies
RUN pip install -r requirements.txt

# copy the content of the client folder to the container
COPY client/. ./client/

# install client dependencies
WORKDIR /code/client
RUN npm install

# build the client application
RUN npm run build

# switch back to the working directory
WORKDIR /code

# copy the content of the server folder to the container
COPY server/. ./server/

# copy the run.py file to the container
COPY run.py .

# expose the port on which the app will run
EXPOSE 5000

# command to start the client and server
CMD python run.py