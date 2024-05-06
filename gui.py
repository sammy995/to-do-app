import func
import FreeSimpleGUI as fg
import time

fg.theme("Dark Teal 12")
timelabel = fg.Text('',key='clock')
label = fg.Text("Type in a To-do")
input_box = fg.InputText(tooltip="Enter a to-do", key="todo",size=[41,1])
add_button = fg.Button("Add")
edit_button = fg.Button("Edit")
complete_button = fg.Button("Complete")
exit_button = fg.Button("Exit")
list_box = fg.Listbox(values=func.get_todos(), key="todos",
                      enable_events=True, size=[40,10])

window = fg.Window('My To-Do App',
                   layout=[[timelabel],
                           [label],
                           [input_box, add_button],
                           [list_box,edit_button, complete_button],
                           [exit_button]],
                   font=('Comic Sans', 14))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = func.get_todos()
            new_todo = values["todo"] +'\n'
            todos.append(new_todo)
            func.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] +'\n'

                todos = func.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                func.write_todos(todos)

                window["todos"].update(values=todos)
            except IndexError:
                fg.Popup("Please select a todo first!", font=("Comic Sans",10))

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = func.get_todos()

                todos.remove(todo_to_complete)
                func.write_todos(todos)

                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                fg.Popup("Please select a todo first!", font=("Comic Sans", 10))

        case fg.WINDOW_CLOSED:
            break
        case "Exit":
            break


window.close()

