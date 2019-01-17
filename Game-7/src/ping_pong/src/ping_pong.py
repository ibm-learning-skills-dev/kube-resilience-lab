import pp_queue
import sys
import message
import os
import time
import redis
import socket

CACHE='ping-pong-redis-ha-master-svc.ping-pong.svc.cluster.local'
#CACHE='localhost'


queue_name = os.environ['QUEUE_NAME']
other_queue = os.environ['OTHER_QUEUE_NAME']

welcome_message = "==> I'm " +queue_name + " in v4/Game-7"
 
red = 0

def getPodName ():
	return socket.gethostname()

key = getPodName()

def throw_ball(ball):
	message.send ("Deleting key " + key)
	red.delete(key)

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

def checkCache():
	value = red.get(key)
	if value is None:
		print ("Nothing in the cache %s" % key)
		message.send ("Nothing found in the cache")
	else:
		# Cleans the cache
		print ("Found a ball %r " % value)
		message.send ("Found a ball %r " % value)

		ball = transformBall(value)

		throw_ball(ball)

def callback(ch, method, properties, body):
	print ("Received a message %s" % body)
	message.send ("I received a %s ball" % body)

	# Store in cache
	message.send ("Storing key " + key)
	sys.stdout.flush ()
	red.set(key, body)

	# Sleep a second
	time.sleep(1)

	# Throw the ball
	# throw_ball(ball)
	checkCache()

def initCache():
	print ("Initializing cache")
	global red
#	red = redis.StrictRedis(host=CACHE, password='ping_pong')
	red = redis.StrictRedis(host=CACHE)

print(welcome_message)

# Init message
message.init ()

message.send (welcome_message)

# Init other queue
connection = pp_queue.connect()
channel = connection.channel()
channel.queue_declare(queue=other_queue)

# Init cache
initCache()

# Check cache
checkCache()

# Init queue
pp_queue.consume(queue_name, callback)

