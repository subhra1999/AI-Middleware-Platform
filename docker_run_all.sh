docker run --rm -it -d -v /etc/localtime:/etc/localtime:ro  --net=host  --name ui_manager ui_manager
docker run --rm -it -d -v /etc/localtime:/etc/localtime:ro --net=host  --name model_manager model_manager
docker run --rm -it -d -v /etc/localtime:/etc/localtime:ro --net=host  --name app_service app_service
docker run --rm -it -d -v /etc/localtime:/etc/localtime:ro --net=host  --name scheduler scheduler
docker run --rm -it -d -v /etc/localtime:/etc/localtime:ro --net=host  --name deployer deployer
docker run --rm -it -d -v /etc/localtime:/etc/localtime:ro --net=host  --name sensor_manager sensor_manager
docker run --rm -it -d -v /etc/localtime:/etc/localtime:ro --net=host  --name control_manager control_manager
docker run --rm -it -d -v /etc/localtime:/etc/localtime:ro --net=host  --name node_manager node_manager

# python3 ./node/app.py & 

# python3 ./controllers/ac_server.py 7001 &