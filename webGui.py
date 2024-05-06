import streamlit as st
import func

todos = func.get_todos()
def add_todo():
    todo= st.session_state["new_todo"] +'\n'
    todos.append(todo)
    func.write_todos(todos)


st.title("My Todo App")
st.subheader("Simple To-do application")
st.write("Increase your productivity!")

for todo in todos:
    st.checkbox(todo)



st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

