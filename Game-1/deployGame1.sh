./deployChart.sh ping-pong

echo Waiting 15 seconds
sleep 15

./deployChart.sh pong
./deployChart.sh ping-player
