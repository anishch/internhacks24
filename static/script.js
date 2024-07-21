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

async function fetchBlobData(url) {
    const response = await fetch(url);
    const blob = await response.blob();
    const text = await blob.text();
    return text;
}

async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const chatbox = document.getElementById('chatbox');
    const message = userInput.value;
    if (message.trim()) {
        const userMessage = document.createElement('p');
        userMessage.textContent = `You: ${message}`;
        chatbox.appendChild(userMessage);
        userInput.value = '';
        
        // Fetching data from Azure Blob Storage
        const fileData = await fetchBlobData('https://sunnyyuan.blob.core.windows.net/target/Doc1.docx?sp=rw&st=2024-07-21T15:22:57Z&se=2024-07-21T23:22:57Z&spr=https&sv=2022-11-02&sr=b&sig=SZmvWkeQmHPG68gPFnzjMnkooL7DrOa6o0V3TNLgPq4%3D');
        console.log(fileData)
        // Call OpenAI API
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer sk-proj-jrHIVRjk4aUWd6FTn4DxT3BlbkFJWKufE7fBMZVSvhm12Aig`
            },
            body: JSON.stringify({
                model: 'gpt-3.5-turbo', // or the model you are using
                messages: [
                    { role: 'system', content: fileData },
                    { role: 'user', content: message }
                ]
            })
        });
        const data = await response.json();
        console.log(data)
        const aiMessage = document.createElement('p');
        aiMessage.textContent = `AI: ${data.choices[0].message.content}`;
        chatbox.appendChild(aiMessage);
    }
}
