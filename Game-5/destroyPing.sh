echo Deleting ping  Pod
kubectl delete pod -l app=ping --grace-period=0 --force

