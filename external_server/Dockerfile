

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# COPY requirements.txt /temp/requirements.txt
# COPY server_app /server_app
# WORKDIR /server_app
# EXPOSE 8001

# RUN pip install -r /temp/requirements.txt

# RUN adduser --disabled-password myuser

# RUN chown -R myuser:myuser /server_app
# USER myuser

FROM python:3.11-alpine3.19
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /server_app
COPY server_app /server_app
COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

EXPOSE 8001