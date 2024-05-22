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
