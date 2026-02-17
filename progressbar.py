#  ritual de início
print("Hello, world!")

# Agora, começo do projeto PROGRESS BAR HELL YEAH
print("Progress bar: input your tasks to make your life easier!")

# Mudar isso para input mais tarde, depois dos testes
tasks = ["Give cat food", "Pet the panda", "Trow a ball to clippy"]

print("Please, input your task type: ")
print("Unique: tasks that only need 1 step.")
print("Various: tasks that need various steps.")
print("Time: tasks that only need time.")
# isso também
task_type = "Unique"

# Condições para o código funcionar
if task_type == "Various":
    print("Please, input the quantity of tasks")

if task_type == "Time":
    print("Please, input your time needed")

# Início da lógica
tasks_compleeted = 3
progress = int((tasks_compleeted / len(tasks)) * 100)

print(f"Progress: {progress}%")

if progress == 100:
    print("Comgratulations, you did all the tasks!")