from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data as an in-memory database
tasks = [
    {"id": 1, "title": "Task 1", "done": False},
    {"id": 2, "title": "Task 2", "done": False},
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"task": task})

@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {"id": len(tasks) + 1, "title": request.json['title'], "done": False}
    tasks.append(new_task)
    return jsonify({"message": "Task created", "task": new_task}), 201

if __name__ == '__main__':
    app.run(debug=True)