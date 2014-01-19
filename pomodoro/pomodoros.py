"""
Read/Write/Manage Pomodoros

"""

from datetime import datetime

class Pomodoro(object):
    """
    Describe a Pomodoro.

    Instance Variables:
        task(pomodoro.Task)
        status(str)
        start_time(datetime.datetime)
        end_time(datetime.datetime)
    """

    valid_status = ["Not Started", "In Progress", "Interrupted", "Complete"]

    def __init__(self, task, status="Not Started", start_time=None,
            end_time=None):
        """Construct a new Pomodoro."""
        self.task = task
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.validate()

    def start(self):
        """Start the Pomodoro."""
        assert self.start_time is None
        assert self.status == "Not Started"
        self.start_time = datetime.now()
        self.status = "In Progress"

    def complete(self):
        """Complete the Pomodoro."""
        assert self.start_time is not None
        assert self.end_time is None
        assert self.status == "In Progress"
        self.end_time = datetime.now()
        self.status = "Complete"

    def interrupt(self):
        """Interrupt the Pomodoro before completion"""
        assert self.start_time is not None
        assert self.end_time is None
        assert self.status == "In Progress"
        self.end_time = datetime.now()
        self.status = "Interrupted"

    def validate(self):
        """Validate Pomodoro Attributes"""
        self.validate_status()

    def validate_status(self):
        """
        Validate Pomodoro Status.

        Status must match a value from Pomodoro.valid_status.

        """
        if self.status not in Pomodoro.valid_status:
            raise AttributeError("Invalid Pomodoro Status")

