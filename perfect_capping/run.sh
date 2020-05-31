docker container stop $(docker container ls -aq)
docker rm $(docker ps -a -q)
docker build -t flask-sample:latest .
docker run -d -p 6021:6021 flask-sample
