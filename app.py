from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return "📝 Simple To-Do App is running!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    if task:
        tasks.append(task)
        return jsonify({"message": "Task added!", "tasks": tasks}), 201
    return jsonify({"error": "No task provided"}), 400

@app.route('/delete', methods=['POST'])
def delete_task():
    data = request.get_json()
    task = data.get('task')
    if task in tasks:
        tasks.remove(task)
        return jsonify({"message": "Task deleted!", "tasks": tasks})
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
