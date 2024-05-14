# Example file showing a circle moving on screen
import pygame
import random
import json
from level_manager import get_level


# pygame setup
pygame.init()
PIXEL_WIDTH = 50
#screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Sokoban")
running = True

#load graphics
def load_icon(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

#load levels from json

def load_levels(file_path):
    with open(file_path, 'r') as file:
        level_data = json.load(file)
    return level_data['levels']

#set level parameters
levels = get_level()
levels_data = load_levels("levels.json")
WIDTH = levels_data[levels-1]['width']
HEIGHT = levels_data[levels-1]['height']
grid = levels_data[levels-1]['grid']
ROW_NUM = levels_data[levels-1]['row_num']
COL_NUM = levels_data[levels-1]['col_num']
y = levels_data[levels-1]['row_pos']
x = levels_data[levels-1]['col_pos']
trget = levels_data[levels-1]['target']

screen = pygame.display.set_mode((WIDTH,HEIGHT))

#if we can go in direction of pressed button or not
def can_go(button,x,y):
    if button=='w':
        if grid[y-1][x]==0 or grid[y-1][x]==4:
            return 1
    if button=='s':
        if grid[y+1][x]==0 or grid[y+1][x]==4:
            return 1
    if button=='a':
        if grid[y][x-1]==0 or grid[y][x-1]==4:
            return 1
    if button=='d':
        if grid[y][x+1]==0 or grid[y][x+1]==4:
            return 1
    return 0

#if we can move crates in direction of pressed button or not
def can_move(button,x,y):
    if button=='w':
        if grid[y-1][x]==3 and (grid[y-2][x]==0 or grid[y-2][x]==4):
            return 1
    if button=='s':
        if grid[y+1][x]==3 and (grid[y+2][x]==0 or grid[y+2][x]==4):
            return 1
    if button=='a':
        if grid[y][x-1]==3 and (grid[y][x-2]==0 or grid[y][x-2]==4):
            return 1
    if button=='d':
        if grid[y][x+1]==3 and (grid[y][x+2]==0 or grid[y][x+2]==4):
            return 1

#move crate
def move(button):
    global x,y
    if button=='w':
        grid[y-2][x]=3
    if button=='s':
        grid[y+2][x]=3
    if button=='a':
        grid[y][x-2]=3
    if button=='d':
        grid[y][x+2]=3

#go in direction of pressed button
def go(button):
    global x,y
    if button=='w':
        grid[y][x]=0
        y-=1
        grid[y][x]=2
    if button=='s':
        grid[y][x]=0
        y+=1
        grid[y][x]=2
    if button=='a':
        grid[y][x]=0
        x-=1
        grid[y][x]=2
    if button=='d':
        grid[y][x]=0
        x+=1
        grid[y][x]=2

#check if win or not
def win():
    for i in trget:
        if grid[i[0]][i[1]]!=3:
            return 0
    return 1

#prints grid
def printgrid():
    for i in range(ROW_NUM):
        for j in range(COL_NUM):
            if grid[i][j]==1:
                screen.blit(STONE,(j*50,i*50))
            elif grid[i][j]==2:
                screen.blit(PLAYER,(j*50,i*50))
            elif grid[i][j]==3:
                if [i,j] in trget:
                    screen.blit(SET_CRATE,(j*50,i*50))
                else:
                    screen.blit(DEF_CRATE,(j*50,i*50))
            elif grid[i][j]==4:
                screen.blit(TARGET,(j*50,i*50))
    
#load images
DEF_CRATE = load_icon('Graphics\crate_01.png', [PIXEL_WIDTH, PIXEL_WIDTH])
SET_CRATE = load_icon('Graphics\crate_02.png', [PIXEL_WIDTH, PIXEL_WIDTH])
STONE = load_icon('Graphics\stone_01.png', [PIXEL_WIDTH, PIXEL_WIDTH])
PLAYER = load_icon('Graphics\player_02.png', [PIXEL_WIDTH, PIXEL_WIDTH])
TARGET = load_icon('Graphics\\target_01.png', [PIXEL_WIDTH, PIXEL_WIDTH])

#main loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # flip() the display to put your work on screens
    pygame.display.flip()
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#ffffb3")

    #printing grid
    printgrid()
    
    #change movement distantion
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if can_move('w',x,y):
            move('w')
            go('w')
        elif can_go('w',x,y):
            go('w')
    elif keys[pygame.K_s]:
        if can_move('s',x,y):
            move('s')
            go('s')
        elif can_go('s',x,y):
            go('s')
    elif keys[pygame.K_a]:
        if can_move('a',x,y):
            move('a')
            go('a')
        elif can_go('a',x,y):
            go('a')
    elif keys[pygame.K_d]:
        if can_move('d',x,y):
            move('d')
            go('d')
        elif can_go('d',x,y):
            go('d')

    pygame.display.flip()
    #idk how to call it
    for i in trget:
        if grid[i[0]][i[1]]==0:
            grid[i[0]][i[1]]=4

    #quit game if we win
    if win():
        running=False
        
   

    clock.tick(8)

pygame.quit()   