# keyboard n some mouse stuff
# uses pydirectinput cause mc just ignores normal pyautogui inputs
import ctypes
import time

import pydirectinput as pdi 

import config
from state import nap 

try:
    # Windows display scaling (125% etc) messes up the mouse without this
    ctypes.windll.shcore.setprocessDpiAwareness(2)
except Exception:
    pass

pdi.PAUSE = 0 # by default it waits 0.1s after EVERYTHING, made turning super duper slow
pdi.FAILSAFE = False # mouse is stuck in the middle in game so the corner failsafe never works anyway 

_pitch = 0.0 # where we think we're looking up/down 


def tap(key, t=0.06):
    pdi.keyDown(key)
    time.sleep(t)
    pdi.keyUp(key)

def hold(key, seconds):
    pdi.keyDown(key)
    try:
        nap(seconds)
    finally:
        pdi.keyUp(key) # always let go even if F9 gets pressed

def walk_blocks(n):
    hold("w", n * config.WALK_ONE_BLOCK)

def walk_jumping(seconds):
    # hold w and jump every so often so it gets over lil bumps
    pdi.keyDown("w")
    try:
        end = time.time() + seconds 
        while time.time() < end:
            tap("space")
            nap(0.4)
    finally:
        pdi.keyUp("w")

def look (dx, dy):
    # moves the mouse in small chunks cause one big move sometimes gets half eaten 
    dx, dy = int(round(dx)), int(round(dy))
    steps = max(1, max(abs(dx), abs(dy)) // 40)
    done_x = done_y = 0 
    for i in range(1, steps + 1):
        tx = dx * i // steps
        ty = dy * i // steps 
        pdi .moveRel(tx - done_x, ty - done_y)
        done_x, done_y = tx, ty
        time.sleep(0.004)

def turn(deg):
    # = is right n - is left
    look(deg * config.COUNTS_PER_DEG, 0)
    
def set_pitch(deg):
    # look up/down to an exact angle, + is down
    global _pitch
    deg = max(-90, min(90, deg))
    look(0, (deg - _pitch) * config.COUNTS_PER_DEG)
    _pitch = deg

def reset_pitch():
    # we dont know where we're looking when it starts 
    # so look ALL the way down (it stops at 90) then come back up to straight ahead
    global _pitch 
    look(0, 200 * config.COUNTS_PER_DEG)
    _pitch = 90
    set_pitch(0)
    
def mine_for(seconds):
    # hold left click
    try:
        nap(seconds)
    finally:
        pdi.mouseUp(button="left")

def let_go():
    # let go of EVERYTHING so it doesn't walk off forever with w held down
    for k in ("w", "a", "s ", "d", "shift", "space"):
        pdi.keyUp(k)
    pdi.mouseUp(button="left")
    pdi.mouseUp(button="right")
    
