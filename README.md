# twitter-stats

Project contents

Tfl Bikes.ipynb: notebook which produces the static/bike_points.html file which is later loaded into the main website


Dockerfile: This is the file which produces the Docker image to be run using the following commands:

docker build -t tfl_bikes .

Then to run the image as a container:

docker run tfl_bikes -p 5005:5005


requirements.txt: These are the libraries this project needs in order to run. The Dockerfile loads this modules into the container

credentials.py: is where the credentials are called from

templates/bike_point_map.html: is the front end main page of the app

templates/login: is the front end login page of the app

static/bike_points.html is a 30mb file which shows all the bike points on a london map

static/London* are the geojson locations used to generate the map in bike_points.html

app.py is the main server end file which serves up the logic for the entire app

.gitignore: to include my service account key