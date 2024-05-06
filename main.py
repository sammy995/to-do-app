from func import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is " +now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        if (len(todo)) > 0:
            todos = get_todos()

            todos.append(todo+'\n')

            write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.title().strip('\n')
            row = f"{index+1}:{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            position = int(user_action[5:])
            todos = get_todos()

            position -= 1

            edited_todo = input("Enter updated todo: ")
            todos[position] = edited_todo+'\n'

            write_todos(todos)
        except ValueError:
            print("Invalid number")
            continue

    elif user_action.startswith("complete"):
        try:
            position = int(user_action[9:])
            todos = get_todos()

            index = position - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("Invalid number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid action")


print("Bye...")
