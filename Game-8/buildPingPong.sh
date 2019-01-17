export IMAGE=ping_pong:Game-8
export IMAGE_PATH=patrocinio/$IMAGE

cd src/ping_pong

cp -r ../common .

docker build -t $IMAGE_PATH .
# docker login 
docker push $IMAGE_PATH

rm -rf common
