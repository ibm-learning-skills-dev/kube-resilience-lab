echo Deleting show_cache job
kubectl delete job show-cache

echo Deploying show_cache
kubectl create -f deploy/show_cache/show_cache_job.yaml