export IMAGE=ping_pong_show_cache:latest
export IMAGE_PATH=patrocinio/$IMAGE

cd src/show_cache

cp -r ../common .

docker build -t $IMAGE_PATH .
# docker login 
docker push $IMAGE_PATH

rm -rf common
