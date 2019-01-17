NODE=$(kubectl get no -o json | \
jq '.items[].metadata | select (.labels.role != "master") | select (.labels.proxy != "true") | .name' | \
tr -d '"' |
head -1)

echo Draining node $NODE 
kubectl drain $NODE --force --delete-local-data
