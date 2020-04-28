FROM python:3.6-slim
ADD . /srv/root/
WORKDIR /srv/root

RUN apt update && apt install -y python3-dev && \
    apt install -y curl && \ 
    pip install -r requirements.txt
WORKDIR /srv/root/src
