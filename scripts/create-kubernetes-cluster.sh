#!/usr/bin/env bash
# Bash script to set the correct gcloud project if, create a kubernetes cluster with 2 nodes

export PROJECT_ID="$(gcloud config get-value project -q)"
gcloud config set project isobel-test
gcloud container clusters create tfl-bikes-cluster --num-nodes=2
kubectl run tfl-bikes --image=gcr.io/${PROJECT_ID}/tfl_bikes:v1 --port 5005
kubectl expose deployment tfl-bikes --type=LoadBalancer --port 5005 --target-port 5005
kubectl scale deployment tfl-bikes --replicas=2

OUTPUT="$(kubectl get service)"
# OUTPUT contains the external ip address of the website that we need to connect to
echo "${OUTPUT}"



