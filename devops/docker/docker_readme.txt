#docker ops howto
==================

#how to build docker image from config residing in dir imgdock__miniconda
docker build -t pyalgo:basic imgdock_miniconda  #build a docker image 

docker images  # to list images
docker image ls

#to run the image
docker run -ti pyalgo:basic

this docker started ipyhon   quit() exists the container
C-p C-q  detaches from a container
docker ps  # shows current running docker containerso

docker attach $CONTAINER_ID

docker stop $CONTAINER_ID


docker image ls

docker image rm (-f) IMAGE_ID




