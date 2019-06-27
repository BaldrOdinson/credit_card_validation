FROM alpine
RUN apk add --no-cache curl wget busybox-extras netcat-openbsd python py-pip && \
    pip install awscli
RUN apk --purge -v del py-pip
RUN apk install apache2
RUN echo 'Hello World from Docker!' > /var/www/html/index.html
CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
EXPOSE 80
CMD tail -f /dev/null
