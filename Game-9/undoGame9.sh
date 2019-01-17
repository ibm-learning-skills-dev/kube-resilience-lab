NODES=$(kubectl get no -o json | \
jq '.items[].metadata | select (.labels.role != "master") | select (.labels.proxy != "true") | .name' | \
tr -d '"' )


for n in $NODES
do
	echo Uncordoning node $n
	kubectl uncordon $n
done
