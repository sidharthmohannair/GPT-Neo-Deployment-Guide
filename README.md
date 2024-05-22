
# GPT-Neo (2.7B parameters) Deployment Guide

This project sets up GPT-Neo (2.7B parameters) on a research office server, including hardware and software requirements, environment setup, model download and run instructions, and creation of an API. It also includes a front-end using Flask for the back-end and a simple HTML/CSS/JavaScript front-end, and instructions on how to share the application locally within the office.

## Features:
- Hardware and Software Requirements: Detailed list of necessary hardware and software components.
- Environment Setup: Step-by-step guide to setting up the environment for running GPT-Neo.
- Model Download and Execution: Instructions to download and run the GPT-Neo model.
- API Creation: Development of a RESTful API using Flask to interact with the GPT-Neo model.
- Front-End Interface: Simple and user-friendly front-end built with HTML, CSS, and JavaScript.
- Local Sharing: Guidelines on how to share the application within a local network in the office.

## Hardware and Software Requirements

### Hardware Requirements:
- A server with at least 16GB of RAM.
- A GPU with at least 12GB of VRAM (e.g., NVIDIA Tesla K80, RTX 2080).
- Sufficient storage space (at least 50GB free).

### Software Requirements:
- Ubuntu 20.04 LTS (or any other compatible Linux distribution).
- Python 3.8 or later.
- Pip (Python package installer).
- Git.

## Environment Setup

1. **Update and upgrade the system:**
    ```sh
    sudo apt update && sudo apt upgrade -y
    ```

2. **Install Python and Pip:**
    ```sh
    sudo apt install python3 python3-pip -y
    ```

3. **Install Git:**
    ```sh
    sudo apt install git -y
    ```

4. **Install virtualenv:**
    ```sh
    pip3 install virtualenv
    ```

5. **Create a virtual environment:**
    ```sh
    virtualenv gpt-neo-env
    source gpt-neo-env/bin/activate
    ```

## Model Download and Run Instructions

1. **Clone the GPT-Neo repository:**
    ```sh
    git clone https://github.com/EleutherAI/gpt-neo.git
    cd gpt-neo
    ```

2. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Download the GPT-Neo model:**
    ```python
    from transformers import GPTNeoForCausalLM, GPT2Tokenizer

    model_name = "EleutherAI/gpt-neo-2.7B"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPTNeoForCausalLM.from_pretrained(model_name)
    model.save_pretrained("./model")
    tokenizer.save_pretrained("./model")
    ```

## Create an API with Flask

1. **Install Flask:**
    ```sh
    pip install Flask
    ```

2. **Create a Flask application:**

    Create a file named `app.py`:
    ```python
    from flask import Flask, request, jsonify
    from transformers import GPTNeoForCausalLM, GPT2Tokenizer

    app = Flask(__name__)

    model_name = "EleutherAI/gpt-neo-2.7B"
    tokenizer = GPT2Tokenizer.from_pretrained("./model")
    model = GPTNeoForCausalLM.from_pretrained("./model")

    @app.route('/generate', methods=['POST'])
    def generate():
        input_text = request.json.get('text', '')
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(**inputs)
        text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return jsonify({'generated_text': text})

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
    ```

## Add a Front-End

1. **Create a directory for the front-end:**
    ```sh
    mkdir -p static/js static/css templates
    ```

2. **Create `index.html` in the `templates` directory:**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GPT-Neo Application</title>
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <div class="container">
            <h1>GPT-Neo Text Generation</h1>
            <textarea id="inputText" placeholder="Enter your text here..."></textarea>
            <button onclick="generateText()">Generate</button>
            <p id="outputText"></p>
        </div>
        <script src="/static/js/script.js"></script>
    </body>
    </html>
    ```

3. **Create `style.css` in the `static/css` directory:**
    ```css
    body {
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f0f0f0;
    }
    .container {
        text-align: center;
    }
    textarea {
        width: 100%;
        height: 100px;
        margin-bottom: 20px;
    }
    button {
        padding: 10px 20px;
        font-size: 16px;
    }
    ```

4. **Create `script.js` in the `static/js` directory:**
    ```javascript
    async function generateText() {
        const inputText = document.getElementById('inputText').value;
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: inputText }),
        });
        const data = await response.json();
        document.getElementById('outputText').innerText = data.generated_text;
    }
    ```

## Share the Application Locally

1. **Run the Flask application:**
    ```sh
    python app.py
    ```

2. **Access the application from other devices in the office:**
    - Ensure that the server’s IP address is accessible within the local network.
    - Colleagues can access the application by navigating to `http://<server-ip>:5000` in their web browsers.

## Final Description

If everything is set up correctly, the final result will be a functional application where users can input text and generate responses using the GPT-Neo model. The application will have the following features:

1. **User Interface**:
    - A web page with a clean and simple design where users can enter text.
    - A button to submit the text for generation.
    - A section to display the generated text.

2. **Functionality**:
    - When a user enters text and clicks the "Generate" button, the application sends the text to the backend API.
    - The backend API processes the text using the GPT-Neo model and returns the generated text.
    - The generated text is displayed on the web page.

3. **Local Access**:
    - The application is accessible within the local network, allowing colleagues to use the GPT-Neo model from their devices by navigating to the server's IP address.

### References:
- [EleutherAI GPT-Neo GitHub Repository](https://github.com/EleutherAI/gpt-neo)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
