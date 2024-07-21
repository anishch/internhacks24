document.getElementById('uploadForm').onsubmit = async function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const content = await response.text();
    console.log("response received");
    document.getElementById('documentContent').innerText = content;
};

function sendMessage() {
    const userInput = document.getElementById('userInput');
    const chatbox = document.getElementById('chatbox');
    const message = userInput.value;
    if (message.trim()) {
        const userMessage = document.createElement('p');
        userMessage.textContent = `You: ${message}`;
        chatbox.appendChild(userMessage);
        userInput.value = '';
        // Add chatbot response logic here
    }
}