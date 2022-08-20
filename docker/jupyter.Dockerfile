FROM jupyter/scipy-notebook

WORKDIR /home
USER root

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install fonts-firacode
