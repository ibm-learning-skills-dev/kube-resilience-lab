import pp_queue
import message
import os

QUEUE = 'ping'
DEFAULT_BALL = 'white'

ball = os.getenv('BALL', DEFAULT_BALL)

ball += '-0'

message.init ()

connection = pp_queue.connect()
channel = connection.channel()
channel.queue_declare(queue=QUEUE)

message.send ("Throwing ball " + ball)

channel.basic_publish(exchange='',
                      routing_key=QUEUE,
                      body=ball)

print("Ball thrown")
message.close()
connection.close()