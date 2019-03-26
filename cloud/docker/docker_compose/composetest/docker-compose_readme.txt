https://docs.docker.com/compose/gettingstarted/


app.py is  flask webapp



Dockerfile
 # builds an image with 2 packages  in requirements.txt  flask and redis


docker-compose.yml  
#defines  2 services web and redis
# the web service
   - will use an image built from dockerfile,
   - forwards the image container port 5000 to host port 5000
# the redis image uses a public redis image pulled from docker hub registry


docker-compose up   #build and run the 2 services  in 2 docker images 

docker-compose build  (re)builds images after a change of deployed files
