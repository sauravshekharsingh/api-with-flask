from flask import Flask,jsonify
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "admn": "adpy",
}

@auth.get_password
def get_pass(username):
    if username in users:
        return users.get(username)
    return None

app = Flask(__name__)

todolist=[{
	'taskid':'0',
	'title':'Go to the market',
	'time':'4 PM',
},
{
	'taskid':'1',
	'title':'Design poster',
	'time':'5 PM',
},
{
	'taskid':'2',
	'title':'Go for a walk',
	'time':'6 AM',
}
]

@app.route('/')
@auth.login_required
def index():
	return "Running the API successfully."

@app.route("/tasks",methods=['GET'])
@auth.login_required
def get():
	return jsonify({ "tasks":todolist })

@app.route("/tasks/<int:taskid>",methods=['GET'])
@auth.login_required
def get_task(taskid):
	return jsonify({ "tasks":todolist[taskid] })

@app.route("/tasks",methods=['POST'])
@auth.login_required
def create():
	task = {'taskid':'3',
			'title':'Brush',
			'time':'8AM'}
	todolist.append(task)
	return jsonify({ "Created":task })

@app.route("/tasks/<int:taskid>",methods=['PUT'])
@auth.login_required
def task_update(taskid):
	todolist[taskid]['title'] = "Buy device"
	return jsonify({ "tasks":todolist[taskid] })

@app.route("/tasks/<int:taskid>",methods=['DELETE'])
@auth.login_required
def task_del(taskid):
	todolist.remove(todolist[taskid])
	return jsonify({ "result":True })

if __name__ == "__main__":
	app.run(debug=True)
