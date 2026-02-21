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

if __name__ == "__main__":
    # Isso só roda se você executar ESTE arquivo diretamente
    countdown_timer(5)