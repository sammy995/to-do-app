import func
import FreeSimpleGUI as fg

label = fg.Text("Type in a To-do")
input_box = fg.InputText(tooltip="Enter a to-do", key="todo",size=[41,5])
add_button = fg.Button("Add")
edit_button = fg.Button("Edit")
complete_button = fg.Button("Complete")
list_box = fg.Listbox(values=func.get_todos(), key="todos",
                      enable_events=True, size=[40,10])

window = fg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box,edit_button]],
                   font=('Comic Sans', 14))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = func.get_todos()
            new_todo = values["todo"] +'\n'
            todos.append(new_todo)
            func.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] +'\n'

            todos = func.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            func.write_todos(todos)

            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])
        case fg.WINDOW_CLOSED:
            break

window.close()

