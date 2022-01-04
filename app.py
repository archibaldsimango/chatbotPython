from flask import Flask, request, Response
from database.db import initialize_app
from database.models import Chat1

app = Flask(__name__)


# configuring mongodb
app.config['MONGO_SETTINGS'] = {
    "host": 'mongodb://localhost:27017/movies',
    "db": 'movies'
}
initialize_app(app)


# get all chat1 items
# localhost:5000/chat1
# get request
@app.route('/chat1')
def get_movies():
    chats1 = Chat1.objects().to_json()
    return Response(chats1, mimetype="application/json", status=200)


# post chat1 items
# localhost:5000/chat1
# post request
@app.route('/chat1', methods=['POST'])
def add_movies():
    body = request.get_json()
    chat = Chat1(**body).save()

    if chat:
        t_id = chat.id
        print(chat)
        return {'chat': chat}, 200
    else:
        return "nothing entered"


if __name__ == "__main__":
    app.run(port=5000, debug=True)


@app.route('/')
def hello_world():
    return 'hello world'

