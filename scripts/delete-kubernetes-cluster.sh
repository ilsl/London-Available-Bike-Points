#!/usr/bin/env bash
# Bash script to delete the kubernetes cluster

kubectl delete service tfl-bikes
gcloud -q container clusters delete tfl-bikes-cluster