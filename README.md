# Project Tracker

A personal task management API built with FastAPI, following 12-factor methodology. Originally created to track the fEstiVa Kombi Instrument Project, now a standalone tool for managing any project.

## 🚀 Features

- Full CRUD operations (Create, Read, Update, Delete)
- SQLite database persistence
- Task categories (research, drivetrain, electronics, etc.)
- Docker support
- Interactive API documentation (FastAPI auto-generated)

## 🛠️ Tech Stack

- FastAPI (Python)
- SQLite with SQLAlchemy
- Pydantic for data validation
- Docker for containerization
- Git for version control

## 📚 Learning Outcomes

This project demonstrates:
- 12-factor methodology (config via environment variables, stateless processes, etc.)
- REST API design
- Database integration with ORM
- Containerization with Docker
- Git best practices (small commits, clear messages)

## 🚀 Quick Start

```bash
git clone https://github.com/sadiecakes/project-tracker.git
cd project-tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit `http://localhost:8000/` to access the app.
Visit `http://localhost:8000/docs` to interact with the API.

## 📄 License

This project is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html). This means you can use, modify, and distribute this code freely, and that if you distribute modified versions, you must also make your source code available under GPL v3.

## 👤 Author

Mercedes Levinson-Mader (sadiecakes) — [GitHub](https://github.com/sadiecakes)
