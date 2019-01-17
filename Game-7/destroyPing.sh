POD_ID=`kubectl get pod -l app=ping | grep -v NAME | head -1 | awk '{print $1}'`


echo Deleting ping  Pod $POD_ID
kubectl delete pod $POD_ID --grace-period=0 --force

