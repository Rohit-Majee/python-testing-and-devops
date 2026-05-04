# Task Manager API - DevOps & Testing Workshop

A lightweight, fully functional RESTful API built with **Python** and **Flask**, designed as a hands-on project for learning Fullstack Testing and DevOps practices.

This repository demonstrates modern software engineering workflows, including unit and integration testing with **pytest**, continuous integration (CI) using **GitHub Actions**, and containerization with **Docker**.

## Features

- **RESTful API:** Full CRUD operations (Create, Read, Update, Delete) for managing tasks.
- **Input Validation:** Custom validation logic ensuring data integrity.
- **Automated Testing:** Comprehensive unit and integration tests using `pytest` with coverage reporting.
- **Flexible Package Management:** Setup instructions provided for both `uv` (ultra-fast) and standard Python `pip`.
- **CI/CD Pipeline:** Automated testing and Docker image builds via GitHub Actions.
- **Containerized:** Ready-to-deploy `Dockerfile` for seamless deployment.

---

## Prerequisites

Make sure you have the following installed on your local machine:

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Git
- _(Optional but recommended)_ [uv](https://docs.astral.sh/uv/) for blazing-fast dependency management.

---

## Local Development Setup

**1. Clone the repository**

```bash
git clone [https://github.com/your-org/task-manager-workshop.git](https://github.com/your-org/task-manager-workshop.git)
cd task-manager-workshop
2. Create a virtual environment and install dependenciesYou can set up your local environment using either uv (recommended for speed) or the standard Python venv module.Option A: Using uv (Recommended)Bash# Create the environment (.venv by default)
uv venv

# Activate it (macOS/Linux)
source .venv/bin/activate
# Activate it (Windows)
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
Tip: You can also use uv run python app.py to run scripts without manually activating the environment!Option B: Using standard pip and venvBash# Create the environment named .venv
python -m venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate
# Activate it (Windows)
.venv\Scripts\activate

# Upgrade pip (best practice) and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
Running the ApplicationTo start the Flask development server:Bashpython app.py
The API will be available at http://127.0.0.1:5000.API EndpointsMethodEndpointDescriptionRequest Body (JSON)GET/tasksRetrieve all tasksNonePOST/tasksCreate a new task{"title": "string", "description": "string"}GET/tasks/<id>Retrieve a specific taskNonePUT/tasks/<id>Update an existing task{"title": "string", "done": boolean}DELETE/tasks/<id>Delete a taskNoneRunning TestsThis project uses pytest for testing. To run the test suite and view the code coverage report:Bashpytest --cov=. --cov-report=term-missing
This will execute both the unit tests (tests/test_utils.py) and integration tests (tests/test_app.py), ensuring your core logic and API endpoints function correctly.Docker ContainerizationYou can run the application entirely within Docker, ensuring it runs identically across all environments.1. Build the Docker ImageBashdocker build -t task-manager-api .
2. Run the ContainerBashdocker run -p 5000:5000 task-manager-api
The API is now accessible at http://localhost:5000.CI/CD Pipeline (GitHub Actions)This repository includes a GitHub Actions workflow (.github/workflows/ci.yml) that automatically triggers on every push or pull request to the main branch.The pipeline performs the following steps:Checks out the code.Sets up Python 3.10.Installs dependencies.Runs the full pytest suite with coverage.(Optional/On Push to Main) Builds and pushes the Docker image to Docker Hub.Note: To enable Docker Hub pushes, ensure you have added DOCKER_USERNAME and DOCKER_PASSWORD to your GitHub Repository Secrets.
```
