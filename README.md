# Property Operations Automation and AI Project

This project is a functional prototype I built for the Automation and Analytics role at reltix. It shows how to automate property management tasks using Python and data.

## Project Goal
In property management, being fast is important. This project automates the process of taking a maintenance request from a tenant and turning it into a prioritized action using data.

## Features

### Automation Bridge
I used FastAPI to build a system that receives property issues. I added logic that reads the issue description and automatically gives it a priority score from 1 to 10.

### Workflow Trigger (n8n Simulation)
I created a function that triggers an alert for high-priority problems. This simulates how I would use n8n to send real-time alerts for serious risks like water leaks or fire.

### Asking Data Questions (Text-to-SQL)
I built a feature called ask-ai. It allows a user to ask a question in plain English, like "How many high urgency tickets do we have?" The code then searches the database and gives the answer without the user needing to know SQL.

### Database Storage
I used SQLite to save all the information about properties and tickets. I also added error handling (try and except blocks) to make sure the system stays stable even if something goes wrong.

## How to run this on your computer

1. Download the files from this repository.
2. Install the necessary tools by typing this in your terminal: 
   pip install fastapi uvicorn requests pandas
3. Start the project by running: 
   python main.py
4. Go to http://127.0.0.1:8000/docs in your browser to test the system.

Developed by
Sameer Sameer
