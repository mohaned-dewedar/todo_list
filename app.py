from flask import Flask , render_template
import json
import os

app = Flask(__name__)

def load_tasks():
    with open("data/tasks.json",'r') as f:
        tasks = json.load(f)
        return tasks
def save_tasks(tasks):
    with open("data/tasks.json",'w') as f:
        json.dump(tasks ,f ,indent=4)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html',tasks=tasks)


@app.route('/add',methods= ['POST'])
def add():
    return 


if __name__ =='__main__':
    app.run()