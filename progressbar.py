from timer import countdown_timer

# ritual de início
print("Hello, world!")

# Agora, começo do projeto PROGRESS BAR, HELL YEAH1!1!!!1111!1
print("""Wellcome to Progress Bar!
Type [add] to enter your tasks (1 per time).
Type [del] to delete one.
Type [done] and the task number when you complete one task (done a timed task will lead you into a timer).
Type [progress] when you want to check the progress done.
Type [help] to a reminder of the comamnds.
Type [end] to end program.
""")

command_list = ["ADD", "DEL", "DONE", "PROGRESS", "HELP", "END"]


user_input = input("> ").strip().upper()

while user_input not in command_list or user_input not in ["ADD", "HELP", "END"]:
    if user_input not in command_list:
        print("Please, type a valid command.")
        user_input = (input("> ").strip().upper())

    if user_input not in ["ADD", "HELP", "END"]:
        print("Try start by adding tasks with [add]")
        user_input = input("> ").strip().upper()

tasks = []
task_type = ""

while user_input != "END":
    match user_input:
        case "HELP":
            print("""
Type [add] to enter your tasks (1 per time).
Type [del] to delete one.
Type [done] and the task number when you complete one task (done a timed task will lead you into a timer).
Type [progress] when you want to check the progress done.
Type [help] to a reminder of the comamnds.
    """)
            user_input = input("> ")

        case "ADD":
            description = """
Please, input your task type andthe task.
Types:
[S] Single: tasks that only need complete 1 time. Example: Feed the cat.
[C] CheckList: tasks that need complete various times. Example: Homeworks done.
[T] Timed: tasks that need time. Example: Reading time
It should be like: S Feed the cat
Type [end] to stop inputing tasks.
        """

            print(description)

            # Recolhe o tipo de task
            task_input = (input("> "))

            parts = task_input.split(maxsplit=1)

            parts[0].strip().upper()

            while len(parts) < 2:
                print("Please, input both the task type and the task name (don't put space in the start, like: > a, >a).")

                task_input = (input("> "))

                parts = task_input.split(maxsplit=1)

                parts[0] = parts[0].upper()


            while parts[0] not in ["C", "S", "T"]:
                print("Please, input a valid type")
                parts[0] = (input("> ")).upper()

            print(parts)

            while tasks_input in ["END", ""] and tasks == []:
                print("You need at least 1 task to continue")
                tasks_input = (input("> ")).strip().upper()

        # Recebe o input do usuário e coloca na lista (colocar opção de remover mais tarde)
            num = 0
            while tasks_input != "end":
                tasks.append(tasks_input)
                for i in tasks:
                    num +=1 
                    print(f"{num}. {i}")
                tasks_input = (input("Continue: "))
                num = 0

            # Pega o tamanho inicial das tasks
            tasks_remaining = len(tasks)

            for i in tasks:
                print(i)


tasks_compleeted = 0

# Condições para o código funcionar lol
if task_type == "S":
    done = []
    tasks = [task for i, task in enumerate(tasks) if i not in done]
    tasks_compleeted += len(done)

    

# Início da lógica

# Pega o tamanho atual das tasks
tasks_lenght = len(tasks)

if user_input == "PROGRESS":
    # %
    progress = int((tasks_compleeted / tasks_remaining) * 100)

    if progress < 100:
        print(f"You have {tasks_lenght} tasks remaining:")

        num = 0
        for remaining in range(tasks_lenght):
            num += 1    
            print(f"{num}. {tasks[remaining]}")



    print(f"Progress: {progress}%")

    if progress == 100:
        print("Congratulations, you did all the tasks!")