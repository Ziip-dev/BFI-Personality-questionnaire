#!/bin/bash
app="bfi"

# build latest image version
docker build --pull --rm -t ${app} "."

# run container
docker run --name=${app} --rm -d -p 80:5001 \
    --env-file=.env \
    ${app}
