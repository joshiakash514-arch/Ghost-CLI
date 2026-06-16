# 👻 Ghost

Ghost is a multipurpose Python CLI toolkit that combines productivity, utility, and automation tools into a single command-line application.

Instead of installing multiple small scripts, Ghost provides everything through one command:

```bash
ghost <module> <command>
```

---

# Features

## ✅ Todo Manager

Manage tasks directly from your terminal.

### Commands

```bash
ghost todo add "Networking" 120
```

Add a new task with a target duration.

```bash
ghost todo list
```

View all tasks.

```bash
ghost todo start 1
```

Start tracking time for a task.

```bash
ghost todo rm 1
```

Delete a task.

```bash
ghost todo rm 1 --force
```

Delete a task without confirmation.

```bash
ghost todo reset
```

Delete all tasks.

```bash
ghost todo reset --force
```

Delete all tasks without confirmation.

### Features

- Add tasks
- Delete tasks
- Reset task list
- Track study/work sessions
- Task deadlines
- Completion tracking
- JSON-based storage

---

## 🔐 Password Manager

Generate and manage secure passwords.

### Planned Features

```bash
ghost pwd generate
ghost pwd suggest
ghost pwd check
ghost pwd list
```

- Password generation
- Password strength analysis
- Secure password storage
- Password suggestions

---

## 🌐 Source Grabber

Fetch and save source code or website content.

### Planned Features

```bash
ghost grabber source <url>
ghost grabber content <url>
```

- Website content extraction
- Source code grabbing
- Save results locally

---

## 📂 File Sorter

Automatically organize files into folders.

### Planned Features

```bash
ghost sorter downloads
ghost sorter desktop
```

- Organize Downloads folder
- Organize Desktop
- Sort by extension
- Sort by category

---

# Project Structure

```text
ghost/
│
├── main.py
│
├── commands/
│   ├── todo_cmds.py
│   ├── grabber_cmds.py
│   ├── pwd_cmds.py
│   └── sorter_cmds.py
│
├── command_handler/
│   ├── todo_handler.py
│   ├── grabber_handler.py
│   ├── pwd_handler.py
│   └── sorter_handler.py
│
├── core/
│   ├── todo.py
│   ├── grabber.py
│   ├── password_manager.py
│   └── sorter.py
│
└── data/
    ├── tasks.json
    └── pwd.json
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ghost.git
```

Move into the project directory:

```bash
cd ghost
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

# Usage

General syntax:

```bash
ghost <module> <command> [arguments]
```

Examples:

```bash
ghost todo add "DSA" 120

ghost todo list

ghost todo start 1

ghost pwd generate

ghost sorter downloads
```
---

# Future Roadmap

- Habit Tracker
- Study Analytics
- Pomodoro Timer
- Notes System
- Password Vault
- URL Shortener
- File Encryption
- System Monitoring
- Network Utilities

---

# License

MIT License

---

Made with Python 👻