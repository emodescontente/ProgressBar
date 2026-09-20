import json
import time

import ProgressBar as pb
import shlex


def ShowTime(time):
    hours, rest = divmod(time, 3600)
    minutes, seconds = divmod(rest, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def AttentionMessage(message: str, ex=False):
    """Prints a highlighted message in the terminal.
    Args:
        message (str): The message to be printed in the terminal.
        ex (bool): If the message contains !"""

    character = "!" if ex else "*"

    print()
    print(character * 20)
    print(message)
    print(character * 20)


def ShowTasksInList():
    for list_index, lst in enumerate(task_lists, 1):
        marker = '*' if (list_index - 1) == actual_list else ''
        print(f"\n    {marker}{list_index} ||| {lst.name}:")
        for task_index, task in enumerate(lst.tasks, 1):
            print(f"{task_index} {task.ShowTask(True)}")


def CountdownTimer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_format = "{:02d}:{:02d}".format(mins, secs)
        print(timer_format, end="\r")
        time.sleep(1)
        seconds -= 1


def TakMessage(message: str) -> str:
    """Prints a Tak message in the terminal."""

    tak_message = {
        "greetings": """- Welcome to Progress Bar Task Manager!

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
        "reminder": """
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
        "add s": """
- In this Menu, you can add tasks to your task list. See bellow how to do that:

- Tasks have 3 types:
[S] stands for "Single Task", a task that simply need be mark as complete. Example: Feed the cat.
[C] stands for "Checklist Task", a task that need a certain amount of Checks to be completed. Example: Homework's done (1/3).
[T] stands for "Timed Task", a task that need a certain amount of Time to be completed. Example: Reading time (30:00).

- Please, say to me the type of task you need to complete, typing one of the 3 letters above.
""",
        "add s S": """
- Great! Now, give a name to the task (you can edit it later in the Edit Menu):""",
        "add s C": """
- Ok, now, type the number of checks that the task need to be completed (that can be edited too in the Edit Menu).""",
        "add s T": """""",
        "add s Final": """
- You want to add more tasks? If so, type the type of the new task. Else, type [exit] to go back to the Main Menu""",
        "done s": """
- In this Menu, you can mark tasks as done. 
- You can also mark a done task as unfinished typing [-] in the start of the command.
- Please, select one of the task numbers to do one of the following things:
- Mark [S] tasks as done, mark checks in [C] tasks and run the timer in [T] tasks.
- Type [exit] to go back to the Main Menu.
""",
        "delete s": """
- In this menu you can delete a task from your list.
- Type the task number that you want to delete from the list.
- Type [exit] to go back to the Main Menu.
""",
        "edit s": """
- In this menu, you can edit a task name or complement.
- Type the task number that you want to edit from the list.
- Type [exit] to go back to the Main Menu.
""",
        "list s": """
- In this menu, you can see through your lists of tasks.
- Here what you can do, type:
[create] to create a new empty list.
[move] to change to a different list.
[del] to delete a list.
[edit] to edit a list name.
[exit] to go back to the main menu.
""",
        "save s": """
- In this menu, you can save your actually list or all of then.
- Type [S] to save your actually list in one file.
- Type [A] to save all the lists in one single file.
- Type [exit] to go back to the main menu.
""",
    }

    print(tak_message[message])


task_lists = [pb.TaskList("My Cool List", [])]
actual_list = 0


def seconds_from_parts(parts: list[int]) -> int:
    # parts expected as [sec, min, hours] but may be shorter
    s = 0
    try:
        sec = int(parts[0]) if len(parts) > 0 else 0
    except ValueError:
        sec = 0
    try:
        minute = int(parts[1]) if len(parts) > 1 else 0
    except ValueError:
        minute = 0
    try:
        hour = int(parts[2]) if len(parts) > 2 else 0
    except ValueError:
        hour = 0
    s += sec
    s += minute * 60
    s += hour * 3600
    return s


TakMessage("greetings")

reminder = False


def print_help(cmd: str | None = None):
    common = {
        "add": "add <type> <name> [args]\nTypes: s (single), c (checklist <checks>), t (timed <sec> [min] [hours])\nExamples: add s 'Buy milk' ; add c 'Steps' 3 ; add t 'Read' 20 30 1",
        "del": "del <index> — delete task by number. Example: del 2",
        "done": "done <index> [checks] — mark task done; for checklist provide number of checks to add. Use prefix '-' to unmark: done - <index> [checks]",
        "edit": "edit <index> name <new name> | edit <index> complement <value> — edit task name or complement",
        "progress": "progress — show current list progress bar and tasks",
        "clear": "clear — delete all tasks from current list (asks confirmation)",
        "list": "list see|create <name>|del <index>|move <index>|edit <index> <newname> — list management. Example: list see",
        "save": "save s — save current list; save a <filename> — save all lists to file",
        "load": "load <path> — load a saved json file",
        "help": "help <command> — show help for a command",
        "remind": "remind — toggle reminder messages",
    }
    if cmd is None:
        print("\nAvailable commands:")
        for k in [
            "add",
            "del",
            "done",
            "edit",
            "progress",
            "clear",
            "list",
            "save",
            "load",
            "help",
            "remind",
        ]:
            print("-", k)
        return
    print("\nHelp for", cmd)
    print(common.get(cmd, "No help available for this command"))


while True:
    try:
        raw = input("\n-> ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
        break
    if not raw:
        continue
    parts = shlex.split(raw)
    if not parts:
        continue
    cmd = parts[0].lower()

    if cmd == "help":
        if len(parts) > 1:
            print_help(parts[1].lower())
        else:
            print_help()
        continue

    if cmd == "add":
        if len(parts) > 1 and parts[1].lower() == "help":
            print_help("add")
            continue
        if len(parts) < 3:
            AttentionMessage("- Usage: add <type> <name> [args]")
            continue
        typ = parts[1].upper()
        name = parts[2]
        if typ == "S":
            task_lists[actual_list].AddTask(pb.Task("S", name, False))
            AttentionMessage(f'- The Single Task "{name}" was added to the list.')
        elif typ == "C":
            if len(parts) < 4:
                AttentionMessage(
                    '- Checklist requires number of checks. Usage: add c "name" <checks>'
                )
                continue
            try:
                checks = int(parts[3])
            except ValueError:
                AttentionMessage("- Checks must be an integer.")
                continue
            task_lists[actual_list].AddTask(pb.Task("C", name, checks))
            AttentionMessage(
                f'- The Checklist Task "{name}" was added to the task list.'
            )
        elif typ == "T":
            # remaining parts after name are numeric time parts
            time_parts = []
            for p in parts[3:]:
                try:
                    time_parts.append(int(p))
                except ValueError:
                    time_parts.append(0)
            seconds = seconds_from_parts(time_parts)
            task_lists[actual_list].AddTask(pb.Task("T", name, seconds))
            AttentionMessage(
                f'- The Timed Task "{name}" was added to the task list ({ShowTime(seconds)}).'
            )
        else:
            AttentionMessage("- Unknown type. Use s, c or t.", True)
        continue

    if cmd == "del":
        if len(parts) > 1 and parts[1].lower() == "help":
            print_help("del")
            continue
        if len(parts) < 2:
            AttentionMessage("- Usage: del <index>")
            continue
        try:
            idx = int(parts[1])
        except ValueError:
            AttentionMessage("- Index must be integer.")
            continue
        if idx < 1 or idx > task_lists[actual_list].total_tasks:
            AttentionMessage("- Invalid task index.")
            continue
        deleted = task_lists[actual_list].tasks.pop(idx - 1)
        AttentionMessage(f"- The task {deleted.name} has been deleted")
        continue

    if cmd == "done":
        if len(parts) > 1 and parts[1].lower() == "help":
            print_help("done")
            continue
        if len(parts) < 2:
            AttentionMessage("- Usage: done <index> or done - <index>")
            continue
        unmark = parts[1] == "-"
        if unmark:
            if len(parts) < 3:
                AttentionMessage("- Usage: done - <index> [checks]")
                continue
            try:
                idx = int(parts[2])
            except ValueError:
                AttentionMessage("- Index must be integer.")
                continue
            if idx < 1 or idx > len(task_lists[actual_list].tasks):
                AttentionMessage("- Invalid task index.")
                continue
            task = task_lists[actual_list].tasks[idx - 1]
            if task.type == "C":
                checks = int(parts[3]) if len(parts) > 3 else 1
                if task.checks - checks < 0:
                    task.SetTask(0)
                    AttentionMessage(f"- The task: {task.name} had all checks removed.")
                    continue
                else:
                    task.SetTask(task.checks - checks)
                AttentionMessage(f"- The task: {task.name} had {checks} checks removed and now has {task.checks}/{task.complement} checks.")
            else:
                task.SetTask(False)
                AttentionMessage(f"- The task: {task.name} was marked as unfinished.")
        else:
            try:
                idx = int(parts[1])
            except ValueError:
                AttentionMessage("- Index must be integer.")
                continue
            if idx < 1 or idx > len(task_lists[actual_list].tasks):
                AttentionMessage("- Invalid task index.")
                continue
            task = task_lists[actual_list].tasks[idx - 1]
            if task.type == "C":
                checks = int(parts[2]) if len(parts) > 2 else 1
                if checks < 0:
                    AttentionMessage("- Checks can't be negative. - Usage: done - <index> [checks]")
                    continue
                new_checks = task.complement if checks > task.complement else task.checks + checks
                task.SetTask(new_checks)
                AttentionMessage(
                    f"- The task: {task.name} now has {task.checks}/{task.complement} checks."
                )
            elif task.type == "T":
                AttentionMessage(
                    """- Starting timer. You will not be able to use the program until it ends."""
                )
                CountdownTimer(task.complement)
                task.SetTask(True)
                AttentionMessage(f"- The task: {task.name} was marked as done.")
            else:
                task.SetTask(True)
                AttentionMessage(f"- The task: {task.name} was marked as done.")
        continue

    if cmd == "edit":
        if len(parts) > 1 and parts[1].lower() == "help":
            print_help("edit")
            continue
        if len(parts) < 4:
            AttentionMessage(
                "- Usage: edit <index> name <new name> | edit <index> complement <value>"
            )
            continue
        try:
            idx = int(parts[1])
        except ValueError:
            AttentionMessage("- Index must be integer.")
            continue
        if idx < 1 or idx > len(task_lists[actual_list].tasks):
            AttentionMessage("- Invalid task index.")
            continue
        field = parts[2].lower()
        if field == "name":
            newname = parts[3]
            task_lists[actual_list].tasks[idx - 1].name = newname
            AttentionMessage("- The task has been renamed.")
        elif field == "complement":
            val = parts[3]
            task = task_lists[actual_list].tasks[idx - 1]
            if task.type == "S":
                AttentionMessage("- Single tasks does not have complements.", True)
                continue
            if task.type == "C":
                checks = int(parts[2]) if len(parts) > 2 else 1
                # clamp addition so checks don't exceed complement
                if task.complement < checks:
                    new_checks = task.complement
                else:
                    new_checks = task.checks + checks
                task.SetTask(new_checks)
                AttentionMessage(
                    f"- The task: {task.name} now has {task.checks}/{task.complement} checks."
                )
                task.complement = checks
                if task.checks > checks:
                    task.SetTask(checks)
                AttentionMessage("- Checklist updated.")
            elif task.type == "T":
                # complement provided as seconds
                try:
                    secs = int(val)
                except ValueError:
                    AttentionMessage(
                        "- Complement must be integer seconds for timed task."
                    )
                    continue
                task.complement = secs
                AttentionMessage("- Timed task updated.")
        continue

    if cmd == "progress":
        print()
        ShowTasksInList()
        print()
        print(task_lists[actual_list].ProgressBar())
        continue

    if cmd == "clear":
        if len(parts) > 1 and parts[1].lower() == "help":
            print_help("clear")
            continue
        AttentionMessage(
            """- Are you sure that you want to delete all tasks from the actual list? Type Y to confirm.""",
            True,
        )
        ans = input("-> ").strip().upper()
        if ans == "Y":
            task_lists[actual_list].ClearList()
            AttentionMessage("All the tasks from this list has been deleted.")
        continue

    if cmd == "list":
        if len(parts) > 1 and parts[1].lower() == "help":
            print_help("list")
            continue
        sub = parts[1].lower() if len(parts) > 1 else ""
        if sub == "see":
            ShowTasksInList()
        elif sub == "create" and len(parts) > 2:
            name = parts[2]
            task_lists.append(pb.TaskList(name, []))
            AttentionMessage(f"The task list {name} was created.")
        elif sub == "del" and len(parts) > 2:
            try:
                idx = int(parts[2])
            except ValueError:
                AttentionMessage("- Index must be integer.")
                continue
            if idx < 1 or idx > len(task_lists):
                AttentionMessage("- Invalid list index.")
                continue
            task_lists.pop(idx - 1)
            actual_list = 0
            AttentionMessage("The list has been deleted.")
        elif sub == "move" and len(parts) > 2:
            try:
                idx = int(parts[2])
            except ValueError:
                AttentionMessage("- Index must be integer.")
                continue
            if idx < 1 or idx > len(task_lists):
                AttentionMessage("- Invalid list index.")
                continue
            actual_list = idx - 1
            ShowTasksInList()
        elif sub == "edit" and len(parts) > 3:
            try:
                idx = int(parts[2])
            except ValueError:
                AttentionMessage("- Index must be integer.")
                continue
            name = parts[3]
            task_lists[idx - 1].name = name
            AttentionMessage("- The list has been renamed.")
        else:
            AttentionMessage('- Unknown list command. Use "list help" to see options.')
        continue

    if cmd == "save":
        if len(parts) > 1 and parts[1].lower() == "help":
            print_help("save")
            continue
        sub = parts[1].lower() if len(parts) > 1 else "s"
        if sub == "s":
            with open(f"{task_lists[actual_list].name}.json", "w") as f:
                task_info = []
                for task in task_lists[actual_list].tasks:
                    if task.type != "C":
                        task_info.append(
                            {
                                "name": task.name,
                                "type": task.type,
                                "complement": task.complement,
                                "done": task.done,
                            }
                        )
                    else:
                        task_info.append(
                            {
                                "name": task.name,
                                "type": task.type,
                                "complement": task.complement,
                                "checks": task.checks,
                                "done": task.done,
                            }
                        )
                save = {"list_name": task_lists[actual_list].name, "tasks": task_info}
                json.dump(save, f, indent=4)
        elif sub == "a":
            name = parts[2] if len(parts) > 2 else "all_lists"
            with open(f"{name}.json", "w") as f:
                save = []
                for lst in task_lists:
                    task_info = []
                    for task in lst.tasks:
                        if task.type != "C":
                            task_info.append(
                                {
                                    "name": task.name,
                                    "type": task.type,
                                    "complement": task.complement,
                                    "done": task.done,
                                }
                            )
                        else:
                            task_info.append(
                                {
                                    "name": task.name,
                                    "type": task.type,
                                    "complement": task.complement,
                                    "checks": task.checks,
                                    "done": task.done,
                                }
                            )
                    save.append({"list_name": lst.name, "tasks": task_info})
                json.dump(save, f, indent=4)
        else:
            AttentionMessage('- Unknown save option. Use "save help"')
        continue

    if cmd == "load":
        if len(parts) > 1 and parts[1].lower() == "help":
            print_help("load")
            continue
        if len(parts) < 2:
            AttentionMessage("- Usage: load <path>")
            continue
        patch = parts[1]
        try:
            with open(patch) as f:
                data = json.load(f)
                if isinstance(data, list):
                    for lists in data:
                        tasks = []
                        for index, task in enumerate(lists["tasks"]):
                            tasks.append(
                                pb.Task(task["type"], task["name"], task["complement"])
                            )
                            if task["type"] == "C":
                                tasks[index].SetTask(task["checks"])
                            else:
                                tasks[index].SetTask(task["done"])
                        task_lists.append(pb.TaskList(lists["list_name"], tasks))
                else:
                    tasks = []
                    for index, task in enumerate(data["tasks"]):
                        tasks.append(
                            pb.Task(task["type"], task["name"], task["complement"])
                        )
                        if task["type"] == "C":
                            tasks[index].SetTask(task["checks"])
                        else:
                            tasks[index].SetTask(task["done"])
                    task_lists.append(pb.TaskList(data["list_name"], tasks))
        except FileNotFoundError:
            AttentionMessage("That file is not valid.", True)
        except json.decoder.JSONDecodeError:
            AttentionMessage("That file is not valid.", True)
        continue

    if cmd == "remind":
        reminder = not reminder
        AttentionMessage(f"Reminder set to {reminder}")
        continue

    AttentionMessage(
        "- I don't recognize this command. If you need help, type [help] to see your options.",
        True,
    )
