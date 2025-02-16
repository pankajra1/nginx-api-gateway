FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443
EXPOSE 8001 8002 8000
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]