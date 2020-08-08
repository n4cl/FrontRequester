FROM ubuntu:18.04

ENV TZ Asia/Tokyo
RUN apt-get update && apt-get -yq install curl net-tools nginx supervisor

ADD ./app/front_supervisor.conf /etc/supervisor/conf.d/front_daemons.conf

#ADD ./app/front_nginx.conf /etc/nginx/sites-available/front_nginx.conf
#RUN ln -s /etc/nginx/sites-available/front_nginx.conf /etc/nginx/sites-enabled/front_nginx.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
