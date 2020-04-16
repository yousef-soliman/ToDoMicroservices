from django.http import HttpResponse
from confluent_kafka import Producer

import socket
import logging
logger = logging.getLogger(__name__)
def acked(err, msg):
    if err is not None:
        logger.info("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        logger.info("Message produced: %s" % (str(msg)))

def index(request):

    conf = {'bootstrap.servers': "kafka:9092",
        'client.id': socket.gethostname()}
    producer = Producer(conf)
    logger.info(" %s" % (str(producer)))
    message = producer.produce("test", key="key", value="value", callback=acked)
    producer.flush()
    return HttpResponse("Hello, world. You're at the polls " +
                        str(message))

