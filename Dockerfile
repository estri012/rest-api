FROM python:3.7
#set workdir
WORKDIR /usr/src/gmlews
#set env
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
#install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/gmlews/requirements.txt
RUN pip install -r requirements.txt
#copy project
COPY . /usr/src/gmlews



