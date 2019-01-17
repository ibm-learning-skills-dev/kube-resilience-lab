export IMAGE=ping_pong_throw_ball:latest
export IMAGE_PATH=patrocinio/$IMAGE

cd src/throw_ball

cp -r ../common .

docker build -t $IMAGE_PATH .
# docker login 
docker push $IMAGE_PATH

rm -rf common
