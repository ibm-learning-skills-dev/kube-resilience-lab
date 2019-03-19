NAME=ping-pong
NAMESPACE=ping-pong
HELM_OPTIONS=--tls

echo Deleting $NAME
helm delete $NAME --purge $HELM_OPTIONS
