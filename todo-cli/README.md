# Todo CLI Application

A simple command-line To-Do list manager built using Python and Click.

## Features

- Add tasks
- List all tasks
- Mark tasks as completed
- Remove tasks

## Installation

Make sure you have Python installed, then install the required package:

```sh
pip install click
```

## Usage

Run the script using the command:

```sh
python todo.py <command> [arguments]
```

### Commands

- **Add a new task**

  ```sh
  python todo.py add "Your task here"
  ```

- **List all tasks**

  ```sh
  python todo.py list
  ```

- **Mark a task as completed**

  ```sh
  python todo.py complete <task_number>
  ```

  Example:

  ```sh
  python todo.py complete 1
  ```

- **Remove a task**

  ```sh
  python todo.py remove <task_number>
  ```

  Example:

  ```sh
  python todo.py remove 1
  ```

##
