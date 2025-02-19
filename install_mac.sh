#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 not found. Installing..."
    brew install python3
fi

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install the package
pip install -e .

# Create application bundle
python3 create_mac_app.py

# Create desktop shortcut
ln -s "/Applications/ThesisManager.app" ~/Desktop/

echo "Installation complete! You can now run Thesis Manager from:"
echo "1. Applications folder"
echo "2. Desktop shortcut"
echo "3. Spotlight (Command + Space, then type 'Thesis Manager')" 