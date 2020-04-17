FROM openjdk:8u252-jre

WORKDIR /app

RUN wget https://downloads.apache.org/kafka/2.5.0/kafka_2.12-2.5.0.tgz

RUN tar -xvzf kafka_2.12-2.5.0.tgz -C /app


WORKDIR /app/kafka_2.12-2.5.0
COPY ./config ./config
RUN ls

CMD ["./bin/kafka-server-start.sh", "./config/server.properties"]
