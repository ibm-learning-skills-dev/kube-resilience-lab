import pp_queue
import sys
import message
import os
import time
import socket


queue_name = os.environ['QUEUE_NAME']
other_queue = os.environ['OTHER_QUEUE_NAME']

welcome_message = "==> I'm " +queue_name + " in v2/Game-8"

def getPodName ():
	return socket.gethostname()

key = getPodName()

def throw_ball(ball):
	message.send ("==> Throwing ball %s" % ball)

	channel.basic_publish(exchange='',
    	                  routing_key=other_queue,
        	              body=ball)
def transformBall(body):
	ball = body.decode('utf-8')
	name, count = ball.split("-", 1)
	count = int(count)
	count += 1
	return name + "-" + str(count)

def processBall(value):
	print ("Found a ball %r " % value)
	message.send ("Found a ball %r " % value)

	ball = transformBall(value)

	throw_ball(ball)

def callback(ch, method, properties, body):
	print ("Received a message %s" % body)
	sys.stdout.flush ()
	message.send ("I received a %s ball" % body)

	# Sleep a second
	time.sleep(1)

	# Throw the ball
	# throw_ball(ball)
	processBall(body)

	# Ack the message
	print ("Ack'ing the message")
	ch.basic_ack(delivery_tag=method.delivery_tag)

print(welcome_message)

# Init message
message.init ()

message.send (welcome_message)

# Init other queue
connection = pp_queue.connect()
channel = connection.channel()
channel.queue_declare(queue=other_queue)

# Init queue
pp_queue.consume(queue_name, callback)

