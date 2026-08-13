# 🤖 Terminal AI Helper

A command-line assistant that translates **plain English requests into terminal commands** and asks for **explicit human confirmation before executing them**.

This project was created as part of an **MLH Challenge: Build a Terminal AI Helper**.

## 🎯 Challenge

The goal of this challenge is to create a command-line agent that can understand requests such as:

```text
Find all files larger than 100MB
```

and turn them into terminal commands while making sure the user approves the command before it runs.

## 🔄 How It Works

```text
User Request
     ↓
🤖 Agent interprets request
     ↓
💻 Terminal command generated
     ↓
⚠️ Human confirmation required
     ↓
   ┌───────────────┐
   │               │
  YES              NO
   │               │
   ↓               ↓
Execute           Cancel
```

The command is **never executed automatically**.

## ✨ Features

* 🤖 Converts simple English requests into terminal commands
* 💻 Executes Windows terminal commands
* ⚠️ Requires human confirmation before execution
* ✅ Allows the user to approve commands
* ❌ Allows the user to reject commands
* 🛑 Prevents rejected commands from running
* 🖥️ Runs directly from the terminal

## 🛠️ Technologies Used

* Python
* Python `subprocess`
* Windows Command Prompt
* PowerShell

## 💬 Example

The user enters:

```text
Show files
```

The agent generates:

```text
dir
```

Before executing it, the application asks:

```text
⚠️ HUMAN APPROVAL REQUIRED

The agent wants to execute:

    dir

Do you want to run this command? (y/n):
```

If the user enters:

```text
y
```

the command is executed.

If the user enters:

```text
n
```

the command is cancelled.

## 📋 Supported Requests

The current version supports examples such as:

```text
Show files
Show current directory
Show running processes
Show network information
Check Python version
Check Java version
Check Node version
Find all Java files
Find all Python files
Find files larger than 100MB
Find files larger than 1GB
```

## 📁 Project Structure

```text
terminal-ai-helper/
│
├── main.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

Clone this repository to your computer.

### 2. Open the project

Open the project folder in VS Code.

### 3. Open the terminal

Make sure the terminal is inside the project directory.

### 4. Run the program

```bash
python main.py
```

### 5. Enter a request

For example:

```text
Find all Java files
```

Then review the generated command and choose:

```text
y
```

to execute it or:

```text
n
```

to cancel it.

## 🧠 Human-in-the-Loop Safety

The most important feature of this project is the **human approval checkpoint**.

The agent can suggest a command, but it cannot execute the command until the user explicitly confirms it.

This helps prevent an autonomous system from performing an unexpected terminal action.

## 📚 What I Learned

Through this project, I learned:

* How to build a command-line application with Python
* How to accept user input from the terminal
* How to translate natural-language requests into commands
* How to execute commands using Python's `subprocess` module
* How to implement a human approval checkpoint
* Why confirmation is important when an AI agent can execute commands

## 🔮 Future Improvements

Possible improvements include:

* 🧠 Connect a real AI/LLM for natural-language command generation
* 🛡️ Detect and block dangerous commands
* 📋 Show a risk level before execution
* 📝 Add command history
* 🔄 Allow users to edit generated commands
* 🌐 Support Linux and macOS commands
* 💾 Save command history
* 🔐 Add additional safety rules

## ⚠️ Safety Note

This application executes terminal commands on the user's computer after approval.

Only approve commands that you understand and trust.

The current version uses predefined command mappings rather than a real AI model.

## 🏆 MLH Challenge

Built for the **MLH "Build a Terminal AI Helper" challenge**.

The project demonstrates an agent-like workflow where natural-language requests are translated into terminal commands and require **explicit human confirmation before execution**.

---

Built with Python 🐍 and 🤖
