from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# Utilizando uma lista no lugar de um banco de dados
task = []
taskid = 1


# Create:
@app.route('/tasks', methods=['POST'])
def create_task():
    global taskid
    data = request.get_json()
    new_task = Task(id=taskid, title=data['title'], description=data.get('description', ""))
    taskid += 1
    task.append(new_task)
    return jsonify({"Message": "Nova tarefa criada."})


# Get (todos):
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in Task]
    output = {
        "tasks": task_list,
        "total": len(task_list)
    }
    return jsonify(output)


# Get (apenas o primeiro):
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in task:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"Message": "Não foi possível encontrar a tarefa."}), 404



# app.run é utilizado para iniciar, rodar a aplicação
# A propriedade debug é utilizado para mostrar as funcionalidades do servidor web (logs)
if __name__ == '__main__':
    app.run(debug=True)