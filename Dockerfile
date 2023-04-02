FROM python:3.10-slim-bullseye

# Set environment variables
ENV WORKSPACE_ROOT=/opt/colibris/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p $WORKSPACE_ROOT
WORKDIR $WORKSPACE_ROOT
COPY . .


# Install OS dependencies
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends build-essential \
    gcc \
    libgnutls28-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    libpq-dev \
    && apt-get clean

# Install Python dependencies
RUN python -m pip install --upgrade pip
RUN pip install  -r requirements.txt




