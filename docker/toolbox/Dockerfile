FROM alpine
RUN apk add --no-cache curl wget busybox-extras netcat-openbsd python py-pip && \
    pip install awscli
RUN apk --purge -v del py-pip
RUN apk add apache2
EXEC rc-service apache2 start
EXEC rc-update add apache2
RUN echo 'Hello World from Docker!' > /var/www/html/index.html
EXPOSE 80
CMD tail -f /dev/null
