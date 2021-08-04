# pull official base image
FROM python:3.6-slim-buster

# set working directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
&& apt-get -y install netcat gcc \
&& apt-get clean

# Install Curl
RUN apt-get update && \
apt-get install -y --no-install-recommends curl && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
cd /usr/local/bin && \
ln -s /opt/poetry/bin/poetry && \
poetry config virtualenvs.create false


RUN pip install --upgrade pip

# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml ./app/poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=true
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY ./app /app
ENV PYTHONPATH=/app
