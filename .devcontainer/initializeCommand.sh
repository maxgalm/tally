#!/bin/bash

warn() {
    # print in yellow color
    echo -e "\e[93m$1\e[0m"
}

create_bind_targets() {
    touch ${HOME}/.netrc
    touch ${HOME}/.gitconfig
    touch ${HOME}/.git-credentials
    mkdir -p ~/.ssh
}

create_bind_targets || warn "Could not create bind targets in the home directory."
