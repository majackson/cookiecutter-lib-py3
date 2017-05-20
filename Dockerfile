FROM python:3.6
ENV PYTHONUNBUFFERED 1

# install packages
RUN apt-get update
RUN apt-get install -y ntpdate

RUN mkdir /code
WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt && \
    pip install -r dev_requirements.txt

