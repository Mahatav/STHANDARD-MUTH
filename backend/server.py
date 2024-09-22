from flask import Flask, request, jsonify
from chatBot import chatBot

app = Flask(__name__)
ai = chatBot()

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    ai_response = ai.generate_response(user_message)
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)