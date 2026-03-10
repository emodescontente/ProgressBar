import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_format, end='\r')
        time.sleep(1)
        seconds -= 1
if __name__ == "__main__":
    countdown_timer(5)