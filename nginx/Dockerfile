FROM nginx:stable-alpine
RUN apk add python3 python3-dev py3-pip build-base libressl-dev musl-dev libffi-dev rust cargo bash nano
RUN pip3 install pip --upgrade
RUN pip3 install certbot-nginx
RUN mkdir /etc/letsencrypt
RUN mkdir /etc/letsencrypt/live
RUN mkdir /etc/letsencrypt/live/project.com
COPY fullchain.pem /etc/letsencrypt/live/project.com/fullchain.pem
COPY privkey.pem /etc/letsencrypt/live/project.com/privkey.pem
COPY default.conf /etc/nginx/conf.d/default.conf
