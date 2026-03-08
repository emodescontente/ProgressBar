from timer import countdown_timer

def get_input():
    while True:
        valor = input("> ")
        if valor != "":
            return valor
        print("Please, type something.")

def p():
    print("")
    return 0

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


tasks_done = [1, 2, 3]
tasks = ["S Cavalo", "S poney", "S Unicorno"]
print("""
Type [help] if you need a reminder of the commands.""")

while True:
    p()
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

    if user_input == "UNDO" and tasks_done == []:
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
Type [end] to stop.""")

            for num, task in enumerate(tasks, 1):
                status = "Done" if num in tasks_done else "Unfinished"
                print(f"{num}. {task}: {status}")

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

                if done_input in tasks_done:
                    p()
                    print("This task is already done.")
                    continue

                if 0 < done_input <= len(tasks):
                    tasks_done.append(done_input)

                    for num, task in enumerate(tasks, 1):
                        status = "Done" if num in tasks_done else "Unfinished"
                        print(f"{num}. {task}: {status}")

                    p()
                    print("Continue:")

                else:
                    p()
                    print("Please, type a valid number inside the tasks index.")

        case "UNDO":
            while True:
                p()
                print("Type the number of the task you want to undo.")
                print("Type [end] to stop.")
                for num, task in enumerate(tasks, 1):
                    status = "Done" if num in tasks_done else "Unfinished"
                    print(f"{num}. {task}: {status}")

                undo_input = get_input().strip().upper()

                if undo_input == "END":
                    break

                try:
                    undo_input = int(undo_input)
                except ValueError:
                    p()
                    print("That's not a number.")
                    continue
                if undo_input not in tasks_done:
                    p()
                    print("That task is not done.")
                    continue
                if 0 > undo_input > max(tasks_done):
                    p()
                    print("Please, type a valid number inside the index.")
                    continue

                print(tasks_done)

                for num, task_done in enumerate(tasks_done):
                    if task_done == undo_input:
                        tasks_done.pop(num)

                print(tasks_done)

        case "ADD":
            description = """
Please, input your task type and the task.
Types:
[S] Single: tasks that only need complete 1 time. Example: Feed the cat.
[C] CheckList: tasks that need complete various times. Example: Homeworks done.
[T] Timed: tasks that need time. Example: Reading time
It should be like: S Feed the cat
Type [end] to stop inputing tasks.
        """

            print(description)


            while True:
                task_input = get_input()
                p()

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

                tasks.append(parts[0] + " " + parts[1])
                for num, i in enumerate(tasks, 1):
                    print(f"{num}. {i}")
                p()
                print("Continue:")
                p()
                continue   
            
        case "DEL":
            print("""  
Type the number of the task to delete it.  
Type [end] to stop.        
                  """) 
            del_input = "" 
            while True:
                for num, task in enumerate(tasks, 1):  
                    status = "Done" if num in tasks_done else "Unfinished" 
                    print(f"{num}. {task}: {status}")  
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

                for i, done_reduce in enumerate(tasks_done):
                    if done_reduce > del_input:
                        tasks_done[i] = tasks_done[i] - 1
                    elif done_reduce == del_input:
                        tasks_done.pop(i)

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
                p()
                print("All tasks has been deleted.")
                p()

        case "PROGRESS": 

                p()

                progress = int((len(tasks_done) / len(tasks)) * 100)

                for num, task in enumerate(tasks, 1):
                    status = "Done" if num in tasks_done else "Unfinished"
                    print(f"{num}. {task}: {status}")

                print(f"Progress: {progress}%")

                if progress == 100:
                    print("Congratulations, you did all the tasks!")