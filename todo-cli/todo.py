import click  # to create a cli
import json  # to save and load task from a file
import os  # (Operating System) | to check if the file exist

# JSON file to store the task list
TODO_FILE = "todo.json"

def load_tasks():
    """Loads tasks from the JSON file. If the file does not exist, it returns an empty list."""
    if not os.path.exists(TODO_FILE):
        return[]
    with open(TODO_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager (CLI Application)"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task" : task, "done" : False})  # Default task status is 'False'
    save_tasks(tasks)
    click.echo(f"Task added seccessfully: {task}")

@click.command()
def list():
    """List ALL Task"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No task found!")
        return
    for index, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"  # Task completion status
        click.echo(f"{index}. {task['task']} [{status}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed!")
    else:
        click.echo(f"Invalid task number.")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        remove_task = tasks.pop(task_number - 1) # Remove the task from the list
        save_tasks(tasks)
        click.echo(f"Removed task {remove_task['task']}")
    else:
        click.echo(f"Invalid task number.")

# Add commands to the CLI group
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

# If the script is run directly, start the CLI
if __name__ == "__main__":
    cli()
    