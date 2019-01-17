NAME=ping-pong
NAMESPACE=ping-pong

echo Deleting $NAME
helm delete $NAME --purge --tls

echo Deploying $NAME
helm install --name $NAME ./helm/ping-pong --namespace $NAMESPACE --tls  

#--dry-run --debug