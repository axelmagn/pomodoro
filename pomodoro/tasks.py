"""
Read/write/manage tasks

"""

class Task(object):
    """
    Describe a Pomodoro Task.

    Instance Variables:
        name(str)
        description(str)
        status(str)
    """

    valid_status = ["Incomplete", "Complete"]

    def __init__(self, name, description=None, status="Incomplete"):
        """Construct a new Task."""
        self.name = name
        self.description = description
        self.status = status
        self.validate()

    def set_status(self, status):
        """Set Task Status."""
        self.status = status
        self.validate_status()

    def complete(self):
        """Set Task Status to Complete."""
        self.set_status("Complete")

    def validate(self):
        """Validate Task Attributes."""
        # self.validate_name()
        # self.validate_description()
        self.validate_status()

    def validate_status(self):
        """Validate Task Status."""
        if self.status not in Task.valid_status:
            raise AttributeError("Invalid Task Status")
