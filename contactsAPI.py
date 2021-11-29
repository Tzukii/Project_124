from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'Name': u'John Doe',
        'Phone Number': u'123-456-7890',
        'done': False
    },
    {
        'id': 2,
        'Name': u'Jane Doe',
        'Phone Number': u'0987-654-321',
        'done': False
    }
]


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Phone Number': request.json.get('Phone Number', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Contact added succesfully!"
    })


@app.route("/get-data")
def get_data():
    return jsonify({
        "data": tasks
    })


if (__name__ == "__main__"):
    app.run(debug=True)
