import pygame
import sys
import matplotlib.pyplot as plt
import cv2
from queue import PriorityQueue


# Initialize Pygame
pygame.init()
# Initializing surface

white=(255,255,255)
# Initializing Color

red = (255,0,0)
green = (0,255,0)
# points_hexgon = [(443.30, 125),(421.65, 164.33),(378.35, 164.33),(356.70, 125),(378.35, 85.67),(421.65, 85.67)]
points_triangle = [(460, 25), (460, 225), (510, 125)]
points_hexgon = [(300,44.22649731),(230.04809472,84.61324865),(230.04809472,165.38675135),(300,205.77350269),(369.95190528,165.38675135),(369.95190528,84.61324865)]
points_triangle_border = [(455,246.18033989),(455.00,3.81966011),(515.59016994,125)]
# points_triangle_border = 
# Set the dimensions of the screen
screen = pygame.display.set_mode((600, 250))
pygame.draw.rect(screen, white, pygame.Rect(5,5,590,240))
pygame.draw.rect(screen,red,pygame.Rect(95,5,60,105))
pygame.draw.rect(screen, red, pygame.Rect(100, 5, 50, 100))
pygame.draw.rect(screen, red, pygame.Rect(95, 140, 60, 105))
pygame.draw.rect(screen, red, pygame.Rect(100, 145, 50, 100))
# pygame.draw.polygon(screen, red, points_triangle_border)
pygame.draw.polygon(screen, red, points_triangle)
pygame.draw.polygon(screen, red, points_hexgon)
pixel_color = (0, 0,255) # Red
pixel_x = 0
pixel_y = 300


def robot_move_up(robot):
    x,y=robot
    robot=(x,y-1)
    cost=1
    return cost,robot

def robot_move_down(robot):
    x,y=robot
    robot=(x,y+1)
    cost=1
    return cost,robot
def robot_move_left(robot):
    x,y=robot
    robot=(x-1,y)
    cost=1
    return cost,robot
def robot_move_right(robot):
    x,y=robot
    robot=(x+1,y)
    cost=1
    return cost,robot


def robot_move_up_left(robot):
    x,y=robot
    robot=(x-1,y-1)
    cost=1.4
    return cost,robot
def robot_move_up_right(robot):
    x,y=robot
    robot=(x+1,y-1)
    cost=1.4
    return cost,robot

def robot_move_down_left(robot):
    x,y=robot
    robot=(x-1,y+1)
    cost=1.4
    return cost,robot

def robot_move_down_right(robot):
    x,y=robot
    robot=(x+1,y+1)
    cost=1.4
    return cost,robot

black = (0, 0, 0)

    

robot_start_position=(10,10)
robot_goal_position=(50,90)
# robot_goal_position=(550,30)
ctc_node=0
parent_node_index=None
node_index=0
closed_list={}
open_list=PriorityQueue()
info=[ctc_node,node_index,parent_node_index,robot_start_position]
open_list.put(info)
while True:
    if(open_list.empty()):
        print("No solution")
    info=open_list.get()
    if(info[3]==robot_goal_position):
        print("goalt reached")
        closed_list[info[1]]=[info[0],info[2],info[3]]
        print(closed_list[info[2]])
        goal_node=info[1]
        break
    ctc_move,new_pos=robot_move_left(info[3])
    if(new_pos==robot_goal_position):
        print("goal reached")
        closed_list[node_index+1]=[ctc_move+info[0],info[2],new_pos]
        goal_node=node_index+1
        break
    if screen.get_at(new_pos) == white:
        if not any(lst[2] == new_pos for lst in closed_list.values()):
            if not any(items[3] == new_pos for items in open_list.queue):
                ctc_node_left = ctc_move + info[0]
                node_index += 1
                info_left = [ctc_node_left, node_index, info[1], new_pos]
                open_list.put(info_left)
            else:
                index = next(i for i, [_, _, _, (x, y)] in enumerate(open_list.queue) if (x, y) == new_pos)
                if round(open_list.queue[index][0], 1) > round(ctc_move + info[0], 1):
                    open_list.queue[index][0] = ctc_move + info[0]
                    open_list.queue[index][2] = info[1]

                            
                    


    ctc_move,new_pos=robot_move_up(info[3])
    if(new_pos==robot_goal_position):
        print("goal reached")
        closed_list[node_index+1]=[ctc_move+info[0],info[2],new_pos]
        goal_node=node_index+1
        break
    if screen.get_at(new_pos) == white:
        if not any(lst[2] == new_pos for lst in closed_list.values()):
            if not any(items[3] == new_pos for items in open_list.queue):
                ctc_node_up = ctc_move + info[0]
                node_index += 1
                info_left = [ctc_node_up, node_index, info[1], new_pos]
                open_list.put(info_left)
            else:
                index = next(i for i, [_, _, _, (x, y)] in enumerate(open_list.queue) if (x, y) == new_pos)
                if round(open_list.queue[index][0], 1) > round(ctc_move + info[0], 1):
                    open_list.queue[index][0] = ctc_move + info[0]
                    open_list.queue[index][2] = info[1]
                            
                            
    ctc_move,new_pos=robot_move_right(info[3])
    if(new_pos==robot_goal_position):
        print("goal reached")
        closed_list[node_index+1]=[ctc_move+info[0],info[2],new_pos]
        goal_node=node_index+1
        break
    if screen.get_at(new_pos) == white:
        if not any(lst[2] == new_pos for lst in closed_list.values()):
            if not any(items[3] == new_pos for items in open_list.queue):
                ctc_node_right = ctc_move + info[0]
                node_index += 1
                info_left = [ctc_node_right, node_index, info[1], new_pos]
                open_list.put(info_left)
            else:
                index = next(i for i, [_, _, _, (x, y)] in enumerate(open_list.queue) if (x, y) == new_pos)
                if round(open_list.queue[index][0], 1) > round(ctc_move + info[0], 1):
                    open_list.queue[index][0] = ctc_move + info[0]
                    open_list.queue[index][2] = info[1]
                            
                            

    ctc_move,new_pos=robot_move_down(info[3])
    if(new_pos==robot_goal_position):
        print("goal reached")
        closed_list[node_index+1]=[ctc_move+info[0],info[2],new_pos]
        goal_node=node_index+1
        break
    if screen.get_at(new_pos) == white:
        if not any(lst[2] == new_pos for lst in closed_list.values()):
            if not any(items[3] == new_pos for items in open_list.queue):
                ctc_node_down = ctc_move + info[0]
                node_index += 1
                info_left = [ctc_node_down, node_index, info[1], new_pos]
                open_list.put(info_left)
            else:
                index = next(i for i, [_, _, _, (x, y)] in enumerate(open_list.queue) if (x, y) == new_pos)
                if round(open_list.queue[index][0], 1) > round(ctc_move + info[0], 1):
                    open_list.queue[index][0] = ctc_move + info[0]
                    open_list.queue[index][2] = info[1]
                            
    
    ctc_move,new_pos=robot_move_down_left(info[3])
    if(new_pos==robot_goal_position):
        print("goal reached")
        closed_list[node_index+1]=[ctc_move+info[0],info[2],new_pos]
        goal_node=node_index+1
        break
    if screen.get_at(new_pos) == white:
        if not any(lst[2] == new_pos for lst in closed_list.values()):
            if not any(items[3] == new_pos for items in open_list.queue):
                ctc_node_dl = ctc_move + info[0]
                node_index += 1
                info_left = [ctc_node_dl, node_index, info[1], new_pos]
                open_list.put(info_left)
            else:
                index = next(i for i, [_, _, _, (x, y)] in enumerate(open_list.queue) if (x, y) == new_pos)
                if round(open_list.queue[index][0], 1) > round(ctc_move + info[0], 1):
                    open_list.queue[index][0] = ctc_move + info[0]
                    open_list.queue[index][2] = info[1]
                            
    
    ctc_move,new_pos=robot_move_down_right(info[3])
    if(new_pos==robot_goal_position):
        print("goal reached")
        closed_list[node_index+1]=[ctc_move+info[0],info[2],new_pos]
        goal_node=node_index+1
        break
    if screen.get_at(new_pos) == white:
        if not any(lst[2] == new_pos for lst in closed_list.values()):
            if not any(items[3] == new_pos for items in open_list.queue):
                ctc_node_dr = ctc_move + info[0]
                node_index += 1
                info_left = [ctc_node_dr, node_index, info[1], new_pos]
                open_list.put(info_left)
            else:
                index = next(i for i, [_, _, _, (x, y)] in enumerate(open_list.queue) if (x, y) == new_pos)
                if round(open_list.queue[index][0], 1) > round(ctc_move + info[0], 1):
                    open_list.queue[index][0] = ctc_move + info[0]
                    open_list.queue[index][2] = info[1]
                            
    
    ctc_move,new_pos=robot_move_up_left(info[3])
    if(new_pos==robot_goal_position):
        print("goal reached")
        closed_list[node_index+1]=[ctc_move+info[0],info[2],new_pos]
        goal_node=node_index+1
        break
    if screen.get_at(new_pos) == white:
        if not any(lst[2] == new_pos for lst in closed_list.values()):
            if not any(items[3] == new_pos for items in open_list.queue):
                ctc_node_ul = ctc_move + info[0]
                node_index += 1
                info_left = [ctc_node_ul, node_index, info[1], new_pos]
                open_list.put(info_left)
            else:
                index = next(i for i, [_, _, _, (x, y)] in enumerate(open_list.queue) if (x, y) == new_pos)
                if round(open_list.queue[index][0], 1) > round(ctc_move + info[0], 1):
                    open_list.queue[index][0] = ctc_move + info[0]
                    open_list.queue[index][2] = info[1]
                            

    ctc_move,new_pos=robot_move_up_right(info[3])
    if(new_pos==robot_goal_position):
        print("goal reached")
        closed_list[node_index+1]=[ctc_move+info[0],info[2],new_pos]
        goal_node=node_index+1
        break
    if screen.get_at(new_pos) == white:
        if not any(lst[2] == new_pos for lst in closed_list.values()):
            if not any(items[3] == new_pos for items in open_list.queue):
                ctc_node_ur = ctc_move + info[0]
                node_index += 1
                info_left = [ctc_node_ur, node_index, info[1], new_pos]
                open_list.put(info_left)
            else:
                index = next(i for i, [_, _, _, (x, y)] in enumerate(open_list.queue) if (x, y) == new_pos)
                if round(open_list.queue[index][0], 1) > round(ctc_move + info[0], 1):
                    open_list.queue[index][0] = ctc_move + info[0]
                    open_list.queue[index][2] = info[1]
                            
                                                    
    closed_list[info[1]]=[info[0],info[2],info[3]]
    screen.set_at(info[3], black)
    pygame.display.update()
    print(info[2])

    



print(closed_list)


# def backtrack():
path = []
current_node = goal_node
while goal_node is not None:
    goal_node_parent = closed_list[goal_node][1]
    path.append(closed_list[goal_node][2])
    screen.set_at(closed_list[goal_node][2], green)
    goal_node=goal_node_parent
    pygame.display.update()
    

    
    


# reverse the path list to get the correct order of nodes
path.reverse()
print(path)


while True:
    # Event loop to handle user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            
            


    # Update the screen
    




