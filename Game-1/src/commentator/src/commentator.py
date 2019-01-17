import pp_queue
import sys

MESSAGE_QUEUE = 'message'

def callback(ch, method, properties, body):
	print ("Message: %s" % body)
	sys.stdout.flush ()

print("Welcome to the Ping Pong solution")
pp_queue.consume(MESSAGE_QUEUE, callback)

