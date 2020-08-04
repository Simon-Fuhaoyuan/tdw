#!/bin/bash

# Check if your Docker image matches your installed TDW version.
# If not, pull the correct image.

TDW_VERSION=$(./tdw_version.sh)
DOCKER_TAG=$(./docker_tag.sh)

if [ $TDW_VERSION == $DOCKER_TAG ]
  then
    echo "No Docker image found that matches TDW v${TDW_VERSION}. Trying to pull now..."
    docker pull tdw:$TDW_VERSION
fi
