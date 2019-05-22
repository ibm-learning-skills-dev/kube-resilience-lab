echo Deleting ping  Pod
kubectl delete pod -l app=ping-player --grace-period=0 --force
