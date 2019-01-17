CID=`kubectl get po | grep commentator | grep Running | awk '{print $1}'`

kubectl logs -f $CID


