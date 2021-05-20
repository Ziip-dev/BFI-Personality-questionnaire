#!/bin/bash
app="personality.bfi"
docker build -t ${app} .
docker run --name=${app} --rm -d -p 80:5001 \
    --env-file=.env \
    ${app}
