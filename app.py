from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

@app.route('/')
def home():
    return jsonify({"message": "update live!", "status": "running"})

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({"todos": todos, "count": len(todos)})

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({"error": "Please provide a task"}), 400
    todo = {"id": len(todos) + 1, "task": data['task'], "done": False}
    todos.append(todo)
    return jsonify({"message": "Task added!", "todo": todo}), 201

@app.route('/health')
def health():
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)