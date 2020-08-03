# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world my url is http://127.0.0.1:5055/'}

class MyHelloWorld(Resource):
    def get(self):
        return {'data': 'This is coming from my hello world.'}

api.add_resource(HelloWorld, '/')
api.add_resource(MyHelloWorld, '/test')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')