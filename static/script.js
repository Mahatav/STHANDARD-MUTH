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

// Handle sending messages
chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const userInput = chatInput.value.trim();

    if (userInput === '') return;

    // Add user's message to the chat
    addMessage('user', userInput);

    // Simulate bot response
    setTimeout(() => {
        const botResponse = generateBotResponse(userInput);
        addMessage('bot', botResponse);
    }, 1000);

    chatInput.value = '';
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
}

// Function to generate a bot response (placeholder logic)
function generateBotResponse(userInput) {
    const responses = [
        "I'm here to help!",
        "That sounds interesting!",
        "Can you tell me more?",
        "I'm not sure about that, but I'll try my best!",
    ];

    return responses[Math.floor(Math.random() * responses.length)];
}
 