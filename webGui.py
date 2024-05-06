import streamlit as st
import func

todos = func.get_todos()
def add_todo():
    todo= st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.write_todos(todos)

def clear_text():
    st.session_state["new_todo"] = ""



st.title("My Todo App")
st.subheader("Simple To-do application")
st.write("Increase your productivity!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



input1 = st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

st.button("Clear", on_click=clear_text)


