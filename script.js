// Dark Mode Toggle
const themeToggle = document.getElementById('theme-toggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    themeToggle.innerText = document.body.classList.contains('dark') ? 'Light Mode' : 'Dark Mode';
});

// Authentication Logic
let isAuthenticated = false;

function authenticate() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    if (document.getElementById('auth-btn').innerText === 'Sign Up') {
        document.getElementById('confirm-password').classList.remove('hidden');
        if (password === confirmPassword && password !== '') {
            localStorage.setItem('userEmail', email);
            localStorage.setItem('userPassword', password);
            alert('Registration successful! Now log in.');
            document.getElementById('auth-btn').innerText = 'Login';
            document.getElementById('confirm-password').classList.add('hidden');
        } else {
            document.getElementById('error-msg').innerText = 'Passwords do not match!';
            document.getElementById('error-msg').classList.remove('hidden');
        }
    } else {
        const storedEmail = localStorage.getItem('userEmail');
        const storedPassword = localStorage.getItem('userPassword');
        if (email === storedEmail && password === storedPassword) {
            isAuthenticated = true;
            showChat();
        } else {
            document.getElementById('error-msg').innerText = 'Invalid login or password.';
            document.getElementById('error-msg').classList.remove('hidden');
        }
    }
}

// Show Chat Function
function showChat() {
    if (isAuthenticated) {
        document.getElementById('auth-section').classList.add('hidden');
        document.getElementById('chat-section').classList.remove('hidden');
    }
}

// Chat Logic
function sendMessage() {
    const input = document.getElementById('chat-input');
    const message = input.value;
    if (message.trim() !== '') {
        appendMessage('user', message);
        input.value = '';

        // Simulate Bot Response
        setTimeout(() => {
            appendMessage('bot', 'Typing...');
            setTimeout(() => {
                appendMessage('bot', 'Hello from Sthandard Muth!');
                autoScroll();
            }, 1000);
        }, 500);
    }
}

function appendMessage(sender, text) {
    const messageContainer = document.getElementById('messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.innerText = text;
    messageContainer.appendChild(messageDiv);
}

function autoScroll() {
    const messages = document.getElementById('messages');
    messages.scrollTop = messages.scrollHeight;
}
