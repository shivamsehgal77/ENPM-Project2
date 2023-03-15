# Move the robot up
def robot_move_up(robot):
    x,y=robot
    robot=(x,y-1)
    cost=1
    return cost,robot
# Move the robot down
def robot_move_down(robot):
    x,y=robot
    robot=(x,y+1)
    cost=1
    return cost,robot
# Move the robot left
def robot_move_left(robot):
    x,y=robot
    robot=(x-1,y)
    cost=1
    return cost,robot
# Move the robot right
def robot_move_right(robot):
    x,y=robot
    robot=(x+1,y)
    cost=1
    return cost,robot
# Move the robot up left
def robot_move_up_left(robot):
    x,y=robot
    robot=(x-1,y-1)
    cost=1.4
    return cost,robot
# Move the robot up right
def robot_move_up_right(robot):
    x,y=robot
    robot=(x+1,y-1)
    cost=1.4
    return cost,robot
# Move the robot down left
def robot_move_down_left(robot):
    x,y=robot
    robot=(x-1,y+1)
    cost=1.4
    return cost,robot
# Move thr robot down right
def robot_move_down_right(robot):
    x,y=robot
    robot=(x+1,y+1)
    cost=1.4
    return cost,robot