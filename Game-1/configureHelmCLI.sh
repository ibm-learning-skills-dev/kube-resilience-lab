MASTER_IP=wdc-master

. ~/icp.sh

echo Configuring Helm CLI for ICP on $MASTER_IP
cloudctl login -a https://$MASTER_IP:8443 -u admin -p $ICP_PASSWORD \
  --skip-ssl-validation
