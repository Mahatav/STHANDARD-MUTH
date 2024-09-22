from flask import Flask, request, jsonify, render_template
from backend.chatBot import chatBot

app = Flask(__name__)
ai = chatBot()

@app.route('/')
def home():
    # Render index.html from the templates directory
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    ai_response = ai.generate_response(user_message)
    return jsonify({'response': ai_response})

@app.route('/api/get_context', methods=['POST'])
def get_context():
    last_name = request.json['lastName']
    context_summary = ai.get_context(last_name)
    return jsonify({'response': context_summary})

if __name__ == '__main__':
    app.run(debug=True)
