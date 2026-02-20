"""Task Data Model (exercise variant)."""
import uuid
from datetime import datetime

class TaskStore:
    def __init__(self):
        self._tasks = {}

    def create(self, user_id, title, description=None):
        task_id = str(uuid.uuid4())
        task = {
            'id': task_id,
            'user_id': user_id,
            'title': title,
            'description': description,
            'created_at': datetime.utcnow().isoformat(),
            'completed': False
        }
        self._tasks[task_id] = task
        return task

    def get_by_user(self, user_id):
        return [t for t in self._tasks.values() if t['user_id'] == user_id]

    def delete(self, task_id):
        self._tasks.pop(task_id, None)
