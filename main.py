from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In memory storage (we'll replace this with a database later)
tasks_db = []

# Task model -- defines what a task looks like
class Task(BaseModel):
	id: int
	title: str
	description: str = ""
	status: str = "todo"

# WELCOME ENDPOINT
@app.get("/")
def root():
	return {"message": "Hello from the Festiva Project Tracker!"}

# GET /tasks -- list all tasks
@app.get("/tasks")
def list_tasks():
	return {"tasks": tasks_db}

# POST /tasks -- add a new task
@app.post("/tasks")
def create_task(task: Task):
	# Check if a task with this ID already exists
	for existing_task in tasks_db:
		if existing_task.id == task.id:
			return {"error": f"Task with id {task.id} already exists"}
	tasks_db.append(task)
	return {"message": "Task created", "task": task}

# PUT /tasks -- update an existing task
@app.put("/taks/{task_di}")
def update_task(task_id: int, updated_task: Task):
	for i, task in enumerate(tasks_db):
		if task.id == task_id:
			tasks_db[i] = updated_task
			return {"message": "Task updated", "task": updated_task}
	return {"error": "Task not found"}

