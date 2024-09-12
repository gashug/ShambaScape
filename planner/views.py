from django.shortcuts import render, redirect
from .models import Task, Reminder
from datetime import datetime, timedelta

# Planner home view
def planner_home(request):
    # Get upcoming tasks (next 7 days)
    upcoming_tasks = Task.objects.filter(due_date__gte=datetime.now(), due_date__lte=datetime.now() + timedelta(days=7))
    
    # Get upcoming reminders
    upcoming_reminders = Reminder.objects.filter(remind_at__gte=datetime.now(), remind_at__lte=datetime.now() + timedelta(days=7))
    
    # Task completion stats
    completed_tasks_count = Task.objects.filter(due_date__lte=datetime.now()).count()
    pending_tasks_count = Task.objects.filter(due_date__gt=datetime.now()).count()
    total_tasks = completed_tasks_count + pending_tasks_count
    progress_percentage = (completed_tasks_count / total_tasks * 100) if total_tasks > 0 else 0

    return render(request, 'planner/planner_home.html', {
        'upcoming_tasks': upcoming_tasks,
        'upcoming_reminders': upcoming_reminders,
        'completed_tasks_count': completed_tasks_count,
        'pending_tasks_count': pending_tasks_count,
        'progress_percentage': progress_percentage,
    })

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