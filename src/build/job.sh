sudo docker build -t job_service ../job_service
sudo docker run --env-file ../.env -it job_service
