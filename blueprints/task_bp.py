from flask import Blueprint, jsonify, request
from controllers import task_controller
from utils.strDateUtil import dateToStr, strToDate

app_task = Blueprint('task_bp', __name__)

@app_task.route('/tasks', methods=["GET"])
def get_tasks():
    tasks = task_controller.get_tasks()
    
    response = {'tasks': []}
    for task in tasks:
        response['tasks'].append({
            'task_id': task.task_id,
            'task_name': task.task_name,
            'task_is_done': task.task_is_done,
        })
    return jsonify(response)

@app_task.route('/post_task', methods=["POST"])
def post_task():
    data = request.get_json()
    
    try:
        task_name = data['task_name']
        task_description = data['task_description']
        task_date = data['task_date']
        task_is_termless = data['task_is_termless']
        
        new_task = task_controller.post_task(task_name, task_is_termless, strToDate(task_date), task_description)
        response = {
            'task_id': new_task.task_id,
            'task_name': new_task.task_name,
            'task_is_done': new_task.task_is_done,
            'task_is_termless': new_task.task_is_termless,
            'task_description': new_task.task_description,
            'task_date': dateToStr(new_task.task_date)
        }
        
        return jsonify(response)
    
    except KeyError:
        response = {'task_error': "Body not have a required keys 'task_name', 'task_description'"}
        return jsonify(response)