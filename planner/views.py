from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Reminder
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from django.utils import timezone

# Planner home view
def planner_home(request):
    # Get upcoming tasks (next 7 days)
    upcoming_tasks = Task.objects.filter(
        due_date__gte=timezone.now(),
        due_date__lte=timezone.now() + timedelta(days=7)
    )
    
    # Get upcoming reminders
    upcoming_reminders = Reminder.objects.filter(
        remind_at__gte=timezone.now(),
        remind_at__lte=timezone.now() + timedelta(days=7)
    )
    
    # Task completion stats
    completed_tasks_count = Task.objects.filter(due_date__lte=timezone.now()).count()
    pending_tasks_count = Task.objects.filter(due_date__gt=timezone.now()).count()
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
    # Filtering options
    status_filter = request.GET.get('status', 'all')  # Get the status filter from query string
    tasks = Task.objects.all()

    # Apply filters
    if status_filter == 'completed':
        tasks = tasks.filter(completed=True)
    elif status_filter == 'pending':
        tasks = tasks.filter(completed=False)
    elif status_filter == 'overdue':
        tasks = tasks.filter(due_date__lt=timezone.now(), completed=False)

    # Apply pagination (10 tasks per page)
    paginator = Paginator(tasks, 10)
    page_number = request.GET.get('page')
    tasks_page = paginator.get_page(page_number)

    if request.method == 'POST':
        # Handle marking a task as completed
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        task.completed = True
        task.save()
        return redirect('task_list')

    return render(request, 'planner/task_list.html', {
        'tasks': tasks_page,
        'status_filter': status_filter
    })

# View to create a new task
def task_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Get the task name from the form
        description = request.POST.get('description')  # Get the task description
        due_date = request.POST.get('due_date')  # Get the due date

        # Convert the due_date to a timezone-aware datetime
        due_date = timezone.make_aware(datetime.strptime(due_date, '%Y-%m-%dT%H:%M'))

        Task.objects.create(name=name, description=description, due_date=due_date)  # Create and save the task
        return redirect('task_list')  # Redirect to the task list page
    return render(request, 'planner/task_create.html')

# View to display and edit the details of a specific task
def task_detail_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Fetch task by ID
    reminders = task.reminders.all()  # Fetch all reminders for the task

    if request.method == 'POST':
        # Handle task update
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')

        # Convert the due_date to a timezone-aware datetime
        task.due_date = timezone.make_aware(datetime.strptime(task.due_date, '%Y-%m-%dT%H:%M'))

        task.completed = 'completed' in request.POST  # Mark as completed if the checkbox is checked
        task.save()
        return redirect('task_detail_edit', task_id=task.id)

    return render(request, 'planner/task_detail_edit.html', {
        'task': task,
        'reminders': reminders
    })

# View to add a reminder for a task
def add_reminder(request, task_id):
    task = Task.objects.get(id=task_id)  # Get the task by ID
    if request.method == 'POST':
        remind_at = request.POST.get('remind_at')  # Get the reminder time

        # Convert the remind_at to a timezone-aware datetime
        remind_at = timezone.make_aware(datetime.strptime(remind_at, '%Y-%m-%dT%H:%M'))

        Reminder.objects.create(task=task, remind_at=remind_at)  # Create and save the reminder
        return redirect('task_detail_edit', task_id=task.id)  # Redirect to the task detail page
    return render(request, 'planner/add_reminder.html', {'task': task})

# View to delete an existing task
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'planner/task_confirm_delete.html', {'task': task})