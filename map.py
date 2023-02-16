from settings import *

text_map = [
    '000000000000',
    '0..........0', # карта имба 
    '0..........0', # чтобы рисовать обьекты
    '0....I.....0', # используйте 0 и 1
    '0..........0', # 1 кирпич
    '0..........0', # 0 стена
    '0..........0',
    '000000000000',
]

world_map = {}
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            if char == '0':
                world_map[(i * TILE, j * TILE)] = '0'
            elif char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == 'I':
                world_map[(i * TILE, j * TILE)] = 'I'
            elif char == 'M':
                world_map[(i * TILE, j * TILE)] = 'M'
            elif char == 'F':
                world_map[(i * TILE, j * TILE)] = 'F'
            elif char == 'G':
                world_map[(i * TILE, j * TILE)] = 'G'            