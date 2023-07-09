FROM nginx

COPY ./nginx.conf ./etc/nginx/nginx.conf

COPY ./app ./etc/nginx/app

CMD [ "nginx", "-g", "daemon off;" ]