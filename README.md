# AI Model Zoo (Mini Version)

AI Model Zoo is a Python console-based application that simulates a repository for managing artificial intelligence models.  
The project demonstrates basic system design concepts and CRUD operations applied to an AI-oriented context.

## Problem Statement
Managing multiple AI models requires tracking their tasks, performance metrics, and training status.  
Without a structured system, maintaining and updating such information becomes inefficient and error-prone.

## Solution
AI Model Zoo provides a simple menu-driven system that allows users to manage AI models by adding, updating, displaying, and removing them in an organized manner.

## Features
- Add new AI models
- Update model task, accuracy, or training status
- Remove existing models
- Display all models in a formatted table
- Exit system using a loop-based menu

## Model Attributes
Each model includes the following attributes:
- Model Name
- Task (Classification / Detection / NLP)
- Accuracy (0–100)
- Status (Trained / Needs Training)

## Technologies Used
- Python 3

## Project Structure
AI-Model-Zoo/ │ ├── main.py └── README.md
Copy code

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Model-Zoo.git
Navigate to the project directory:
Copy code
Bash
cd AI-Model-Zoo
Run the application:
Copy code
Bash
python main.py
Example Use Case
This system can be used as a simplified model management tool where users maintain information about AI models, their performance, and training readiness.
It is suitable for demonstrating CRUD operations and basic workflow management in an AI-related project.
Limitations
Console-based interface only
No persistent storage (data is lost after program termination)
No authentication or role management
Future Improvements
Add file-based or database storage
Implement search and filtering functionality
Add graphical user interface (GUI)
Extend support for additional AI metrics
Commit Message
Initial commit: AI Model Zoo CRUD system
Project Description
This is a mini AI Model Zoo system that demonstrates CRUD operations and basic system design using Python.
This project was created as part of an AI training task to demonstrate system thinking and CRUD implementation.
Author
Rawan Aldawsari
