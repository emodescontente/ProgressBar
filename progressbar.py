from timer import countdown_timer

def get_input():
    while True:
        valor = input("> ")
        if valor != "":
            return valor
        print("Please, type something.")

def p():
    print("")

def ShowTaskList():
        for t in tasks:
            print(f"{t['id']}. [{t['type']}] {t['name']}: {t['status']}")

def AddTask(type: str, task_name: str):
    global actual_id
    tasks.append({"id": actual_id + 1, "type": type, "name": task_name, "status": "Unfinished"})
    actual_id += 1

def NoTaskDone():
    for t in tasks:
        if t["status"] == "Done":
            return False 
    return True

def CheckTask(id: int, checker: str):
    for t in tasks:
        if t["id"] == id:
            match checker:
                case "type":
                    return t["type"]
                case "name":
                    return t["name"]
                case "status":
                    return t["status"]
    return None

def EditTask(id: int, checker: str, alt):
    for t in tasks:
        if t["id"] == id:
            match checker:
                case "type":
                    t["type"] = alt
                case "name":
                    t["name"] = alt
                case "status":
                    t["status"] = alt
                case "id":
                    t["id"] = alt

# ritual de início
print("Hello, world!")

# Agora, começo do projeto PROGRESS BAR, HELL YEAH1!1!!!1111!1
print("""Wellcome to Progress Bar!
Type [add] to enter your tasks.
Type [del] to delete one.
Type [done] and the task number when you complete one task (done a timed task will lead you into a timer).
Type [undo] to undo a task.
Type [progress] when you want to check the tasks and the progress done.
Type [clear] to delete all the tasks.
Type [close] to end program.""")
command_list = ["ADD", "DEL", "DONE", "PROGRESS", "CLOSE", "HELP", "CLEAR", "UNDO"]

tasks = [
    {"id": 1, "type": "S", "name": "Feed the cat", "status": "Unfinished"},
    {"id": 2, "type": "S", "name": "Feed the dog", "status": "Done"},
    {"id": 3, "type": "S", "name": "Feed the horse", "status": "Unfinished"},
    {"id": 4, "type": "S", "name": "Feed the fish", "status": "Done"},
    {"id": 5, "type": "S", "name": "Feed the baby", "status": "Done"}
]
actual_id = 1

print("""
Type [help] if you need a reminder of the commands.""")

while True:
    p()
    print("Type your command:")
    user_input = get_input().strip().upper()

    if user_input == "CLOSE":
        break

    if user_input not in command_list:
        p()
        print("Please, type a valid command.")
        continue

    if user_input not in ["ADD", "HELP", "END"] and tasks == []:
        p()
        print("Try start by adding tasks with [add]")
        continue

    if user_input == "UNDO" and NoTaskDone():
        p()
        print("No task is done, type [done] if you want mark a task as done.")
        continue

    match user_input:
        case "HELP":
            print("""
Type [add] to enter your tasks (1 per time).
Type [del] to delete one.
Type [done] and the task number when you complete one task (done a timed task will lead you into a timer).
Type [undo] to undo a task.
Type [progress] when you want to check the progress done.
Type [close] to end the program.""")
            
        case "DONE":
            print("""
Type the number of the task you want to mark as done.
Type [end] to stop.
""")

            ShowTaskList()

            while True:
                p()
                done_input = get_input().strip().upper()
                if done_input == "END":
                    break
                try:
                    done_input = int(done_input)
                except ValueError:
                    done_input = 0
                    p()
                    print("Please, type a valid number inside the tasks index.")
                    continue

                if CheckTask(done_input, "status") == "Done":
                    p()
                    print("This task is already done.")
                    continue

                if 0 < done_input <= len(tasks):
                    EditTask(done_input, "status", "Done")
                    p()
                    ShowTaskList()
                    print("Continue.")
                else:
                    p()
                    print("Please, type a valid number inside the tasks index.")

        case "UNDO":
            p()
            print("Type the number of the task you want to undo.")
            print("Type [end] to stop.")
            p()
            ShowTaskList()
            p()
    
            while True:
                undo_input = get_input().strip().upper()

                if undo_input == "END":
                    break

                try:
                    undo_input = int(undo_input)
                except ValueError:
                    p()
                    print("That's not a number.")
                    continue
                if CheckTask(undo_input, "status") == "Unfinished":
                    p()
                    print("That task is not done.")
                    continue
                if 0 > undo_input > actual_id:
                    p()
                    print("Please, type a valid number inside the index.")
                    continue

                EditTask(undo_input, "status", "Unfinished")
                print("Continue.")
                p()

        case "ADD":
            description = """
Please, input your task type and the task.
Types:
[S] Single: tasks that only need complete 1 time. Example: Feed the cat.
[C] CheckList: tasks that need complete various times. Example: Homeworks done.
[T] Timed: tasks that need time. Example: Reading time
It should be like: S Feed the cat
Type [end] to stop inputing tasks."""

            print(description)
            while True:
                task_input = get_input()

                task_ender = task_input.strip().upper()
                if task_ender == "END":
                    break
                # Divide no primeiro espaço que encontrar num array
                parts = task_input.split(maxsplit=1)
                
                parts[0] = parts[0].strip().upper()

                if len(parts) < 2:
                    print("Please, input both the task type and the task name.")
                    continue

                if parts[0] not in ["C", "S", "T"]:
                    print("Please, input a valid type")
                    continue

                AddTask(parts[0], parts[1])
                ShowTaskList()
                print("Continue.")
                p()
                continue   
            
        case "DEL":
            print("""  
Type the number of the task to delete it.  
Type [end] to stop.        
                  """) 
            while True:
                ShowTaskList() 
                p()
                del_input = get_input().strip().upper()

                if del_input == "END":
                    break

                try:
                    del_input = int(del_input)
                except ValueError:
                    p()
                    print("That's not a number.")
                    p()
                    continue

                tasks.pop(del_input - 1)
                actual_id -= 1
                for t in tasks:
                    if t["id"] > del_input:
                        t["id"] -= 1
                print("Continue.")

                if tasks == []:
                    print ("You deleted all the tasks.")
                    break

        case "CLEAR":
            print("""
Are you sure that you want to clear all the tasks?
If yes, type [y], else type anyting.
""")
            clear_input = get_input().strip().upper()

            if clear_input == "Y":
                tasks = []
                actual_id = 1
                p()
                print("All tasks has been deleted.")
                p()

        case "PROGRESS": 
            p()
            ShowTaskList()