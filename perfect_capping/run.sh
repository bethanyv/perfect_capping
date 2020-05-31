docker container stop $(docker container ls -aq)
docker rm $(docker ps -a -q)
# docker rmi -f $(docker images -q)
docker build -t cap:latest .
docker run -d -p 5000:5000 cap
