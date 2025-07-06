
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prompt-form');
    const input = document.getElementById('prompt-input');
    const chatContainer = document.getElementById('chat-container');
    const sendButton = document.getElementById('send-button');

    // Remove the initial welcome message on first input
    input.addEventListener('focus', () => {
        const welcomeMessage = chatContainer.querySelector('.text-center');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }
    }, { once: true });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const prompt = input.value.trim();

        if (!prompt) return;

        // Disable form and show loading state
        input.disabled = true;
        sendButton.disabled = true;
        sendButton.innerHTML = '<div class="loader-sm"></div>'; // Simple spinner

        // Display user's message immediately
        addMessage(prompt, 'user');
        input.value = '';

        // Add a placeholder for Gemini's response
        const thinkingEl = addMessage('Thinking...', 'gemini', true);

        try {
            const response = await fetch('/send_prompt', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            // Update the placeholder with the actual response
            updateMessage(thinkingEl, data.response);

        } catch (error) {
            console.error('Error sending prompt:', error);
            updateMessage(thinkingEl, 'Sorry, something went wrong. Please check the console for details.');
        } finally {
            // Re-enable form
            input.disabled = false;
            sendButton.disabled = false;
            sendButton.innerHTML = 'Send';
            input.focus();
        }
    });

    function addMessage(text, sender, isThinking = false) {
        const messageWrapper = document.createElement('div');
        messageWrapper.classList.add('flex', sender === 'user' ? 'justify-end' : 'justify-start', 'mb-4');

        const messageBubble = document.createElement('div');
        messageBubble.classList.add('message-bubble', sender === 'user' ? 'user-message' : 'gemini-message');
        
        if (isThinking) {
            messageBubble.innerHTML = '<div class="flex items-center gap-2"><div class="loader-xs"></div><span>Thinking...</span></div>';
        } else {
            messageBubble.innerHTML = '<pre>' + text + '</pre>';
        }

        messageWrapper.appendChild(messageBubble);
        chatContainer.appendChild(messageWrapper);
        chatContainer.scrollTop = chatContainer.scrollHeight; // Auto-scroll to bottom

        return messageBubble; // Return the bubble to update it later if needed
    }

    function updateMessage(element, newText) {
        element.innerHTML = '<pre>' + newText + '</pre>'; // Using innerHTML to allow for formatted responses if ever needed
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
});

// Add a small loader style for the button
const style = document.createElement('style');
style.innerHTML = `
.loader-sm {
    border: 2px solid #f3f3f3;
    border-top: 2px solid #3498db;
    border-radius: 50%;
    width: 16px;
    height: 16px;
    animation: spin 1s linear infinite;
    display: inline-block;
}
.loader-xs {
    border: 2px solid #f3f3f3;
    border-top: 2px solid #3498db;
    border-radius: 50%;
    width: 12px;
    height: 12px;
    animation: spin 1s linear infinite;
    display: inline-block;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}`;
document.head.appendChild(style);
