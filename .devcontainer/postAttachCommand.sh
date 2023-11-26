#!/usr/bin/env bash

printf "\n✨ Preparing Devcontainer... ✨\n"

set -euo pipefail

# Setup env
mkdir -p $XDG_CONFIG_HOME/direnv/
printf '[whitelist]\nprefix = [ "/workspace" ]\n' >$XDG_CONFIG_HOME/direnv/config.toml

printf "\n✨ Setup done. ✨\n"
