FROM alpine
RUN apk add --no-cache curl wget busybox-extras netcat-openbsd python py-pip && \
    pip install awscli
RUN apk --purge -v del py-pip
RUN apk add apache2
RUN apk add openrc --no-cache
RUN apk add tree
CMD tree /var
RUN rc-update add apache2
RUN echo 'Hello World from Docker!' > /var/www/html/index.html
EXPOSE 80
CMD tail -f /dev/null
