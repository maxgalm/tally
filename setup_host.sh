#!/bin/bash

# Install the Remote - Containers extension for VSCode

# Check if Visual Studio Code is installed
if ! command -v code &> /dev/null; then
  echo "Visual Studio Code is not installed. Please install it first."
  exit 1
fi

# Install the Remote - Containers extension
if ! command -v code --install-extension ms-vscode-remote.remote-containers &> /dev/null; then
  echo "Installation of Visual Studio Code Dev Containers extension failed!"
  exit 1
fi

echo "Setup of host system was successful." 
