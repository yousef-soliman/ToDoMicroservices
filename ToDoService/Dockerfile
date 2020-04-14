FROM golang:latest


RUN go mod download 

RUN mkdir -p /app

WORKDIR /app

ADD . /app

# RUN go build ./app.go

CMD ["gin", "run", "app.go"]
