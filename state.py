# stuff every file needs to see
# yes it globals shocking right 😱
import threading
import time 

stop_requested = threading.Event()
start_requested = False
running = False


class Stopped(Exception):
    pass

def checkpoint():
    # if F9 got pressed stop
    if stop_requested.is_set():
        raise Stopped

def nap(seconds):
    # same as time.sleep but F9 still works while its waiting
    end = time.time() + seconds
    while True:
        checkpoint()
        left = end - time.time()
        if left <= 0:
            return 
        time.sleep(min(0.05, left))

def reset():
    global logs
    logs = 0 # this is jst counted not read off the screen so its a guess

reset()