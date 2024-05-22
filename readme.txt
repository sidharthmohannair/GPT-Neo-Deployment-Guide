# GPT-Neo Deployment Guide

This guide provides instructions for deploying GPT-Neo (2.7B parameters) on a research office server, including setting up a Flask web application and using the Transformers library.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sidharthmohannair/GPT-Neo-Deployment-Guide.git
    cd GPT-Neo-Deployment-Guide
    ```

2. Run the installation script to install the required packages:
    ```sh
    ./install.sh
    ```

## Usage

1. Start the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## File Structure

- `requirements.txt`: Contains the list of dependencies.
- `install.sh`: Shell script to install dependencies.
- `app.py`: Main Flask application file.
- Additional configuration and setup files for deploying GPT-Neo.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
