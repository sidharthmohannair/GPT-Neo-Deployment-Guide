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
