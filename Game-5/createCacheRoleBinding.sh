NAMESPACE=ping-pong

kubectl delete rolebinding pp-cache-rolebinding

kubectl create rolebinding -n $NAMESPACE pp-cache-rolebinding --clusterrole=privileged \
	--serviceaccount=$NAMESPACE:cache-redis-ha \
	--group=[system:authenticated]
