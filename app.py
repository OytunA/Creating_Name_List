from flask import Flask, request, Response
from process import get_users_from_mongo, create_name_surname

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    demo_variable = 'hoşgeldiniz'
    return demo_variable

@app.route('/get-users', methods=['GET'])
def get_users():
    try:
        users = get_users_from_mongo()
        return users
    except Exception as ex:
        return Response(str(ex), 400)


@app.route('/create-user', methods=['POST'])
def create_user():
    try:
        data = request.json
        is_created = create_name_surname(data)
        return str(is_created)
    except Exception as ex:
        return Response(str(ex), 400)


app.run(host='localhost', port=5000)

