# TFL Bike Point Python Simple Website

This simple website connects to TFL API and pulls the currently available information about specific bike points in London. It has the following features:

1. Hashed + salted passwords
2. Dockerised Application
3. Storing credentials on GCP bucket.
4. Accessing the GCP bucket using a service account key which is hidden in the .gitignore file
5. Able to access the TFL api and retrieve available bike info
6. Stored docker image on Google Container Registry
7. Scripts which provision the website to be deployed on a kuberentes cluster on GCP

### File descriptions

Tfl Bikes.ipynb: notebook which produces the static/bike_points.html file which is later loaded into the main website

Dockerfile: This is the file which produces the Docker image to be run using the following commands:


requirements.txt: These are the libraries this project needs in order to run. The Dockerfile loads this modules into the container

credentials.py: file stored on GCP bucket

get_credentials.py: functios to read data from gcp bucket, hash and unhash password. This was the following command used to has the password:
get_credentials.hash_password('password')

templates/bike_point_map.html: is the front end main page of the app

templates/login: is the front end login page of the app

static/bike_points.html is a 30mb file which shows all the bike points on a london map

static/London* are the geojson locations used to generate the map in bike_points.html

app.py is the main server end file which serves up the logic for the entire app

.gitignore: to include my service account key

create-kubernetes-cluster.sh: creates and provisions a kubernetes cluster

delete-kubernetes-cluster.sh: deletes the kuberenets cluster

### To Run locally
```
docker build -t tfl_bikes . #This should be run in the root of the project, where the Dockerfile is

docker run tfl_bikes -p 5005:5005
```

### To run on Kubernetes cluster with load balancing
```
bash scripts/create-kubernetes-cluster.sh
```
Then go the external website shown as output and add port 5005 e.g 12.34.56.7:5005
