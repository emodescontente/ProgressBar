import time

def countdown_timer(seconds):
    while seconds > 0:
        # Divide os segundos em minutos e segundos restantes
        mins, secs = divmod(seconds, 60)
        
        # Formata o tempo como 00:00
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        
        # O end='\r' faz o cursor voltar para o início da linha
        print(timer_format, end='\r')
        
        time.sleep(1) # Pausa o código por 1 segundo
        seconds -= 1



# ritual de início
print("Hello, world!")

# Agora, começo do projeto PROGRESS BAR, HELL YEAH1!1!!!1111!1
print("""Progress bar: input your tasks to make your life easier!
Input your task (1 per time).
Write end to stop and del to delete one.""")

tasks = []
tasks_input = str(input())

while tasks_input in ["end", ""]:
    print("You need at least 1 task to continue")
    tasks_input = str(input())

# Recebe o input do usuário e coloca na lista (colocar opção de remover mais tarde)
num = 0
while tasks_input != "end":
    tasks.append(tasks_input)
    for i in tasks:
        num +=1 
        print(f"{num}. {i}")
    tasks_input = str(input("Continue: "))
    num = 0

# Pega o tamanho inicial das tasks
tasks_remaining = len(tasks)

for i in tasks:
    print(i)


description = """
Please, input your task type:

[S] Single: tasks that only need complete 1 time. Example: Feed the cat.
[C] CheckList: tasks that need complete various times. Example: Homeworks done.
[T] Timed: tasks that need time. Example: Reading time.
"""

print(description)

# Recolhe o tipo de task
task_type = str(input()).strip().capitalize()

while task_type not in ["C", "S", "T"]:
    print("Please, input a valid type")
    task_type = str(input())

tasks_compleeted = 0

# Condições para o código funcionar lol
if task_type == "S":
    done = []
    tasks = [task for i, task in enumerate(tasks) if i not in done]
    tasks_compleeted += len(done)

    

# Início da lógica

# Pega o tamanho atual das tasks
tasks_lenght = len(tasks)

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