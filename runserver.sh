#!/usr/bin/env bash

docker run --rm -ti -v $(pwd)/src:/src -p 5000:5000 --env-file ./src/.env $1