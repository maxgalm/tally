#!/bin/bash

cd "$(dirname "$0")"
docker buildx build -f Dockerfile -t tally_devenv:2023.11.1 .