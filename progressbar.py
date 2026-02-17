# ritual de início
print("Hello, world!")

# Agora, começo do projeto PROGRESS BAR HELL YEAH
print("Progress bar: input your tasks to make your life easier!")

# Mudar isso para input mais tarde, depois dos testes
tasks = ["Give cat food", "Pet the panda", "Trow a ball to clippy"]

tasks_lenght = len(tasks)

print("Please, input your task type: ")
print("Unique: tasks that only need complete 1 time. Ex: Feed the cat.")
print("Various: tasks that need complete various times. Ex: Homeworks done.")
print("Time: tasks that need time. Ex: Study time.")
# isso também
task_type = "Unique"

tasks_compleeted = 0

# Condições para o código funcionar
if task_type == "Unique":
    task_done = 1
    done = 2
    tasks.pop(done - 1)
    tasks_compleeted += task_done

    

if task_type == "Various":
    print("Please, input the quantity of tasks")

if task_type == "Time":
    print("Please, input your time needed")

# Início da lógica
progress = int((tasks_compleeted / tasks_lenght) * 100)

if tasks_lenght != 0:
    print(f"You have {tasks_lenght - 1} tasks remain:")
    for remain in range(tasks_lenght - 1):
        print(tasks[remain])

print(f"Progress: {progress}%")

if progress == 100:
    print("Comgratulations, you did all the tasks!")