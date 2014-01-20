"""
Manage state data

"""
from .tasks import Task
from .pomodoros import Pomodoro

class StateManager(object):
    """Task and Pomodoro state manager"""

    def __init__(self):
        self.pomodoros = []
        self.tasks = []

    def add_task(self, name, description=None):
        """Add a new task to the list"""
        self.tasks.append(Task(name, description=description))

    def remove_task(self, index):
        """Remove a task from the list by index"""
        self.tasks.pop(index)

    def start_pomodoro(self, task_index=0):
        """Start a new pomodoro for a task"""
        pomo = Pomodoro(self.tasks[task_index])
        pomo.start()

    def stop_pomodoro(self):
        """Finish a pomodoro"""
