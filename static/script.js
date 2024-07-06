document.addEventListener('DOMContentLoaded', function() {
    const chatInput = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    const chatLog = document.getElementById('chat-log');

    sendBtn.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const userMessage = chatInput.value;
        if (userMessage.trim() === '') return;

        const userMessageDiv = document.createElement('div');
        userMessageDiv.textContent = 'You: ' + userMessage;
        chatLog.appendChild(userMessageDiv);

        chatInput.value = '';

        fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            const botMessageDiv = document.createElement('div');
            botMessageDiv.textContent = 'Bot: ' + data.response;
            chatLog.appendChild(botMessageDiv);
            chatLog.scrollTop = chatLog.scrollHeight;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
