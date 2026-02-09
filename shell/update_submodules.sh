#!/bin/bash

# Pull and install the various git submodules
# chmod a+x shell/update_submodules.sh

echo "Pulling submodules..."
git submodule foreach git pull
echo "Submodules pulled!"
echo "Installing packages..."
pip install submodules/mmma/src
echo "Installing requirements..."
pip install -r submodules/mmma/src/requirements.txt