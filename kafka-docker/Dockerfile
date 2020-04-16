FROM openjdk:8u252-jre

COPY . /app

WORKDIR /app

RUN ls

CMD ["/app/bin/kafka-server-start.sh", "/app/config/server.properties"]
