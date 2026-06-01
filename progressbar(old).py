from timer import countdown_timer

def get_input():
    while True:
        valor = input("> ")
        if valor != "":
            return valor
        print("Please, type something.")

def p():
    print("")

def AddTask(type: str, task_name: str, additional: int = None):
    global actual_id
    if type == "C":
        task_list[actual_list].append({"id": actual_id + 1, "type": type, "name": task_name,"num": 0, "cl_final": additional})
    elif type == "S":
        task_list[actual_list].append({"id": actual_id + 1, "type": type, "name": task_name, "status": "Unfinished"})
    elif type == "T":
        task_list[actual_list].append({"id": actual_id + 1, "type": type, "name": task_name, "timer": additional, "status": "Unfinished"})
    actual_id += 1

def NoTaskDone():
    for t in task_list[actual_list]:
        if t['type'] != 'C':
            if t["status"] == "Done":
                return False 
        else:
            if t['num'] != 0:
                return False
    return True

def CheckTask(id: int, checker: str):
    for t in task_list[actual_list]:
        if t["id"] == id:
            match checker:
                case "type":
                    return t["type"]
                case "name":
                    return t["name"]
                case "status":
                    if t["type"] in ["S", "T"]:
                        return t["status"]
                case "cl_final":
                    if t["type"] == "C":
                        return t["cl_final"]
                case "num":
                    if t["type"] == "C":
                        return t["num"]
                case "timer":
                    if t["type"] == "T":
                        return t["timer"]
    return None

def EditTask(id: int, checker: str, alt):
    for t in task_list[actual_list]:
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
                case "cl_final":
                    t["cl_final"] = alt
                case "timer":
                    t["timer"] = alt


def ShowTime(time):
    horas, resto = divmod(time, 3600)
    minutos, segundos = divmod(resto, 60)
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

def ShowTaskList():
    print(f'{actual_list}:')
    for t in task_list[actual_list]:
        if t["type"] == "C":
            print(f"  {t['id']}. [{t['type']}] {t['name']}: {t['num']}/{t['cl_final']}")
        elif t["type"] == "S":
            print(f"  {t['id']}. [{t['type']}] {t['name']}: {t['status']}")
        elif t["type"] == "T":
            print(f"  {t['id']}. [{t['type']}] {t['name']}, {ShowTime(t['timer'])}: {t['status']}")

def ShowLists():
    num = 1
    p()
    for list_name, task in task_list.items():
        print(f"{num}°. {list_name}")
        if task == []:
            print("   This list is empty.")
        else:
            for t in task:
                if t["type"] == "C":
                    print(f"   {t['id']}. [{t['type']}] {t['name']}: {t['num']}/{t['cl_final']}")
                elif t["type"] == "S":
                    print(f"   {t['id']}. [{t['type']}] {t['name']}: {t['status']}")
                elif t["type"] == "T":
                    print(f"   {t['id']}. [{t['type']}] {t['name']}, {ShowTime(t['timer'])}: {t['status']}")
        num += 1

def CheckNum(num):
    try:
        num = int(num)
        return num
    except ValueError:
        p()
        print("Please, type a valid number inside the index.")
        return False
def GetNum():
    while True:
        num = get_input().strip()
        try:
            num = int(num)
            return num
        except ValueError:
            p()
            print("Please, type a valid number inside the index.")
            continue

def GetTimer():
    time = 0
    p()
    print("Type the time to increment the timer.")
    print("[S]: seconds, [M]: minutes, [H]: hours.")
    print("It should be like: S 30, or S -10 if you want do decrement. Type [end] to stop.")
    while True:
        time_input = get_input().strip().upper()
        if time_input =="END":
            break
        parts_timer = time_input.split(maxsplit=1)
        if len(parts_timer) != 2:
            p()
            print("Please, type only the time format and the time.")
            continue
        if parts_timer [0] not in ["S","M","H"]:
            p()
            print("Please, type a valid format.")
            continue
        try:
            parts_timer[1] = int(parts_timer[1])
        except ValueError:
            p()
            print("Please, type a valid number.")
            continue
        number = parts_timer[1]
        timer = 0
        match parts_timer[0]:
            case "S":
                timer += number
            case "M":
                timer += (number * 60)
            case "H":
                timer += (number * 3600)
        if timer < 0 and time + timer < 0:
            p()
            print("Can't do a negative timer, sorry.")
            continue
        time += timer
        print(ShowTime(time))
        print("Continue:")
        continue
    return time




# Agora, começo do projeto PROGRESS BAR, HELL YEAH1!1!!!1111!1
print("---------------------------------------------------")
print("""Welcome to Progress Bar!
Type [add] to enter your tasks.
Type [del] to delete one.
Type [done] to mark a task as done.
Type [undo] to undo or decrease a task.
Type [edit] to edit a task name or value.
Type [progress] to check the tasks and the progress done.
Type [clear] to delete all the tasks.
Type [list] to see and change trought task lists.
Type [close] to end program (or ctrl+c).""")

command_list = ["ADD", "DEL", "DONE", "PROGRESS", "CLOSE", "HELP", "CLEAR", "UNDO", "EDIT", "LIST"]
valid_types = ["S", "C", "T"]
task_list = {"Tasks": []}
actual_list = "Tasks"
actual_id = 0
pb_type = True
print("""
Type [help] if you need a reminder or a more detailed description of the commands.""")

while True:
    p()
    print("Type your command:")
    user_input = get_input().strip().upper()
    if user_input == "Q PROGRESS":
        pb_type = not pb_type
        p()
        print("Progress bar type changed.")
        continue

    if user_input == "CLOSE":
        break

    if user_input not in command_list:
        p()
        print("Please, type a valid command.")
        continue

    if user_input not in ["ADD", "HELP", "END", "LIST"] and task_list[actual_list] == []:
        p()
        print("Try start by adding tasks with [add]")
        continue

    if user_input == "UNDO" and NoTaskDone():
        p()
        print("No task is done, type [done] if you want to mark a task as done.")
        continue

    match user_input:
        case 'LIST':
            print("---------------------------------------------------")
            print("""Here you can see your lists of tasks.
    * = number of the list.
Type [create] [name of the new list] to create a new list.
Type [move] * to move to the tasks of the list.
Type [del] * to delete a list.
Type [edit] * to edit a list name.
Type [end] to stop.
""")
            ShowLists()
            valid_input = ['MOVE', 'CREATE', 'DEL', 'EDIT']
            while True:
                p()
                list_input = get_input().strip().split(maxsplit=1)
                list_input[0] = list_input[0].upper()
                if list_input[0] == "END":
                    print("---------------------------------------------------")
                    break
                
                if list_input[0] == "CREATE":
                    for l in task_list:
                        exists = any(list_input[1].upper() == l.upper() for l in task_list)
                        if exists:
                            print("A list with that name already exists.")
                            break
                    task_list.update({list_input[1]: []})
                    ShowLists()
                    print("Continue.")
                    continue

                if len(list_input) != 2:
                    p() # type: ignore
                    print('Please, type both comand and the list number.')

                if list_input[0] not in valid_input:
                    print("Please, type a valid input.")
                    continue
                list_number = CheckNum(list_input[1]) # type: ignore
                if list_number == False:
                    continue
                if 0 > list_number or list_number > len(task_list):
                    p()
                    print('Please, type a valid number inside the index.')
                    continue
                match list_input[0]:
                    case "MOVE":
                        list_name = list(task_list.keys())
                        index = list_number - 1
                        name = list_name[index]
                        actual_list = name
                        list_lenght = list(task_list.values())
                        actual_id = len(list_lenght[index])
                        p()
                        ShowLists()
                        print(f"Now, you are in the list: {actual_list}")
                        continue
                    case 'DEL':
                        list_name = list(task_list.keys())
                        index = list_number - 1
                        name = list_name[index]
                        task_list.pop(name)
                        p()
                        ShowLists()
                        print("The list has been deleted.")
                        continue
                    case 'EDIT':
                        new_name = input("New name: ") 
                        
                        list_name = list(task_list.keys())
                        index = list_number - 1
                        name = list_name[index]
                        if actual_list == name:
                            actual_list = new_name
                        task_list[new_name] = task_list.pop(name)
                        p()
                        print("The name of the list has been renamed.")
                        ShowLists()
                        continue
                

        case "HELP":
            print("---------------------------------------------------")
            print("""Type [add] to enter your tasks.
Type [del] to delete one.
Type [done] to mark a task as done.
    Marking a timed task will lead you into a timer.
    Type: Q [the task number] with a C task type to quickly add one check.
Type [undo] to undo or decrease a task.
    Type: Q [the task number] to quickly decrease all checks.
Type [edit] to edit a task name or value.
Type [progress] when you want to check the tasks and the progress done.
    You can change the visual type of the progress bar by typing [Q progress].
Type [clear] to delete all the tasks.
Type [lists] to see and change trought task lists.
Type [close] to end program (or ctrl+c).""")
            print("---------------------------------------------------")
        case "EDIT":
            print("---------------------------------------------------")
            print("""Type the number of the task that you want to edit, then:
Type [N] if you want to change the name.
Type [V] if you want to change a vallue.
It should be like: 1 N.
Type [end] to stop.
""")
            ShowTaskList()
            while True:
                p()
                edit_input = get_input().strip().upper() # type: ignore
                edit_input = edit_input.split(maxsplit=1)
                if edit_input[0] == "END":
                    print("---------------------------------------------------")
                    break
                if 2 > len(edit_input) or len(edit_input) > 3:
                    p()
                    print('Please, input only the task number and what you want to edit.')
                    continue
                number = CheckNum(edit_input[0])
                if not number:
                    continue
                if 0 > number > len(task_list[actual_list]) - 1:
                    p()
                    print("Please, type a vaid number inside the index.")
                    continue
                if edit_input[1] not in ["N", "V"]:
                    p()
                    print("Please, type a valid input.")
                    continue

                if edit_input[1] == "N":
                    name = input("New name: ")
                    EditTask(number, "name", name)
                    p()
                    ShowTaskList()
                    p()
                    print('The task has been renamed.')
                    continue

                if edit_input[1] == "V":
                    i = next((t for t in task_list[actual_list] if t["id"] == number), None) # type: ignore

                    match i["type"]:
                        case "S":
                            p()
                            print("That task does not have a vallue.")
                            continue
                        case "C":
                            print("Type the new vallue of checks:")
                            while True:
                                val_input = get_input().strip()
                                vallue = CheckNum(val_input)
                                if not vallue:
                                    continue

                                if vallue < i["num"]:
                                    print("You canot change the vallue under the checks done.")
                                    continue
                                i['cl_final'] = vallue
                                p()
                                ShowTaskList()
                                p()
                                print('The task has been edited.')
                                break
                        case "T":
                            time = GetTimer()
                            p()
                            ShowTaskList()
                            p()
                            print('The task has been edited.')
                            EditTask(i['id'], "timer", time)

                

        case "DONE":
            print("---------------------------------------------------")
            print("""Type the number of the task you want to mark as done.
A Single task will just be marked as done;
A CheckList one will add the number that you want to the checks counter;
A Timed one will lead you into a timer.
Type [end] to stop.
""")

            ShowTaskList()

            while True:
                p()
                done_input = get_input().strip().upper()
                if done_input == "END":
                    print("---------------------------------------------------")
                    break

                parts = done_input.split(maxsplit=1)

                if parts[0] == "Q":
                    if len(parts) != 2:
                        p()
                        print('Please, type the task number next time.')
                        continue
                    task_id = CheckNum(parts[1])
                    if not task_id:
                        continue
                    task_found = next((t for t in task_list[actual_list] if t["id"] == task_id), None)

                    if not task_found:
                        print("This task does not exist")
                        continue
                    if task_found["type"] == "C":
                        if task_found["num"] < task_found["cl_final"]:
                            task_found["num"] += 1
                            p()
                            ShowTaskList()
                            print("Continue.")
                            continue
                        else:
                            p()
                            print("This task is already done.")
                            continue
                    else:
                        p()
                        print("The type of the task is not [C].")
                        continue
                
                done_input = CheckNum(done_input)
                if not done_input:
                    continue
                if 0 > done_input or done_input > len(task_list[actual_list]):
                    p()
                    print('Please, type a valid number inside the index.') 
                    continue
                task = 0
                for t in task_list[actual_list]:
                    if t["id"] == done_input:
                        task = t
                if (task["type"] in ["S", "T"] and task["status"] == "Done") or (task["type"] == "C" and task["num"] == task["cl_final"]):
                    p()
                    print("This task is already done.")
                    continue

                if 0 < done_input <= len(task_list[actual_list]):
                    if CheckTask(done_input, "type") == "S":
                        EditTask(done_input, "status", "Done")
                    elif CheckTask(done_input, "type") == "T":
                        print("""
Are you sure? When you start this timer, you can no longer exit it while is running.
Type [Y] to run.
Type anything to cancel.""")
                        confirm = get_input().strip().upper()
                        if confirm == "Y":
                            countdown_timer(CheckTask(done_input, "timer"))
                            EditTask(done_input, "status", "Done")
                    elif CheckTask(done_input, "type") == "C":
                        p()
                        print("How much?")
                        while True:
                            num = GetNum()
                            if 0 > num:
                                p()
                                print("That's a negative number. If you want to decrease, type 0 and go to the [undo] menu.")
                                continue
                            if num + CheckTask(done_input, "num") > CheckTask(done_input, "cl_final"):
                                p()
                                print("That's more than the limit.")
                                continue
                            for t in task_list[actual_list]:
                                if t["id"] == done_input:
                                    t["num"] += num
                            break
                    p()
                    ShowTaskList()
                    print("Continue.")
                else:
                    p()
                    print("Please, type a valid number inside the index.")

        case "UNDO":
            print("---------------------------------------------------")
            p()
            print("Type the number of the task you want to undo.")
            print("Type [end] to stop.")
            p()
            
    
            while True:
                ShowTaskList()
                p()
                undo_input = get_input().strip().upper()
                parts = undo_input.split(maxsplit=1)
                if undo_input == "END":
                    print("---------------------------------------------------")
                    break
                if parts[0] == "Q":
                    if len(parts) != 2:
                        p()
                        print('Please, type the task number next time')
                        continue
                    task_id = CheckNum(parts[1])
                    if not task_id:
                        continue
                    task_found = next((t for t in task_list[actual_list] if t["id"] == task_id), None)

                    if not task_found:
                        print("This task does not exist")
                        continue
                    if task_found["type"] == "C":
                        if task_found["num"] != 0:
                            task_found["num"] = 0
                            p()
                            print("Continue.")
                            continue
                        else:
                            p()
                            print("This task is already empty.")
                            continue
                    else:
                        p()
                        print("The type of the task is not [C].")
                        continue

                undo_input = CheckNum(undo_input)
                if not undo_input:
                    continue

                if CheckTask(undo_input, "status") == "Unfinished":
                    p()
                    print("This task is not done.")
                    continue
                if 0 > undo_input > actual_id:
                    p()
                    print("Please, type a valid number inside the index.")
                    continue
                if CheckTask(undo_input, "num") == 0:
                    p()
                    print("This task is already empty.")
                
                if CheckTask(undo_input, "type") in ["S", "T"]:
                    EditTask(undo_input, "status", "Unfinished")
                elif CheckTask(undo_input, "type") == "C":
                    p()
                    print("How much you want to decrease?")
                    while True:
                        decrease_num = GetNum()
                        if (CheckTask(undo_input, "num") - decrease_num) < 0:
                            p()
                            print("That decrease to a negative number. If you want decrease all the task, type 0 and then type q (the number of the task)")
                            continue
                        if decrease_num < 0:
                            p()
                            print("Please, type a positive number to decrease.")
                            continue
                        for t in task_list[actual_list]:
                            if t["id"] == undo_input:
                                t["num"] -= decrease_num
                        break
                if NoTaskDone():
                    p()
                    print('All taks has been set to unfinished.')
                    print("---------------------------------------------------")
                    break
                print("Continue.")
                p()

        case "ADD":
            print("---------------------------------------------------")
            description = """Here you can add tasks to your list.
Types:
[S] Single: tasks that only need complete 1 time. Example: Feed the cat.
[C] CheckList: tasks that need complete various times. Example: Homeworks done.
[T] Timed: tasks that need time. Example: Reading time
It should be like: S Feed the cat
Type [end] to stop inputting tasks."""

            print(description)
            while True:
                task_input = get_input()

                task_ender = task_input.strip().upper()
                if task_ender == "END":
                    print("---------------------------------------------------")
                    break
                parts = task_input.split(maxsplit=1)
                
                parts[0] = parts[0].strip().upper()

                if len(parts) < 2:
                    p()
                    print("Please, input both the task type and the task name.")
                    continue

                if parts[0] not in ["C", "S", "T"]:
                    p()
                    print("Please, type a valid type")
                    continue
                
                if parts [0] == "C":
                    p()
                    print("Type how much checks (times it need be done):")
                    while True:
                        quantity = GetNum()
                        if quantity < 1:
                            print("That's not a valid number.")
                            p()
                            continue
                        AddTask("C", parts[1], quantity)
                        break
                elif parts[0] == "S":
                    AddTask("S", parts[1])
                elif parts[0] == "T":
                    time = GetTimer()
                    AddTask("T", parts[1], time)
                p()
                ShowTaskList()
                p()
                print("Task added.")
                p()
                continue   
            
        case "DEL":
            print("---------------------------------------------------")
            print("""Type the number of the task to delete it.  
Type [end] to stop.        
                  """) 
            
            ShowTaskList() 
            while True:
                p()
                del_input = get_input().strip().upper()

                if del_input == "END":
                    print("---------------------------------------------------")
                    break

                del_input = CheckNum(del_input)
                if not del_input:
                    continue
                if 0 > del_input > len(task_list[actual_list]) - 1:
                    print("Please, type a valid number inside the index.")
                    continue

                task_list[actual_list].pop(del_input - 1)
                actual_id -= 1
                for t in task_list[actual_list]:
                    if t["id"] > del_input:
                        t["id"] -= 1
                p()
                ShowTaskList()
                p()
                print("Task deleted")

                if task_list[actual_list] == []:
                    print ("You deleted all the tasks.")
                    break

        case "CLEAR":
            print("---------------------------------------------------")
            print("""Are you sure that you want to clear all the tasks?
If yes, type [y], else type anyting.
""")
            clear_input = get_input().strip().upper()

            if clear_input == "Y":
                task_list[actual_list] = []
                actual_id = 0
                p()
                print("All tasks have been deleted.")
                p()
                print("---------------------------------------------------")

        case "PROGRESS": 
            print("---------------------------------------------------")
            ShowTaskList()
            tasks_done = 0
            tasks_remaining = 0
            for t in task_list[actual_list]:
                if t["type"] in ["S", "T"]:
                    tasks_remaining += 1
                    if t["status"] == "Done":
                        tasks_done += 1
                elif t["type"] == "C":
                    tasks_remaining += t["cl_final"]
                    tasks_done += t["num"]



            progress = int(tasks_done / tasks_remaining * 100)
            p()
            if pb_type:
                print(f"[{'█'*progress + '░' * (100 - progress)}]")
            else:
                print(f"[{'█' * int(progress/10) + '░' * int(10 - progress / 10)}]")
            
            print(f"Progress: {progress}%")

            if progress == 100:
                print("Congratulations, you did all the tasks!")
            print("---------------------------------------------------")
