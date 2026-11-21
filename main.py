import time
import keyboard

import brain #brain.py (gonna make it later on)
import config #config.py (gonna make it later on)
import state # state.py (gonna also make it later on)

def on_start():
    if state.running:
        print("AFK-CRAFT is already running.")
        return
    state.stop_requested.clear()
    state.start_requested = True

def on_stop():
    if state.running:
        print("Stopping...")
    state.stop_requested.set()


# hotkeys (F8 N F9) just flip a switch so the bot runs down here so F9 always works

keyboard.add_hotkey(config.START_KEY, on_start) #DEFINE START_KEY IN CONFIG.PY!!! >w<
keyboard.add_hotkey(config.STOP_KEY, on_stop) #DEFINE STOP_KEY IN CONFIG.PY!! :3

print(f"{config.START_KEY.upper()} to start (in game), {config.STOP_KEY.upper()} to stop, ctrl+c here to quit")

try:
    while True:
        if state.start_requested:
            state.start_requested = False
            state.running = True
            brain.run()
            state.running = False
            print(f"{config.START_KEY.upper()} to go again")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Bye bye :3")