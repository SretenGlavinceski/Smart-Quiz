FROM nginx:alpine

RUN apk add --no-cache curl unzip

WORKDIR /usr/share/nginx/html

# Download Bootstrap
RUN curl -L -o bootstrap.zip https://github.com/twbs/bootstrap/releases/download/v5.3.3/bootstrap-5.3.3-dist.zip && \
    unzip bootstrap.zip -d ./bootstrap && \
    rm bootstrap.zip

COPY index.html quiz.html ./

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
