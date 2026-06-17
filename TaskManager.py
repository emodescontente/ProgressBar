import ProgressBar as pb
import time
import json

def MS(menu_name = '') -> str:
    """Stands for "Menu Switch", prints various '-' in the terminal followed by the name of the menu (defaults to none)"""
    print('-' * 100, f'\n{menu_name}')

def UserInput(exception = 'error', upper = True, inte = False, positive = True, error_message = '- Please, type something') -> str | int:
    """Returns the user input.
    Args:
        exception (str): Case where the function should return immediately case inputted.
        upper (bool): If the returned input is in uppercase or not. Defaults to True.
        inte (bool): If the returned input need to be a integer. Defaults to False.
        error_message (bool): The error message when the typed answer is not the expected."""
    

    if inte:
        while True:
            user_input =  input('-> ').strip()

            if user_input.upper() == exception.upper():
                return user_input.upper()
            
            try:
                user_input = int(user_input)
            except ValueError:
                print(error_message)
                continue
            if positive and user_input <= 0:
                print(error_message, sep='')
                continue

            return user_input

    while True:
        user_input = input('-> ').strip().upper() if upper else input('-> ').strip()
        if user_input == '':
            print('- Please, type something')
            continue
        break
        
    return user_input

def ShowTime(time):
    hours, rest = divmod(time, 3600)
    minutes, seconds = divmod(rest, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def GetTimer():
    time = 0
    print("\n- Ok, now, how much time the task need to be completed?")
    print("- Type the format of time followed by the number that you want to increment the timer on. The formats are the following:")
    print("[S]: seconds, [M]: minutes, [H]: hours.")
    print("- It should be like: [S 30] to increment 30 seconds on the timer, or S -10 if you want do decrement. Type [end] to stop.\n")
    while True:
        time_input = UserInput()
        if time_input =="END":
            break
        parts_timer = time_input.split(maxsplit=1)
        if len(parts_timer) != 2:
            print("\n- Please, type only the time format and the time.\n")
            continue
        if parts_timer [0] not in ["S","M","H"]:
            print("\n- Please, type a valid format.\n")
            continue
        try:
            parts_timer[1] = int(parts_timer[1])
        except ValueError:
            print("\n- Please, type a integer number.\n")
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
            print("\n- I Can't do a negative timer, sorry.\n")
            continue
        time += timer
        print(ShowTime(time))
        print("Continue:")
        continue
    return time

def AttentionMessage(message: str, ex = False):
    """Prints a highlighted message in the terminal.
    Args:
        message (str): The message to be printed in the terminal.
        ex (bool): If the message contains !"""
    
    character = '!' if ex else '*'
    
    print()
    print(character * 20)
    print(message)
    print(character * 20)
    
def ShowTasksInList():
    for index, task in enumerate(task_lists[actual_list].tasks, 1):
        print(index, task.ShowTask(True))

def CountdownTimer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_format, end='\r')
        time.sleep(1)
        seconds -= 1

def TakMessage(message: str) -> str:
    """Prints a Tak message in the terminal."""
    
    tak_message = {
        'greetings' : """- Welcome to Progress Bar Task Manager!

- My name is Tak and I'm your personal task assistant.

- Here what I can do for you:
Type [add] to enter your tasks. 
Type [del] to delete one. 
Type [done] to mark a task as done or unfinished. 
Type [edit] to edit a task name or complement. 
Type [progress] to check the tasks on the current list and the progress done. 
Type [clear] to delete all the tasks. 
Type [list] to see and change through task lists. 
Type [save] to export your tasks from this list or all lists. 
Type [load] to load tasks saved (json format). 
Type ctrl + z or ctrl + c to end the program.
""",


        'reminder': """
Type [add] to enter your tasks. 
Type [del] to delete one. 
Type [done] to mark a task as done or unfinished. 
Type [edit] to edit a task name or complement. 
Type [progress] to check the tasks on the current list and the progress done. 
Type [clear] to delete all the tasks. 
Type [list] to see and change through task lists. 
Type [save] to export your tasks from this list or all lists. 
Type [load] to load tasks saved (json format). 
Type [remind] to deactivate this message.
Type ctrl + z or ctrl + c to end the program.
""",


        'add s': """
- In this Menu, you can add tasks to your task list. See bellow how to do that:

- Tasks have 3 types:
[S] stands for "Single Task", a task that simply need be mark as complete. Example: Feed the cat.
[C] stands for "Checklist Task", a task that need a certain amount of Checks to be completed. Example: Homework's done (1/3).
[T] stands for "Timed Task", a task that need a certain amount of Time to be completed. Example: Reading time (30:00).

- Please, say to me the type of task you need to complete, typing one of the 3 letters above.
""",


        'add s S': """
- Great! Now, give a name to the task (you can edit it later in the Edit Menu):""",


        'add s C': """
- Ok, now, type the number of checks that the task need to be completed (that can be edited too in the Edit Menu).""",


        'add s T': """""",


        'add s Final': """
- You want to add more tasks? If so, type the type of the new task. Else, type [exit] to go back to the Main Menu""",


        'done s': """
- In this Menu, you can mark tasks as done. 
- You can also mark a done task as unfinished typing [-] in the start of the command.
- Please, select one of the task numbers to do one of the following things:
- Mark [S] tasks as done, mark checks in [C] tasks and run the timer in [T] tasks.
- Type [exit] to go back to the Main Menu.
""",


        'delete s': """
- In this menu you can delete a task from your list.
- Type the task number that you want to delete from the list.
- Type [exit] to go back to the Main Menu.
""",


        'edit s': """
- In this menu, you can edit a task name or complement.
- Type the task number that you want to edit from the list.
- Type [exit] to go back to the Main Menu.
""",


        'list s': """
- In this menu, you can see through your lists of tasks.
- Here what you can do, type:
[create] to create a new empty list.
[move] to change to a different list.
[del] to delete a list.
[edit] to edit a list name.
[exit] to go back to the main menu.
""",



    'save s': """
- In this menu, you can save your actually list or all of then.
- Type [S] to save your actually list in one file.
- Type [A] to save all the lists in one single file.
- Type [exit] to go back to the main menu.
"""
    }

    print(tak_message[message])


task_lists = [pb.TaskList('My Cool List', [])]
actual_list = 0


MS('MENU: MAIN')
TakMessage('greetings')

reminder = False

while True:
    print('\n- What you want to do?')

    if reminder:
        TakMessage('reminder')
        
    user_choice = UserInput()

    if user_choice not in ['ADD', 'LIST', 'LOAD', 'SAVE'] and task_lists[actual_list].total_tasks == 0:
        AttentionMessage('- You have no tasks in your list yet. Try start by typing [add]')
        continue

    match user_choice:
        case 'ADD':
            MS('MENU: ADD')
            TakMessage('add s')
            while True:
                add_choice = UserInput()
                match add_choice:
                    case 'S': 
                        TakMessage('add s S')
                        task_name = UserInput(upper=False)
                        task_lists[actual_list].AddTask(pb.Task('S', task_name, False))
                        AttentionMessage(f'- The Single Task "{task_name}" was added to the list.')

                    case 'C':
                        TakMessage('add s S')
                        task_name = UserInput(upper=False)
                        TakMessage('add s C')
                        task_complement = UserInput(inte=True, error_message="\n- Please, type a positive integer number")
                        task_lists[actual_list].AddTask(pb.Task('C', task_name, task_complement))
                        AttentionMessage(f'- The Checklist Task "{task_name}" was added to the task list.')
                    
                    case 'T':
                        TakMessage('add s S')
                        task_name = UserInput(upper=False)
                        task_complement = GetTimer()
                        task_lists[actual_list].AddTask(pb.Task('T', task_name, task_complement))
                        AttentionMessage(f'- The Timed Task "{task_name}" was added to the task list.')


                    case 'EXIT':
                        MS('MENU: MAIN')
                        break

                    case _:
                        AttentionMessage("- I don't recognize this type. Please, choice something between: [S], [C] or [T]", True)
                        print()
                        continue

                TakMessage('add s Final')

        case 'DEL':
            MS('MENU: DELETE')
            TakMessage('delete s')
            ShowTasksInList()

            while True:
                print()
                index = UserInput('exit', inte=True)

                if index == 'EXIT':
                    MS('MENU: MAIN')
                    break

                if index > task_lists[actual_list].total_tasks or index < 1:
                    print('\n- Please, choice a task number inside the list.')
                    continue

                deleted_task = task_lists[actual_list].tasks[index - 1]
                task_lists[actual_list].DeleteTask(index - 1)

                AttentionMessage(f'- The task {deleted_task.name} has been deleted')
                ShowTasksInList()

        case 'DONE':
            MS('MENU: DONE')
            TakMessage('done s')
            ShowTasksInList()

            while True:
                print()
                done_choice = UserInput(upper=True).split()

                if done_choice[0] == 'EXIT':
                    MS('MENU: MAIN')
                    break
                
                if done_choice[0] != '-':
                    try:
                        index = int(done_choice[0])
                    except ValueError:
                        AttentionMessage('Please, type a task number.')
                        continue

                    if index > task_lists[actual_list].total_tasks or index < 1:
                        print('\n- Please, choice a task number inside the list.')
                        continue

                    task = task_lists[actual_list].tasks[index - 1]

                    if task.done:
                        AttentionMessage('That task is already set as done.', True)
                        continue

                    match task.type:
                        case 'S':
                            task.SetTask(True)
                            print()
                            AttentionMessage(f'- The task: {task.name} was marked as done.')
                            print()
                            ShowTasksInList()
                        case 'C':
                            print('\n- Ok, now, type the number of checks you want to mark in')
                            while True:
                                checks = UserInput(positive=True, inte=True, error_message='- Please, type a positive integer number.')
                                if task.checks + checks > task.complement:
                                    AttentionMessage('- That extrapolates the max number of checks to mark.', True)
                                    print()
                                    continue
                                task.SetTask(task.checks + checks)
                                break
                            print()
                            AttentionMessage(f'- The task: {task.name} now has {task.checks}/{task.complement} checks.')
                            print()
                            ShowTasksInList()
                        case 'T':
                            AttentionMessage('''- Are you sure that you want start this timer? Until the end of it, you will be not able to use the program.
    Type [Y] if so, else type anything.''')
                            decision = UserInput()
                            if decision == 'Y':
                                CountdownTimer(task.complement)
                                task.SetTask(True)
                                print()
                                AttentionMessage(f'- The task: {task.name} was marked as done.')

                            print()
                            ShowTasksInList()

                else:

                    try:
                        index = int(done_choice[1])
                    except ValueError:
                        AttentionMessage('Please, type a task number.')
                        continue

                    if index > task_lists[actual_list].total_tasks or index < 1:
                        print('\n- Please, choice a task number inside the list.')
                        continue

                    task = task_lists[actual_list].tasks[index - 1]

                    if not task.done:
                        AttentionMessage('That task is already set as unfinished.', True)
                        continue

                    match task.type:
                        case 'C':
                            print()
                            print('- Ok, now, type the number of checks you want to remove')
                            while True:
                                checks = UserInput(positive=True, inte=True, error_message='- Please, type a positive integer number.')
                                if task.checks - checks < 0:
                                    AttentionMessage('- The checks number cannot go bellow 0.', True)
                                    print()
                                    continue
                                task.SetTask(task.checks - checks)
                                break
                            print()
                            AttentionMessage(f'- The task: {task.name} now has {task.checks}/{task.complement} checks.')
                            print()
                            ShowTasksInList()
                        case _:
                            task.SetTask(False)
                            print()
                            AttentionMessage(f'- The task: {task.name} was marked as unfinished.')
                            print()
                            ShowTasksInList()

        case 'EDIT':
            MS('MENU: EDIT')
            TakMessage('edit s')
            ShowTasksInList()

            while True:
                print()
                index = UserInput('exit', inte=True)

                if index == 'EXIT':
                    MS('MENU: MAIN')
                    break

                if index > task_lists[actual_list].total_tasks or index < 1:
                    print()
                    print('- Please, choice a task number inside the list.')
                    continue



                while True:
                    print('\n- What you want to change?')
                    print('If its the name, type [N]. If its the complement, type [C].')
                    print()
                    user_choice = UserInput()

                    if user_choice == 'N':
                        print(f'\n- Ok, what name you want to set for the task: {task_lists[actual_list].tasks[index - 1].name}?')
                        task_lists[actual_list].tasks[index - 1].name = UserInput(upper=False)
                        AttentionMessage('- The task has been renamed.')
                        print()
                        ShowTasksInList()
                        break
                    if user_choice == 'C':
                        task = task_lists[actual_list].tasks[index - 1]
                        match task.type:
                            case 'S':
                                AttentionMessage('- Single tasks does not have complements.', True)
                                ShowTasksInList()
                                break
                            case 'C':
                                print('\n- How much checks the task must have now?')
                                checks = UserInput(inte=True, positive=True, error_message='- Please, type a positive integer.')

                                if checks < task.checks:
                                    task.complement = checks
                                    task.SetTask(checks)
                                else:
                                    task.complement = checks
                                ShowTasksInList()
                                break
                            case 'T':
                                complement = GetTimer()
                                task.complement = complement
                                ShowTasksInList()
                                break

        case 'PROGRESS':
            print()
            ShowTasksInList()
            print()
            print(task_lists[actual_list].ProgressBar())

        case 'CLEAR':
            AttentionMessage('''- Are you sure that you want to delete all tasks from the actual list?
- If so, type [Y]. Else type anything''', True)
            user_choice = UserInput()

            if user_choice == 'Y':
                task_lists[actual_list].ClearList()

                AttentionMessage('All the tasks from this list has been deleted.')

        case 'LIST':
            MS('MENU: LISTS')
            TakMessage('list s')
            def ShowList():
                for index, lists in enumerate(task_lists, 1):
                    print()
                    print(f"    {'*' if index - 1 == actual_list else ''}{index} ||| {lists.name}:")
                    for number, task in enumerate(task_lists[index - 1].tasks, 1):
                        print(number, task.ShowTask(True))
            ShowList()

            while True:
                print()
                user_choice = UserInput()

                if user_choice == 'DEL' and len(task_lists) == 1:
                    AttentionMessage("- You can't delete the only list you have.", True)
                    continue

                match user_choice:
                    case 'EXIT':
                        MS('MENU: MAIN')
                        break
                    case 'CREATE':
                        print('\n- Ok, what the name you want to the new list have?')
                        name = UserInput(upper=False)
                        task_lists.append(pb.TaskList(name, []))
                        AttentionMessage(f'The task list {name} was created.')
                        ShowList()
                    case 'DEL':
                        print('\n- Type the list number that you will to delete or 0 to cancel.')
                        while True:
                            delete_index = UserInput(inte=True, positive=False)
                            if 0 > delete_index > len(task_lists):
                                print('- Please, type a valid list number.')
                                continue
                            
                            if delete_index == 0:
                                print('\n- Fine, you can type other command now')
                                ShowList()
                                break
                            
                            actual_list = 0
                            
                            task_lists.pop(delete_index - 1)
                            AttentionMessage('The list has been deleted.')
                            ShowList()
                            break
                    case 'MOVE':
                        print('\n- Ok, type the number of the list you want to change.')
                        while True:
                            index = UserInput(inte=True, positive=True)
                            if 1 > index > len(task_lists):
                                print('- Please, type a valid list number.')
                                continue
                            actual_list = index -1
                            ShowList()
                            break
                    case 'EDIT':
                        print('\n- Ok, type the number of the list you want to edit.')
                        while True:
                            index = UserInput(inte=True, positive=True)
                            if 1 > index > len(task_lists):
                                print('- Please, type a valid list number.')
                                continue
                            print('- What should be the new name?')
                            name = UserInput(upper=False)
                            AttentionMessage('- The list has been renamed.')
                            ShowList()
                            break
                    case _:
                        AttentionMessage("I don't recognize this command.", True)

        case 'SAVE':
            MS('MENU: SAVE')
            TakMessage('save s')
            
            user_choice = UserInput()

            match user_choice:
                case 'S':
                    with open(f'{task_lists[actual_list].name}.json', 'w') as f:
                        task_info = []
                        for task in task_lists[actual_list].tasks:
                            if task.type != 'C':
                                task_info.append({'name': task.name, 'type': task.type, 'complement': task.complement, 'done': task.done})
                            else:
                                task_info.append({'name': task.name, 'type': task.type, 'complement': task.complement, 'checks': task.checks, 'done': task.done})    
                        save = {
                            'list_name': task_lists[actual_list].name,
                            'tasks': task_info
                            }
                        
                        json.dump(save, f,  indent=4)
                        
                case 'A':
                    print('\n- Give a name for the file.')
                    name = UserInput(upper=False)
                    with open(f'{name}.json', 'w') as f:
                        save = []
                        for lists in task_lists:
                            task_info = []
                            for task in lists.tasks:
                                if task.type != 'C':
                                    task_info.append({'name': task.name, 'type': task.type, 'complement': task.complement, 'done': task.done})
                                else:
                                    task_info.append({'name': task.name, 'type': task.type, 'complement': task.complement, 'checks': task.checks, 'done': task.done})  

                            save.append({
                                'list_name': lists.name,
                                'tasks': task_info
                                })
                        
                        json.dump(save, f,  indent=4)

                
            MS('MENU: MAIN')
            
        case 'LOAD':
            MS('MENU: LOAD')
            print('\n- Please, copy the patch for the JSON file containing the list to load.')
            patch = UserInput(upper=False)

            try:
                with open(patch) as f:
                    data = json.load(f)
                    
                    if type(data) == list:

                        for lists in data:
                            tasks = []

                            for index, task in enumerate(lists['tasks']):
                                tasks.append(pb.Task(task['type'], task['name'], task['complement']))

                                if task['type'] == 'C':
                                    tasks[index].SetTask(task['checks'])
                                else:
                                    tasks[index].SetTask(task['done'])
                            task_lists.append(pb.TaskList(lists['list_name'], tasks))
                    else:

                        tasks = []

                        for index, task in enumerate(data['tasks']):
                            tasks.append(pb.Task(task['type'], task['name'], task['complement']))

                            if task['type'] == 'C':
                                tasks[index].SetTask(task['checks'])
                            else:
                                tasks[index].SetTask(task['done'])
                        task_lists.append(pb.TaskList(data['list_name'], tasks))

            except FileNotFoundError:
                AttentionMessage('That file is not valid.', True)
            except json.decoder.JSONDecodeError:
                AttentionMessage('That file is not valid.', True)

            MS('MENU: MAIN')

        case 'HELP':
            TakMessage('reminder')

        case 'REMIND':
            reminder = not reminder

        case _:
            AttentionMessage("""- I don't recognize this command. If you need help, type [help] to see your options.
- If you want a reminder of the commands every time you leave a Menu, type [remind].""", True)