import streamlit as st
import datetime

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Title
st.title("🗓️ Daily Task Manager")

# --- Add New Task ---
with st.form("Add Task", clear_on_submit=True):
    task_title = st.text_input("Task Title", placeholder="e.g. Complete project report")
    task_desc = st.text_area("Description", placeholder="Optional task details")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    submitted = st.form_submit_button("Add Task")

    if submitted and task_title.strip():
        st.session_state.tasks.append({
            "title": task_title,
            "description": task_desc,
            "priority": priority,
            "completed": False,
            "created_at": datetime.datetime.now()
        })
        st.success("Task added successfully!")

# --- Show Tasks ---
st.subheader("📋 Your Tasks")

if not st.session_state.tasks:
    st.info("No tasks yet. Add your first task above!")
else:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.05, 0.95])
        with col1:
            if st.checkbox("", key=f"check_{i}", value=task["completed"]):
                task["completed"] = not task["completed"]
        with col2:
            task_style = "✅ ~~{}~~".format(task["title"]) if task["completed"] else f"🔹 {task['title']}"
            st.markdown(f"**{task_style}**  \n*Priority:* {task['priority']}  \n{task['description']}")

# --- Remove Completed Tasks ---
if any(task["completed"] for task in st.session_state.tasks):
    if st.button("🗑️ Clear Completed Tasks"):
        st.session_state.tasks = [t for t in st.session_state.tasks if not t["completed"]]
        st.success("Completed tasks removed!")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")