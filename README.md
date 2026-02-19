# Task Tracker CLI

This is a simple command-line task tracker inspired by [roadmap.sh Task Tracker Project](https://roadmap.sh/projects/task-tracker).

## Features
- Add, list, update, and mark tasks
- Tasks stored in `tasks.json`

## Getting Started

### Requirements
- Python 3.7+

### Running the Project
1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the CLI:

```bash
python3 task_cli.py <task_id> <command>
```

#### Example Commands
- CLI Guide:
  ```bash
  python3 task_cli.py
  ```
- List tasks:
  ```bash
  python3 task_cli.py list
  ```
- Add a task:
  ```bash
  python3 task_cli.py add "Task description"
  ```
- Mark a task as in progress:
  ```bash
  python3 task_cli.py mark-in-progress <task_id>
  ```
- Mark a task as completed:
  ```bash
  python3 task_cli.py mark-completed <task_id>
  ```

## Reference
- [roadmap.sh Task Tracker Project](https://roadmap.sh/projects/task-tracker)

## License
MIT License
