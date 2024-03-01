# syntax=docker/dockerfile:1
# Machine Translation × Feature Engineering
# https://www.graphviz.org/download/

FROM ubuntu:latest

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# RUN pip install -r requirements.txt

CMD ["python3", "--version"]
