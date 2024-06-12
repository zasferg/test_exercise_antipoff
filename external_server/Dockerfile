
FROM python:3.11-alpine3.19

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /server_app

COPY server_app /server_app
COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt

EXPOSE 8001