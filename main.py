from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
	return {"message": "Hello from The Festiva Project Task Tracker."}
