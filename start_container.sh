#!/bin/bash
app="personality.bfi"
docker build -t ${app} .
docker run --name=${app} --rm -d -p 5001:5001 \
    --env-file=.env \
    ${app}
