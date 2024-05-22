#!/bin/bash

# Update package list and install prerequisites
sudo apt update
sudo apt install -y python3 python3-pip

# Install Python packages
pip3 install -r requirements.txt

# Print installation completion message
echo "Installation complete. You can now run the Flask application with 'python app.py'."
