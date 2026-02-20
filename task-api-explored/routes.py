"""API Routes for Task Management (exercise variant)."""
from flask import jsonify, request, session
from app import app
from models import TaskStore

tasks = TaskStore()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    user_id = session.get('user_id', 'anonymous')
    return jsonify(tasks.get_by_user(user_id))

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    user_id = session.get('user_id', 'anonymous')
    task = tasks.create(user_id, data.get('title'), data.get('description'))
    return jsonify(task), 201

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks.delete(task_id)
    return '', 204
