from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from chat1.chat import Bot
import nltk

nltk.download('punkt')

app = Flask(__name__)
api = Api(app)

class ChatBot(Resource):
    def post(self):
        user_input = request.json['user_input']
        response = jsonify({'bot': str(Bot(user_input))})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

api.add_resource(ChatBot, "/api/bot/")

if __name__ == '__main__':
    app.run(debug=True)
