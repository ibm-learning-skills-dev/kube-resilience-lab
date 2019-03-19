NAMESPACE=ping-pong

kubectl create rolebinding -n $NAMESPACE pp-rolebinding --clusterrole=privileged \
	--serviceaccount=$NAMESPACE:default

kubectl delete psp retrict-root

kubectl create -f permit-root.yaml 
