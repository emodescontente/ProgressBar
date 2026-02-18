# ritual de início
print("Hello, world!")

# Agora, começo do projeto PROGRESS BAR HELL YEAH
print("Progress bar: input your tasks to make your life easier!")

# Mudar isso para input mais tarde, depois dos testes
tasks = ["Give cat food", "Pet the panda", "Trow a ball to clippy"]

for i in tasks:
    print(i)

tasks_remaining = len(tasks)

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
    for pop in range(done - 1):
        tasks.pop(pop)
    tasks_compleeted += task_done

    

if task_type == "Various":
    print("Please, input the quantity of tasks")

if task_type == "Time":
    print("Please, input your time needed")

# Início da lógica
tasks_lenght = len(tasks)

progress = int((tasks_compleeted / tasks_remaining) * 100)


print(f"You have {tasks_lenght - 1} tasks remaining:")
for remaining in range(tasks_lenght - 1):
        print(tasks[remaining])

print(f"Progress: {progress}%")

if progress == 100:
    print("Comgratulations, you did all the tasks!")