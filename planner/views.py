from django.shortcuts import render, redirect
from .models import Task, Reminder

# View to list all tasks
def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks
    return render(request, 'planner/task_list.html', {'tasks': tasks})

# View to create a new task
def task_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Get the task name from the form
        description = request.POST.get('description')  # Get the task description
        due_date = request.POST.get('due_date')  # Get the due date
        Task.objects.create(name=name, description=description, due_date=due_date)  # Create and save the task
        return redirect('task_list')  # Redirect to the task list page
    return render(request, 'planner/task_create.html')

# View to display the details of a specific task
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)  # Fetch task by ID
    reminders = task.reminders.all()  # Fetch all reminders for the task
    return render(request, 'planner/task_detail.html', {'task': task, 'reminders': reminders})

# View to add a reminder for a task
def add_reminder(request, task_id):
    task = Task.objects.get(id=task_id)  # Get the task by ID
    if request.method == 'POST':
        remind_at = request.POST.get('remind_at')  # Get the reminder time
        Reminder.objects.create(task=task, remind_at=remind_at)  # Create and save the reminder
        return redirect('task_detail', task_id=task.id)  # Redirect to the task detail page
    return render(request, 'planner/add_reminder.html', {'task': task})