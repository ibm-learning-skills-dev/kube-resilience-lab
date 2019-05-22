NAMESPACE=ping-pong

kubectl create rolebinding -n $NAMESPACE pp-rolebinding --clusterrole=privileged \
	--serviceaccount=$NAMESPACE:default