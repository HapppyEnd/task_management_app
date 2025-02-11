from app import app, db
from app.models import User, Task
from flask import request, jsonify

@app.route('/')
def index():
    return 'Hello, World!'
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.todict() for task in tasks])


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title=data.get('title'),
                    description=data.get('description'),
                    owner=data.get('owner'), status=data.get('status'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.todict()), 201

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.todict())

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get_or_404(task_id)
    task.title = data.get('title')
    task.description = data.get('description')
    task.owner = data.get('owner')
    task.status = data.get('status')
    db.session.commit()
    return jsonify(task.todict())

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204