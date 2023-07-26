import math

VERSION = "0.1.0"

# game
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0  # might not need

# PLAYER_POS = 1.5, 5  # get from the map in the future
# PLAYER_ANGLE = 1.5  # could get from the map so player does start facing a wall
PLAYER_SPEED = 0.003  # originally 0.004
PLAYER_ROT_SPEED = 0.002  # rotation speed
PLAYER_SIZE_SCALE = 60

MOUSE_SENSITIVITY = 0.0002  # originally 0.0003
MOUSE_MAX_REL = 40
MOUSE_BOARDER_LEFT = 100
MOUSE_BOARDER_RIGHT = WIDTH - MOUSE_BOARDER_LEFT

FLOOR_COLOR = (30, 30, 30)  # get from the map in the future

# ray casting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 250
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
