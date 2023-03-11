
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
def robot_move_up_left(robot):
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



