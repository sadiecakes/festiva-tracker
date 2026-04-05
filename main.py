from fastapi import FastAPI
app = FastAPI()

@app.get("/tasks")
def list_tasks():
	return {"tasks": []}

@app.get("/")
def root():
	return {"message": "Hello from The Festiva Project Task Tracker."}
