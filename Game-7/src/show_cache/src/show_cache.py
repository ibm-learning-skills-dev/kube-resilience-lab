import pp_queue
import sys
import message
import os
import time
import redis

CACHE='ping-pong-redis-ha-master-svc.ping-pong.svc.cluster.local'
#CACHE='localhost'

welcome_message = "==> Checking caches"

red = 0

def checkCache(key):
	print ("Checking cache %s" % key)
	value = red.get(key)
	if value is None:
		print ("Nothing in the cache")
		message.send ("Nothing found in the cache")
	else:
		# Cleans the cache
		print ("Found a ball %r " % value)
		message.send ("Found a ball %r " % value)

def initCache():
	print ("Initializing cache")
	global red
	red = redis.StrictRedis(host=CACHE)

print(welcome_message)

# Init message
message.init ()

message.send (welcome_message)

# Init cache
initCache()

# Check cache
checkCache('ping-0')
checkCache('ping-1')


