NAME=ping-pong
NAMESPACE=ping-pong

echo Upgrading $NAME
helm upgrade $NAME ./helm/ping-pong --tls 

#--dry-run --debug