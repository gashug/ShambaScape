from django.db import models

# Model representing a garden_related task
class Task(models.Model):
    name = models.CharField(max_length=100)  # Task name (e.g., "Water the roses")
    description = models.TextField(blank=True)  # Optional task description
    due_date = models.DateTimeField()  # Date and time the task is due
    completed = models.BooleanField(default=False)  # Field to track if the task is completed

    def __str__(self):
        return self.name  # Returns the task name when referenced

# Model representing a reminder for a specific task
class Reminder(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="reminders")  # Reminder is linked to a task
    remind_at = models.DateTimeField()  # Date and time when the reminder should trigger

    def __str__(self):
        return f"Reminder for {self.task.name} at {self.remind_at}"