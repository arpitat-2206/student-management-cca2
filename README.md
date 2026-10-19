# Student Management System — CCA 2

A beginner-friendly Flask web application for adding, viewing and deleting student records.

## Features
- Add a student with roll number, name and department
- View student records in a table
- Delete a student
- Health-check endpoint at `/health`

## Run locally
1. Install Python 3.12 or a compatible recent Python version.
2. Open a terminal in this folder.
3. Install dependencies:
   `python -m pip install -r requirements.txt`
4. Start the app:
   `python app.py`
5. Open `http://127.0.0.1:5000`

## Docker
Build the image:
`docker build -t student-management:1.0 .`

Run the container:
`docker run --rm -p 5000:5000 student-management:1.0`

Then open `http://127.0.0.1:5000`.

## Important note
This starter version stores records in memory. Records added during a run are not permanently saved and reset when the application restarts. That is acceptable for a first pipeline demonstration; persistent storage can be added later if required.
