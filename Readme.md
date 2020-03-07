# Simple Python REST api for posting to Google Cloud Message
The intention with this repository is to create an easy way to test sending data messages and notifications to Google Cloud Messenger. 

This is in use at my internal docker cluster to post messages from Node Red to an Android client I develop.

## Precaution!!
Do NOT use this on any public facing web service. This should only be used internally behind a firewall. Currently it does not support SSL/TLS traffic.

## Requirenments
- Docker
- Service account credentials downloaded as json file from Firebase admin console

## Docker info
Volumes:
    - /app/secure - must be bound to a folder where your private-api-key.json is located
    - /app/logs - when bound you can access the log file log.txt

## To run
docker build -t mkmedia/gcloud-notifier:latest .
docker run -p 5000:5000 -v ~/tmp:/app/logs -v secure:/app/secure mkmedia/gcloud-notifier:latest