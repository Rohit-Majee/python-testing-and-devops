# Task Manager API - DevOps & Testing Workshop

A lightweight, fully functional RESTful API built with **Python** and **Flask**, designed as a hands-on project for learning Fullstack Testing and DevOps practices. 

This repository demonstrates modern software engineering workflows, including unit and integration testing with **pytest**, continuous integration (CI) using **GitHub Actions**, and containerization with **Docker**.

## Features

- **RESTful API:** Full CRUD operations (Create, Read, Update, Delete) for managing tasks.
- **Input Validation:** Custom validation logic ensuring data integrity.
- **Automated Testing:** Comprehensive unit and integration tests using `pytest` with coverage reporting.
- **Modern Package Management:** Fast, reliable environment setup using `uv`.
- **CI/CD Pipeline:** Automated testing and Docker image builds via GitHub Actions.
- **Containerized:** Ready-to-deploy `Dockerfile` for seamless deployment.

---

## Prerequisites

Make sure you have the following installed on your local machine:
- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/) (Extremely fast Python package installer and resolver)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Git

---

## Local Development Setup

We use `uv` for blazing-fast virtual environment management and dependency installation.

**1. Clone the repository**
```bash
git clone [https://github.com/your-org/task-manager-workshop.git](https://github.com/your-org/task-manager-workshop.git)
cd task-manager-workshop


# Create the environment
uv venv

# Activate it (macOS/Linux)
source .venv/bin/activate
# Activate it (Windows)
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt