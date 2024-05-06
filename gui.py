import func
import FreeSimpleGUI as fg

label = fg.Text("Type in a To-do")
input_box = fg.InputText(tooltip="Enter a to-do")
add_button = fg.Button("Add")
edit_button = fg.Button("Edit")
complete_button = fg.Button("Complete")

window = fg.Window('My To-Do App', layout=[[label], [input_box, add_button]])

window.read()
window.close()