from timer import countdown_timer

def get_input():
    while True:
        valor = input("> ")
        if valor != "":
            return valor
        print("Por favor, escreva alguma coisa.")

def p():
    print("")

def AddTask(type: str, task_name: str, additional: int = None):
    global actual_id
    if type == "C":
        task_list[actual_list].append({"id": actual_id + 1, "type": type, "name": task_name,"num": 0, "cl_final": additional})
    elif type == "S":
        task_list[actual_list].append({"id": actual_id + 1, "type": type, "name": task_name, "status": "Inacabado"})
    elif type == "T":
        task_list[actual_list].append({"id": actual_id + 1, "type": type, "name": task_name, "timer": additional, "status": "Inacabado"})
    actual_id += 1

def NoTaskDone():
    for t in task_list[actual_list]:
        if t['type'] != 'C':
            if t["status"] == "Feito":
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
            print("   Essa lista está vazia.")
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
        print("Por favor, digite um número válido dentro da lista.")
        return False

def GetNum():
    while True:
        num = get_input().strip()
        try:
            num = int(num)
            return num
        except ValueError:
            p()
            print("Por favor, digite um número válido dentro da lista.")
            continue

def GetTimer():
    time = 0
    p()
    print("Escreva o tempo para aumentar o timer.")
    print("[S]: segundos, [M]: minutos, [H]: horas.")
    print("Deve estar assim: S 30, ou: S -10 se você quiser diminuir. Digite [end] para parar.")
    while True:
        time_input = get_input().strip().upper()
        if time_input =="END":
            break
        parts_timer = time_input.split(maxsplit=1)
        if len(parts_timer) != 2:
            p()
            print("Por favor, digite apenas o formato e o tempo.")
            continue
        if parts_timer [0] not in ["S","M","H"]:
            p()
            print("Por favor, digite um formato válido.")
            continue
        try:
            parts_timer[1] = int(parts_timer[1])
        except ValueError:
            p()
            print("Por favor, digite um número válido.")
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
            print("Não posso fazer um timer negativo, desculpe.")
            continue
        time += timer
        p()
        print(ShowTime(time))
        p()
        print("Continue:")
        continue
    return time

print("---------------------------------------------------")
print("""Bem-vindo à Barra de Progresso!
Digite [add] para adicionar suas tarefas.
Digite [del] para deletar uma tarefa.
Digite [done] para marcar tarefas como pronta.
Digite [undo] para desfazer ou diminuir uma tarefa.
Digite [edit] para editar o nome ou valor de uma tarefa.
Digite [progress] para ver as tarefas e o progresso feito.
Digite [clear] para deletar todas as tarefas.
Digite [list] para ver e mudar entre listas de tarefas.
Digite [close] para fechar o programa (ou ctrl+c).""")

command_list = ["ADD", "DEL", "DONE", "PROGRESS", "CLOSE", "HELP", "CLEAR", "UNDO", "EDIT", "LIST"]
valid_types = ["S", "C", "T"]
task_list = {"Tarefas": []}
actual_list = "Tarefas"
actual_id = 0
pb_type = True
print("""
Digite [help] se você precisa relembrar os comandos ou uma descrição mais detalhada dos comandos.""")

while True:
    p()
    print("Digite seu comando:")
    user_input = get_input().strip().upper()
    if user_input == "Q PROGRESS":
        pb_type = not pb_type
        p()
        print("Tipo da barra de progresso mudada.")
        continue

    if user_input == "CLOSE":
        break

    if user_input not in command_list:
        p()
        print("Por favor, digite um comando válido.")
        continue

    if user_input not in ["ADD", "HELP", "END", "LIST"] and task_list[actual_list] == []:
        p()
        print("Tente começar adicionando tarefas com [add]")
        continue

    if user_input == "UNDO" and NoTaskDone():
        p()
        print("Nenhuma tarefa está pronta, digite [done] se você quiser marcar uma tarefa como pronta.")
        continue

    match user_input:
        case 'LIST':
            print("---------------------------------------------------")
            print("""Aqui você consegue ver as listas de tarefas.
    * = número da lista.
Digite [create] [nome da lista] para criar uma nova lista.
Digite [move] * para mudar de tarefas com a lista.
Digite [del] * para deletar uma lista.
Digite [edit] * para editar o nome de uma lista.
Digite [end] para parar.
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
                            p()
                            print("Uma lista com esse nome já existe.")
                            break
                    task_list.update({list_input[1]: []})
                    ShowLists()
                    print("Continue.")
                    continue

                if len(list_input) != 2:
                    p() # type: ignore
                    print('Por favor, digite o comando e o número da lista.')

                if list_input[0] not in valid_input:
                    p()
                    print("Por favor, digite um comando válido.")
                    continue
                list_number = CheckNum(list_input[1]) # type: ignore
                if list_number == False:
                    continue
                if 0 > list_number or list_number > len(task_list):
                    p()
                    print('Por favor, digite um número válido dentro da lista.')
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
                        print(f"Agora você está na lista: {actual_list}")
                        continue
                    case 'DEL':
                        list_name = list(task_list.keys())
                        index = list_number - 1
                        name = list_name[index]
                        task_list.pop(name)
                        p()
                        ShowLists()
                        print("A lista foi deletada.")
                        continue
                    case 'EDIT':
                        new_name = input("Novo nome: ") 
                        
                        list_name = list(task_list.keys())
                        index = list_number - 1
                        name = list_name[index]
                        if actual_list == name:
                            actual_list = new_name
                        task_list[new_name] = task_list.pop(name)
                        p()
                        print("A lista foi renomeada.")
                        ShowLists()
                        continue
                
        case "HELP":
            print("---------------------------------------------------")
            print("""Digite [add] para adicionar suas tarefas.
Digite [del] para deletar uma.
Digite [done] para marcar uma tarefa como pronta.
    Marcar uma tarefa de tempo vai te levar a um timer.
    Digite: Q [número da tarefa] com uma tarefa do tipo Checklist para rapidamente adicionar uma marcação.
Digite [undo] para desfazer ou diminuir uma tarefa.
    Digite: [número da tarefa] com uma tarefa do tipo Checklist para rapidamente desfazer todas as marcações.
Digite [edit] para editar o nome ou valor de uma tarefa.
Digite [progress] para ver as tarefas e o progresso feito.
    Você consegue trocar o visual da barra de progresso digitando [Q progress].
Digite [clear] para deletar todas as tarefas.
Digite [lists] para ver e trocar entre listas de tarefas.
Digite [close] para sair do programa (ou ctrl+c).""")
            print("---------------------------------------------------")
        case "EDIT":
            print("---------------------------------------------------")
            print("""Digite o número da tarefa que você quer editar, então:
Digite [N] se você quer trocar o nome.
Digite [V] se você quer trocar o valor.
Deve estar tipo: 1 N.
Digite [end] para parar.
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
                    print('Por favor, digite apenas o número da tarefa e o que você quer editar.')
                    continue
                number = CheckNum(edit_input[0])
                if not number:
                    continue
                if 0 > number > len(task_list[actual_list]) - 1:
                    p()
                    print("Por favor, digite um número válido dentro da lista.")
                    continue
                if edit_input[1] not in ["N", "V"]:
                    p()
                    print("Por favor, digite um comando válido.")
                    continue

                if edit_input[1] == "N":
                    name = input("Novo nome: ")
                    EditTask(number, "name", name)
                    p()
                    ShowTaskList()
                    p()
                    print('A tarefa foi renomeada.')
                    continue

                if edit_input[1] == "V":
                    i = next((t for t in task_list[actual_list] if t["id"] == number), None) # type: ignore

                    match i["type"]:
                        case "S":
                            p()
                            print("Essa tarefa não tem um valor.")
                            continue
                        case "C":
                            print("Digite o novo número de checks:")
                            while True:
                                val_input = get_input().strip()
                                vallue = CheckNum(val_input)
                                if not vallue:
                                    continue

                                if vallue < i["num"]:
                                    p()
                                    print("Você não pode mudar o valor abaixo das marcações.")
                                    continue
                                i['cl_final'] = vallue
                                p()
                                ShowTaskList()
                                p()
                                print('A tarefa foi editada.')
                                break
                        case "T":
                            time = GetTimer()
                            p()
                            ShowTaskList()
                            p()
                            print('A tarefa foi editada.')
                            EditTask(i['id'], "timer", time)

        case "DONE":
            print("---------------------------------------------------")
            print("""Digite o número da tarefa que você deseja marcar como feita.
Uma tarefa do tipo Única será apenas marcada como feita;
Uma tarefa do tipo Checklist vai adicionar o número que você quiser ao contador;
Uma tarefa de Tempo te levará a um timer.
Digite [end] para parar.
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
                        print('Por favor, digite o número da tarefa na próxima vez.')
                        continue
                    task_id = CheckNum(parts[1])
                    if not task_id:
                        continue
                    task_found = next((t for t in task_list[actual_list] if t["id"] == task_id), None)

                    if not task_found:
                        print("Esta tarefa não existe.")
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
                            print("Esta tarefa já está pronta.")
                            continue
                    else:
                        p()
                        print("O tipo da tarefa não é [C].")
                        continue
                
                done_input = CheckNum(done_input)
                if not done_input:
                    continue
                if 0 > done_input or done_input > len(task_list[actual_list]):
                    p()
                    print('Por favor, digite um número válido dentro da lista.') 
                    continue
                task = 0
                for t in task_list[actual_list]:
                    if t["id"] == done_input:
                        task = t
                if (task["type"] in ["S", "T"] and task["status"] == "Feito") or (task["type"] == "C" and task["num"] == task["cl_final"]):
                    p()
                    print("Esta tarefa já está pronta.")
                    continue

                if 0 < done_input <= len(task_list[actual_list]):
                    if CheckTask(done_input, "type") == "S":
                        EditTask(done_input, "status", "Feito")
                    elif CheckTask(done_input, "type") == "T":
                        print("""
Você tem certeza? Quando você iniciar este timer, não poderá mais sair enquanto ele estiver rodando.
Digite [Y] para rodar.
Digite qualquer outra coisa para cancelar.""")
                        confirm = get_input().strip().upper()
                        if confirm == "Y":
                            countdown_timer(CheckTask(done_input, "timer"))
                            EditTask(done_input, "status", "Feito")
                    elif CheckTask(done_input, "type") == "C":
                        p()
                        print("Quanto?")
                        while True:
                            num = GetNum()
                            if 0 > num:
                                p()
                                print("Esse é um número negativo. Se você quiser diminuir, digite 0 e vá para o menu [undo].")
                                continue
                            if num + CheckTask(done_input, "num") > CheckTask(done_input, "cl_final"):
                                p()
                                print("Isso é mais do que o limite.")
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
                    print("Por favor, digite um número válido dentro da lista.")

        case "UNDO":
            print("---------------------------------------------------")
            print("Digite o número da tarefa que você quer desfazer.")
            print("Digite [end] para parar.")
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
                        print('Por favor, digite o número da tarefa na próxima vez.')
                        continue
                    task_id = CheckNum(parts[1])
                    if not task_id:
                        continue
                    task_found = next((t for t in task_list[actual_list] if t["id"] == task_id), None)

                    if not task_found:
                        print("Esta tarefa não existe.")
                        continue
                    if task_found["type"] == "C":
                        if task_found["num"] != 0:
                            task_found["num"] = 0
                            p()
                            print("Continue.")
                            continue
                        else:
                            p()
                            print("Esta tarefa já está vazia.")
                            continue
                    else:
                        p()
                        print("O tipo da tarefa não é [C].")
                        continue

                undo_input = CheckNum(undo_input)
                if not undo_input:
                    continue

                if CheckTask(undo_input, "status") == "Inacabado":
                    p()
                    print("Esta tarefa não está pronta.")
                    continue
                if 0 > undo_input > actual_id:
                    p()
                    print("Por favor, digite um número válido dentro da lista.")
                    continue
                if CheckTask(undo_input, "num") == 0:
                    p()
                    print("Esta tarefa já está vazia.")
                
                if CheckTask(undo_input, "type") in ["S", "T"]:
                    EditTask(undo_input, "status", "Inacabado")
                elif CheckTask(undo_input, "type") == "C":
                    p()
                    print("Quanto você quer diminuir?")
                    while True:
                        decrease_num = GetNum()
                        if (CheckTask(undo_input, "num") - decrease_num) < 0:
                            p()
                            print("Isso diminui para um número negativo. Se você quiser diminuir toda a tarefa, digite 0 e depois digite q (o número da tarefa).")
                            continue
                        if decrease_num < 0:
                            p()
                            print("Por favor, digite um número positivo para diminuir.")
                            continue
                        for t in task_list[actual_list]:
                            if t["id"] == undo_input:
                                t["num"] -= decrease_num
                        break
                if NoTaskDone():
                    p()
                    print('Todas as tarefas foram marcadas como inacabadas.')
                    print("---------------------------------------------------")
                    break
                print("Continue.")
                p()

        case "ADD":
            print("---------------------------------------------------")
            description = """Aqui você pode adicionar tarefas à sua lista.
Tipos:
[S] Única (Single): tarefas que só precisam ser concluídas 1 vez. Exemplo: Alimentar o gato.
[C] Checklist: tarefas que precisam ser concluídas várias vezes. Exemplo: Dever de casa.
[T] Tempo (Timed): tarefas que exigem tempo. Exemplo: Tempo de leitura.
Deve ficar assim: S Alimentar o gato
Digite [end] para parar de adicionar tarefas."""

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
                    print("Por favor, digite tanto o tipo da tarefa quanto o nome da tarefa.")
                    continue

                if parts[0] not in ["C", "S", "T"]:
                    p()
                    print("Por favor, digite um comando válido.")
                    continue
                
                if parts [0] == "C":
                    p()
                    print("Digite quantos checks (quantas vezes precisa ser feita):")
                    while True:
                        quantity = GetNum()
                        if quantity < 1:
                            print("Isso não é um número válido.")
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
                print("Tarefa adicionada.")
                p()
                continue   
            
        case "DEL":
            print("---------------------------------------------------")
            print("""Digite o número da tarefa para deletá-la.  
Digite [end] para parar.        
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
                    print("Por favor, digite um número válido dentro da lista.")
                    continue

                task_list[actual_list].pop(del_input - 1)
                actual_id -= 1
                for t in task_list[actual_list]:
                    if t["id"] > del_input:
                        t["id"] -= 1
                p()
                ShowTaskList()
                p()
                print("Tarefa deletada")

                if task_list[actual_list] == []:
                    print ("Você deletou todas as tarefas.")
                    break

        case "CLEAR":
            print("---------------------------------------------------")
            print("""Tem certeza de que deseja apagar todas as tarefas?
Se sim, digite [y], senão digite qualquer outra coisa.
""")
            clear_input = get_input().strip().upper()

            if clear_input == "Y":
                task_list[actual_list] = []
                actual_id = 0
                p()
                print("Todas as tarefas foram deletadas.")
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
                    if t["status"] == "Feito":
                        tasks_done += 1
                elif t["type"] == "C":
                    tasks_remaining += t["cl_final"]
                    tasks_done += t["num"]

            progress = int(tasks_done / tasks_remaining * 100) if tasks_remaining > 0 else 0
            p()
            if pb_type:
                print(f"[{'█'*progress + '░' * (100 - progress)}]")
            else:
                print(f"[{'█' * int(progress/10) + '░' * int(10 - progress / 10)}]")
            
            print(f"Progresso: {progress}%")

            if progress == 100:
                print("Parabéns, você completou todas as tarefas!")
            print("---------------------------------------------------")