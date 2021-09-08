from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from chat1.chat import Bot

app = Flask(__name__)
api = Api(app)

class ChatBot(Resource):
    def post(self):
        user_input = request.json['user_input']
        print(user_input)
        return jsonify({'bot': str(Bot(user_input))})

api.add_resource(ChatBot, "/api/bot/")

if __name__ == '__main__':
    app.run(debug=True)