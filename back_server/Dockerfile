FROM ubuntu:18.04

ENV TZ Asia/Tokyo
RUN apt-get update && apt-get -yq install curl net-tools supervisor python3-pip
ADD ./app/back_supervisor.conf /etc/supervisor/conf.d/back_supervisor.conf

ADD ./app /app
WORKDIR /app
RUN pip3 install -r requirements.txt

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
