from settings import *

text_map = [
    '222222222222',
    '2..........2',
    '2.....IV...2', 
    '2..........2', 
    '2..........2', 
    '2...201FG..2', 
    '2..........2',
    '222222222222'
]

world_map = {}
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            if char == '0':
                world_map[(i * TILE, j * TILE)] = '0'
            elif char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == '2':
                world_map[(i * TILE, j * TILE)] = '2'
            elif char == 'I':
                world_map[(i * TILE, j * TILE)] = 'I'
            elif char == 'M':
                world_map[(i * TILE, j * TILE)] = 'M'
            elif char == 'F':
                world_map[(i * TILE, j * TILE)] = 'F'
            elif char == 'G':
                world_map[(i * TILE, j * TILE)] = 'G'
            elif char == 'V':
                world_map[(i * TILE, j * TILE)] = 'V'
            elif char == 'K':
                world_map[(i * TILE, j * TILE)] = 'K'
