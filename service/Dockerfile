FROM python:3.11-alpine3.19

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /temp/requirements.txt
COPY app /app
WORKDIR /app
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password myuser

RUN chown -R myuser:myuser /app
USER myuser











