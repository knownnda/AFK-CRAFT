START_KEY = "f8"
STOP_KEY = "f9" # super sigma panic button works any time

SCREEN_W = 1920
SCREEN_H = 1080
FOV = 70 # Vert fov. "Normal" in the menu
SENSITIVITY = 0.5 

# Mc turns (0.6*s + 0.2)^3 * 8 * 0.15 degrees per mouse count
# this is how mc's own code does it, so should be spot on idk tho 

_f = SENSITIVITY * 0.6 + 0.2
DEG_PER_COUNT = _f ** 3 * 8 * 0.15
COUNTS_PER_DEG = 1 / DEG_PER_COUNT

CX = SCREEN_W // 2 # middle of the screen (where the crosshair is)
CY = SCREEN_H // 2

#where to look for each block rev to you (degrees)
#based of guesses CHANGE IF IT DOESN'T WORK!!

HEAD_PITCH = 8 
FEET_PITCH = 45

WALK_ONE_BLOCK = 0.23 # walking speed is roughly around 4.3 ish block per sec
LOG_TIME = 3.2 # punching a log takes 3 secs but a lil extra time jst incase of lag
LOGS_WANTED = 20 # based on how many logs the user wants

DEBUG = False # true = saves pic of what it thinks are trees into debug/  