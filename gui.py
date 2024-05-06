import func
import FreeSimpleGUI as fg

label = fg.Text("Type in a To-do")
input_box = fg.InputText(tooltip="Enter a to-do", key="todo")
add_button = fg.Button("Add")
edit_button = fg.Button("Edit")
complete_button = fg.Button("Complete")

window = fg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button]],
                   font=('Comic Sans', 14))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = func.get_todos()
            new_todo = values["todo"] +'\n'
            todos.append(new_todo)
            func.write_todos(todos)
        case fg.WINDOW_CLOSED:
            break
window.close()

