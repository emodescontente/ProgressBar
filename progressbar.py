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
Type [add] to enter your tasks (1 per time).
Type [del] to delete one.
Type [done] and the task number when you complete one task (done a timed task will lead you into a timer).
Type [undo] to undo a task.
Type [progress] when you want to check the tasks and the progress done.
Type [clear] to delete all the tasks.
Type [close] to end program.
""")
command_list = ["ADD", "DEL", "DONE", "PROGRESS", "CLOSE", "HELP", "CLEAR", "UNDO"]

user_input = ""
tasks_done = []
tasks = []

while user_input != "CLOSE":


    print("""
Type [help] if you need a reminder of the commands.
          """)
    
    user_input = input("> ").strip().upper()

    while user_input not in command_list or (user_input not in ["ADD", "HELP", "CLOSE"] and tasks == []):
        if user_input not in command_list:
            print("Please, type a valid command.")
            user_input = (input("> ").strip().upper())

        if user_input not in ["ADD", "HELP", "END"]:
            print("Try start by adding tasks with [add]")
            user_input = input("> ").strip().upper()


    match user_input:
        case "HELP":
            print("""
                  
Type [add] to enter your tasks (1 per time).
Type [del] to delete one.
Type [done] and the task number when you complete one task (done a timed task will lead you into a timer).
Type [undo] to undo a task.
Type [progress] when you want to check the progress done.
Type [close] to end the program.
                  """)
        case "DONE":

            print("""
Type the number of the task you want to mark as done.
Type [end] to stop.""")

            done_input = ""
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

            # Recolhe o tipo de task
            task_input = get_input()

            num = 0
            while task_input != "end":

                # Divide no primeiro espaço que encontrar num array
                parts = task_input.split(maxsplit=1)
                
                parts[0] = parts[0].strip().upper()

                # Previnir qualquer erro
                while len(parts) < 2 or parts[0] not in ["C", "S", "T"]:

                    if len(parts) < 2:
                        print("Please, input both the task type and the task name.")

                        task_input = get_input()

                        parts = task_input.split(maxsplit=1)

                        parts[0] = parts[0].strip().upper()

                    if parts[0] not in ["C", "S", "T"]:
                        print("Please, input a valid type (only the type)")
                        parts[0] = (input("> ")).strip().upper()

                tasks.append(task_input)
                for i in tasks:
                    num +=1 
                    p()
                    print(f"{num}. {i}")
                p()
                print("Continue:")
                p()
                task_input = get_input()
                num = 0

        case "DEL":
            num = 0
            print("""
Type the number of the task to delete it.
Type [end] to stop.                
                  """)
            del_input = ""
            while del_input != "END":
                for task in tasks:
                    num += 1
                    print(f"{num}. {task}")
                del_input = get_input().strip().upper()
                del_input = int(del_input)
                tasks.pop(del_input - 1)
                num = 0

                if tasks == []:
                    print ("You deleted all thetasks.")
                    del_input = "end"

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

                num = 0
                for remaining in range(len(tasks)):
                    num += 1    
                    print(f"{num}. {tasks[remaining]}")

                print(f"Progress: {progress}%")

                if progress == 100:
                    print("Congratulations, you did all the tasks!")