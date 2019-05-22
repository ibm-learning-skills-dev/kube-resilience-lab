import pika
import sys
import os

PASSWORD = 'ping_pong'

#HOST = 'localhost'
PORT = 5672

channel = 0
host = os.getenv('QUEUE', 'localhost')

def connect ():
	credentials = pika.PlainCredentials('user', PASSWORD)
	parameters = pika.ConnectionParameters(host, PORT, '/', credentials)

	print ("Connecting to queue at " + host)
	connection = pika.BlockingConnection(parameters)

	return connection

def consume(queue_name, callback):
	connection = connect ()
	channel = connection.channel()
	channel.queue_declare(queue=queue_name)

# Set ack mode
	channel.basic_consume(queue_name,
        		          callback,
					      False)

	print(" [*] Waiting for messages in queue " + queue_name + ". To exit press CTRL+C")
	sys.stdout.flush ()
	channel.start_consuming()
