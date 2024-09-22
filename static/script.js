// Theme toggle functionality
const themeToggleBtn = document.querySelector('.theme-btn');
const body = document.body;

themeToggleBtn.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    themeToggleBtn.textContent = body.classList.contains('dark-mode') ? 'Light Mode' : 'Dark Mode';
});

// Chat functionality
const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const messagesContainer = document.getElementById('messages');

// Add instruction element
const instructionElement = document.createElement('p');
instructionElement.id = 'instruction';
instructionElement.textContent = 'Please enter a last name to begin the conversation.';
chatForm.insertBefore(instructionElement, chatInput);

// Handle sending messages
let isFirstMessage = true;

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const userInput = chatInput.value.trim();

    if (userInput === '') return;

    // Add user's message to the chat
    addMessage('user', userInput);

    // Show loading indicator
    const loadingMessage = addMessage('bot', 'Thinking...');

    // Disable input while waiting for response
    chatInput.disabled = true;

    try {
        let response;
        if (isFirstMessage) {
            // For the first message, call get_context
            response = await fetch('/api/get_context', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ lastName: userInput }),
            });
            isFirstMessage = false;
            instructionElement.textContent = 'Now you can chat freely!';
        } else {
            // For subsequent messages, use the regular chat API
            response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userInput }),
            });
        }

        if (!response.ok) {
            throw new Error('Failed to get AI response');
        }

        const data = await response.json();
        
        // Remove loading indicator with a slight delay
        setTimeout(() => {
            loadingMessage.remove();
        }, 500);

        // Add AI's response to the chat
        addMessage('bot', data.response);
    } catch (error) {
        console.error('Error:', error);
        // Remove loading indicator with a slight delay
        setTimeout(() => {
            loadingMessage.remove();
        }, 500);
        // Add error message to the chat
        addMessage('bot', 'Sorry, I encountered an error. Please try again.');
    }

    // Re-enable input
    chatInput.disabled = false;
    chatInput.value = '';
    chatInput.focus();
});

// Function to add message to the chat
function addMessage(sender, text) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    
    // Create message content with avatar and timestamp
    const messageContent = document.createElement('div');
    messageContent.classList.add('message-content');

    const messageText = document.createElement('span');
    messageText.classList.add('message-text');
    messageText.textContent = text;

    const timestamp = document.createElement('span');
    timestamp.classList.add('timestamp');

    // Get the current time in PST
    const options = {
        timeZone: 'America/Los_Angeles', // Pacific Time Zone
        hour: '2-digit',
        minute: '2-digit',
        hour12: false // Set to true for 12-hour format
    };
    timestamp.textContent = new Date().toLocaleTimeString([], options);

    // Append text and timestamp to message content
    messageContent.appendChild(messageText);
    messageContent.appendChild(timestamp);

    // Append avatar
    const avatar = document.createElement('div');
    avatar.classList.add('avatar', `${sender}-avatar`);
    
    messageElement.appendChild(avatar);
    messageElement.appendChild(messageContent);

    messagesContainer.appendChild(messageElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight; // Auto-scroll to bottom

    return messageElement;
}

// Function to get last name context
async function getLastNameContext(lastName) {
    try {
        const response = await fetch('/api/get_context', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ lastName: lastName }),
        });

        if (!response.ok) {
            throw new Error('Failed to get last name context');
        }

        const data = await response.json();
        return data.response;
    } catch (error) {
        console.error('Error:', error);
        return 'Sorry, I encountered an error while fetching the last name context.';
    }
}
