import streamlit as st
from datetime import datetime
import requests

# Initialize tasks list using Streamlit's session state
session_state = st.session_state
if "tasks" not in session_state:
    session_state.tasks = []

# Streamlit UI
st.title("Enhanced To-Do App")

# Input field to add new tasks
new_task = st.text_input("Enter a new task:")
task_notes = st.text_area("Notes:", "")
due_date = st.date_input("Due Date:", min_value=datetime.today())

if st.button("Add Task"):
    if new_task:
        response = requests.post("http://backend:8000/tasks/", json={"task": new_task, "notes": task_notes, "due_date": due_date.isoformat()})
        if response.status_code == 200:
            st.success("Task added successfully!")
        else:
            st.error("Error adding task")
    else:
        st.warning("Please enter a task.")

# Display existing tasks
st.subheader("Tasks:")
response = requests.get("http://backend:8000/tasks/")
if response.status_code == 200:
    tasks = response.json()
    if tasks:
        for i, task in enumerate(tasks, start=1):
            st.write(f"{i}. Task: {task['task']}")
            if task["notes"]:
                st.write(f"   Notes: {task['notes']}")
            st.write(f"   Due Date: {task['due_date']}")
        
        # Delete tasks
        task_index_to_delete = st.selectbox("Select task to delete:", range(1, len(tasks) + 1))
        if st.button("Delete Task"):
            response = requests.delete(f"http://backend:8000/tasks/{tasks[task_index_to_delete - 1]['id']}")
            if response.status_code == 200:
                st.success("Task deleted successfully!")
            else:
                st.error("Error deleting task")
    else:
        st.info("No tasks yet.")
else:
    st.error("Error fetching tasks")
