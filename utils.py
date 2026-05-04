# utils.py

def validate_task(title, description=""):
    """
    Returns (is_valid, error_message).
    A task is valid if title is non-empty and < 100 characters.
    """
    if not title or not title.strip():
        return False, "Title cannot be empty"
    if len(title) > 100:
        return False, "Title too long (max 100 characters)"
    return True, ""

def format_task_response(task):
    """Take a task dict and return a formatted string for display."""
    return f"Task: {task['title']} | Done: {task['done']}"