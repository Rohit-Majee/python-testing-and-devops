# 🚀 Task Manager API - DevOps & Testing Workshop

A lightweight, fully functional RESTful API built with **Python** and **Flask**, designed as a hands-on project for learning **Fullstack Testing** and **DevOps practices**.

This repository demonstrates modern software engineering workflows, including:

- Unit & integration testing with **pytest**
- Continuous Integration (CI) using **GitHub Actions**
- Containerization with **Docker**

---

## ✨ Features

- 🔹 **RESTful API** – Full CRUD operations (Create, Read, Update, Delete)
- 🔹 **Input Validation** – Custom validation logic for data integrity
- 🔹 **Automated Testing** – Unit & integration tests with coverage reports
- 🔹 **Flexible Package Management** – Supports both `uv` and `pip`
- 🔹 **CI/CD Pipeline** – Automated testing & Docker builds via GitHub Actions
- 🔹 **Containerized** – Ready-to-deploy with Docker

---

## 📋 Prerequisites

Ensure you have the following installed:

- Python 3.10+
- Docker Desktop
- Git
- _(Optional but recommended)_ `uv` (for faster dependency management)

---

## 🛠️ Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/task-manager-workshop.git
cd task-manager-workshop
```

---

### 2. Setup Virtual Environment & Install Dependencies

You can use either **uv (recommended)** or standard **pip**.

#### ⚡ Option A: Using `uv` (Recommended)

```bash
# Create virtual environment
uv venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```

💡 Tip:

```bash
uv run python app.py
```

---

#### 🐍 Option B: Using `pip` and `venv`

```bash
# Create virtual environment
python -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Upgrade pip & install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
python app.py
```

📍 API will be available at:
http://127.0.0.1:5000

---

## 📡 API Endpoints

| Method | Endpoint    | Description            | Request Body                                 |
| ------ | ----------- | ---------------------- | -------------------------------------------- |
| GET    | /tasks      | Retrieve all tasks     | None                                         |
| POST   | /tasks      | Create a new task      | {"title": "string", "description": "string"} |
| GET    | /tasks/<id> | Retrieve specific task | None                                         |
| PUT    | /tasks/<id> | Update a task          | {"title": "string", "done": boolean}         |
| DELETE | /tasks/<id> | Delete a task          | None                                         |

---

## 🧪 Running Tests

```bash
pytest --cov=. --cov-report=term-missing
```

✔ Runs:

- Unit tests → tests/test_utils.py
- Integration tests → tests/test_app.py

---

## 🐳 Docker Containerization

### 1. Build Docker Image

```bash
docker build -t task-manager-api .
```

### 2. Run Container

```bash
docker run -p 5000:5000 task-manager-api
```

📍 Access API at:
http://localhost:5000

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

Workflow file:
.github/workflows/ci.yml

### 🔄 Pipeline Steps

- Checkout repository
- Setup Python 3.10
- Install dependencies
- Run pytest with coverage
- (On push to main) Build & push Docker image

---

## 📦 Tech Stack

- **Backend:** Flask (Python)
- **Testing:** pytest
- **CI/CD:** GitHub Actions
- **Containerization:** Docker

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests. Suggestions and improvements are always welcome!

---

## 📄 License

This project is for educational purposes. Add a license if needed.

---

## ⭐ Support

If you found this helpful, consider giving it a star ⭐
