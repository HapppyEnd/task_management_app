from app import app, db
from app.models import User, Task
from flask import request, jsonify
from flask_jwt_extended import (create_access_token, jwt_required,
                                get_jwt_identity)
from werkzeug.security import generate_password_hash, check_password_hash

from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data.get('username'), password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    if not user or not check_password_hash(user.password,
                                           data.get('password')):
        return jsonify({'message': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200


@app.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    current_user = get_jwt_identity()
    tasks = Task.query.filter_by(owner_id=current_user).all()
    return jsonify([task.todict() for task in tasks])


@app.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    new_task = Task(title=data.get('title'),
                    description=data.get('description'),
                    owner=data.get('owner'), status=data.get('status'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.todict()), 201


@app.route('/tasks/<int:id>', methods=['GET'])
@jwt_required()
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.todict())


@app.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
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
@jwt_required()
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204
