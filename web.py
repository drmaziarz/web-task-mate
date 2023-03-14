import streamlit as st
from functions import get_todos, write_todos
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

todos = get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("TaskMate")
st.subheader("Your productivity partner")
st.write("")

new_todo = st.text_input(label="Enter a todo:",
                         placeholder="Add new todo...",
                         on_change=add_todo,
                         key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.session_state.setdefault("new_todo", "")
if new_todo != st.session_state["new_todo"]:
    st.session_state["new_todo"] = new_todo
