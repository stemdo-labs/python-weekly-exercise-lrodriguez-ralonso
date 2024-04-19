FROM postgres:latest

LABEL author=Luis-rodr author_mail=lrdriguez@stemdo.io
LABEL version="0.1"

WORKDIR /

ADD ./init-database.sh /

RUN sed -i 's/\r$//' /init-database.sh  && \  
chmod +x $app/init-database.sh

ENTRYPOINT /init-database.sh

EXPOSE 5432