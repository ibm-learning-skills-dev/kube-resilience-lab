NAME=ping-pong
NAMESPACE=ping-pong

echo Deleting $NAME
helm delete $NAME --purge --tls

