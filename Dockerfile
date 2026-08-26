FROM nginx:alpine
RUN echo "<h1>Hello from CI/CD!</h1>" > /usr/share/nginx/html/index.html
EXPOSE 80
