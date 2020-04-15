# ToDoMicroservices

## project for training purpose

## First step

* service1
  - name: ToDoService
  - languague: Go
  - Port: 8088
  - type: REST API
  - functionality:
    - create Todo
    - update Todo
    - delete Todo
    
* service1
  - name: ToDoViewService
  - languague: Python(Django)
  - Port: 8000
  - type: REST API
  - functionality:
    - get Todo
    - list All Todos
    
 Communicate with services with [Kafka](https://kafka.apache.org/)
