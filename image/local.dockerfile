# FROM python:3.8.11-buster

# ENV PYTHONUNBUFFERED=1

# RUN apt-get update \
#     && apt-get upgrade -y \
#     && apt-get install -y \
#     --no-install-recommends \
#     curl \
#     gcc \
#     graphviz \
#     libpq-dev \
#     make \
#     postgresql-client \
#     python3-dev \
#     && apt-get autoremove -y \
#     && apt-get clean
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /code/

# COPY requirements.txt /code.txt
# RUN pip install -r  /code.txt
# COPY . /code/
# COPY requirements.txt /code/

# RUN pip install --upgrade pip

# RUN pip install -r ./requirements.txt 

# RUN mkdir /app

# WORKDIR /app

# COPY ./alocai_backend alocai_backend

# COPY ./sql/alocai.sql sql/alocai.sql

# COPY ./.env alocai_backend/.env

# WORKDIR /app/alocai_backend