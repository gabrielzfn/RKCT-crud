from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

# Utilizando uma lista no lugar de um banco de dados
tasks = []
taskid = 1


# Post:
@app.route('/tasks', methods=["POST"])
def create_task():
    global taskid
    data = request.get_json()
    new_task = Task(id=taskid, title=data['title'], description=data.get('description', ""))
    taskid += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"Message": "Nova tarefa criada."})


# Get (todos os itens da lista):
@app.route('/tasks', methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)


# Get (apenas o primeiro da lista):
@app.route('/tasks/<int:id>', methods=["GET"])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"Message": "Não foi possível encontrar a tarefa."}), 404


# Put
@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
    task = None
    for t in task:
        if t.id == id:
            task = t
    print(task)

    if task == None:
        return jsonify({"Message": "Não foi possível encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    
    return jsonify({"Message": "Tarefa atualizada com sucesso"})
 

# Delete:
@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks: 
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({"Message": "Não foi possível encontrar a atividade."}), 404
    
    tasks.remove(task)
    return jsonify({"Message": "Tarefa deletada com sucesso."})



# app.run é utilizado para iniciar, rodar a aplicação
# A propriedade debug é utilizado para mostrar as funcionalidades do servidor web (logs)
if __name__ == '__main__':
    app.run(debug=True)