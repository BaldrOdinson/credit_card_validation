FROM alpine
RUN apk add --no-cache curl wget busybox-extras netcat-openbsd python py-pip && \
    pip install awscli
RUN apk --purge -v del py-pip
RUN apk add apache2
RUN exec /usr/sbin/httpd -D FOREGROUND -f /web/config/httpd.conf
RUN echo 'Hello World from Docker!' > /var/www/html/index.html
EXPOSE 80
CMD tail -f /dev/null
