import math as m

# экран
WIDTH = 1200
HEIGHT = 700
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 100
TILE = 100
FPS_POS = (WIDTH - 65, 5)

# алгебра
FOV = m.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 500
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * m.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# картиночки
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# камера
player_pos = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_angle = 0
player_speed = 2

# палитрочка
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)