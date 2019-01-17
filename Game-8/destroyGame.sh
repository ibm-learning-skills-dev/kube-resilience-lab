NAME=ping-pong
NAMESPACE=ping-pong
HELM_OPTIONS=

echo Deleting $NAME
helm delete $NAME --purge $HELM_OPTIONS

