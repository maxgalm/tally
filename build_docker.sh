#!/usr/bin/env bash

set -e

BASE_FOLDER="$( dirname "${0}" )"

USER=${USER:-$(whoami)}

DOCKER_BUILDKIT=1 docker build \
    --progress=plain \
    --build-arg USERNAME=${USER} \
    --tag tally-devenv:latest \
    -f .devcontainer/Dockerfile \
    ${BASE_FOLDER}/.devcontainer