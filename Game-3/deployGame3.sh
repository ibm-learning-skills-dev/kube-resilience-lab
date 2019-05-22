NAME=ping-player
NAMESPACE=ping-pong

HELM_OPTIONS=--tls
#HELM_OPTIONS=

echo Deleting $NAME
helm delete $NAME --purge $HELM_OPTIONS

echo Deploying $NAME
helm install --name $NAME ./helm/ping-player --namespace $NAMESPACE $HELM_OPTIONS
