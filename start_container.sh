#!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run -d -p 80:5000 --rm --name=${app} ${app}
