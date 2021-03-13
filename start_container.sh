#!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run --name=${app} -d -p 80:5001 --rm \
    --env-file=.env \
    ${app}
