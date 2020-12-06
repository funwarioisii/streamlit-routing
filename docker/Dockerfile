FROM ubuntu:20.04

ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

# setup python
RUN apt-get update && apt-get install -y \
  python3.7 \
  python3-pip \
  python3-dev
RUN pip3 install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# set nginx
RUN apt install -y nginx
COPY ./docker/nginx/nginx.conf /etc/nginx/nginx.conf

# set streamlit
WORKDIR /root/.streamlit
COPY ./docker/streamlit/config.toml ./config.toml

WORKDIR /work
COPY ./src /work/src
COPY ./docker/entrypoint.sh /work/entrypoint.sh

RUN chmod 755 entrypoint.sh
CMD ["./entrypoint.sh"]

