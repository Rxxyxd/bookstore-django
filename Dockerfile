# Pull base image
FROM python:3.9.13-slim-bullseye

# Set enviroment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBITECODE 1
ENV PYTHONUNBUFFERED 1

# Set Work Directory
WORKDIR /bookstore

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .