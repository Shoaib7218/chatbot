from flask import Flask, render_template, request, jsonify
from src.chatbot import load_classifier
from src.chatbot import get_response

app = Flask(__name__)

classifier = load_classifier()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def respond():
    user_input = request.json.get('message')
    response = get_response(user_input, classifier)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
