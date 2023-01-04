import streamlit as st  # Streamlit allows you to create a stunning-looking application with only a few lines of code.
import functions as fs

# import web_app_func as wf

todos = fs.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # session_state is like a dict
    todos.append(todo)
    fs.write_todos(todos)


st.title("My To-Do's")
st.subheader("This is my To-Do app")
st.write('This app is to help with productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  # best to have a dynamic key to access
    if checkbox:
        todos.pop(index)
        fs.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="new todo", placeholder="Add new to-do...",
              on_change=add_todo, key="new_todo", label_visibility='hidden')