from queue import PriorityQueue
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from matplotlib.patches import Polygon
import numpy as np

#Obstacle definition
def arrow_obstacle1(coordinates): #breaking the first obstacle into two parts
    x = coordinates[0] 
    y = coordinates[1]
    if  ((y-180)-((180-185)/(80-36))*(x-80) <= 0) and ((y-100)-((100-180)/(105-80))*(x-105) <= 0) and ((y-100)-((100-185)/(105-36))*(x-105) >= 0): # line l4
#         ((y-180)-((180-185)/(80-36))*(x-80) <= 0) # line l5 (arrow)
#         ((y-100)-((100-180)/(105-80))*(x-105) <= 0): # line l4 (arrow) 
#         ((y-100)-((100-185)/(105-36))*(x-105) >= 0): # line l1 (arrow)
        return True
    else:
        return False

def arrow_obstacle2(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    if ((y-210)-((210-185)/(115-36))*(x-115) <= 0) and ((y-210)-((210-180)/(115-80))*(x-115) >= 0) and ((y-180)-((180-185)/(80-36))*(x-80) >= 0):
#     ((y-210)-((210-185)/(115-36))*(x-115) <= 0) # line l2 (arrow)
#     ((y-210)-((210-180)/(115-80))*(x-115) >= 0) # line l3 (arrow)
#     ((y-180)-((180-185)/(80-36))*(x-80) >= 0) # line l5 (arrow)
        return True
    else:
        return False

def circle_obstacle(coordinates): #circle obstacle definition
    x = coordinates[0]
    y = coordinates[1]
    if (((x-300)**2)+((y-185)**2)-(40**2)) <= 0:
        return True
    else:
        return False

def hexagon_obstacle(coordinates): #circle obstacle definition
    x = coordinates[0]
    y = coordinates[1]
    if (x >= 165) and ((y-59.586)-((59.586-79.793)/(200-165))*(x-200) >= 0) and ((y-79.793)-((79.793-59.586)/(235-200))*(x-235) >= 0) and (x <= 235) and ((y-140.414)-((140.414-120.207)/(200-235))*(x-200) <= 0) and ((y-140.414)-((140.414-120.207)/(200-165))*(x-200) <= 0):
#     (x >= 165) #line l6 (hexagon)
#     ((y-59.586)-((59.586-79.793)/(200-165))*(x-200) >= 0) # line l7 (hexagon)
#     ((y-79.793)-((79.793-59.586)/(235-200))*(x-235) >= 0) # line l8 (hexagon)
#     (x <= 235) #line l9 (hexagon)
#     ((y-140.414)-((140.414-120.207)/(200-235))*(x-200) <= 0) # line l10 (hexagon)
#     ((y-140.414)-((140.414-120.207)/(200-165))*(x-200) <= 0) # line l11 (hexagon)
        return True
    else:
        return False

def outer_boundary(coordinates): #definition of boundary as an obstacle
    x = coordinates[0]
    y = coordinates[1]
    if (x <= 0) or (x >= 400) or (y <= 0) or (y >= 250):
        return True
    else:
        return False
    
def obstacle(coordinates): #checking all boundaries
    if (outer_boundary(coordinates) or arrow_obstacle1(coordinates) or arrow_obstacle2(coordinates) or circle_obstacle(coordinates) or hexagon_obstacle(coordinates)) == True:
        return True
    else:
        return False


input_start_x = input("Enter start position 'x' coordinate \n") #taking user input for start coordinates; reprompt if in obstacle
input_start_y = input("Enter start position 'y' coordinate \n")
input_start_coordinates = (int(input_start_x), int(input_start_y))
while obstacle(input_start_coordinates):
    print("The entered value is in the obstacle. Please enter new values\n")
    input_start_x = input("Enter start position 'x' coordinate \n")
    input_start_y = input("Enter start position 'y' coordinate \n")
    input_start_coordinates = (int(input_start_x), int(input_start_y))

input_goal_x = input("Enter goal position 'x' coordinate \n") #taking user input for goal coordinates; reprompt if in obstacle
input_goal_y = input("Enter goal position 'y' coordinate \n")
input_goal_coordinates = (int(input_goal_x), int(input_goal_y))
while obstacle(input_goal_coordinates):
    print("The entered value is in the obstacle. Please enter new values\n")
    input_goal_x = input("Enter goal position 'x' coordinate \n")
    input_goal_y = input("Enter goal position 'y' coordinate \n")
    input_goal_coordinates = (int(input_goal_x), int(input_goal_y))

a = [] #list to store x coordinates of visited nodes
b = [] #list to store y coordinates of visited nodes
initial_coordinates = input_start_coordinates
goal_coordinates = input_goal_coordinates

cost_to_come = 0
parent_coordinates = None
initial_node = (cost_to_come,(parent_coordinates),(initial_coordinates))
open_list = PriorityQueue()
closed_list_dict = {} #to store visited nodes
open_list.put(initial_node)

while True:
    current_node = open_list.get() #poppoing least cost from priority queue
    if current_node[2] in closed_list_dict: #if already in visited list go for next iteration or else continue
        continue
    a.append(current_node[2][0]) #appending respective values in the visited nodes
    b.append(current_node[2][1])
    closed_list_dict[current_node[2]] = (current_node[1]) #stroing current node info in visited dictionary with current coordinates as key
    if current_node[2] == goal_coordinates: #check for goal else move ahead
        print("Goal Reached")
        print(current_node)
        break
        #run backtrack function to find path
    else:
        #move left
        cost_to_come_left = current_node[0]+1
        parent_coordinates_left = current_node[2]
        x_new = current_node[2][0]-1
        y_new = current_node[2][1]
        new_coordinates = (x_new, y_new)
        if obstacle(new_coordinates) == False: #check obstacle
            if new_coordinates not in closed_list_dict: #check if not in visited dictionary
                left_node = (cost_to_come_left, parent_coordinates_left, new_coordinates)
                open_list.put(left_node) #add to priority queue

        #move right
        cost_to_come_right = current_node[0]+1
        parent_coordinates_right = current_node[2]
        x_new = current_node[2][0]+1
        y_new = current_node[2][1]
        new_coordinates = (x_new, y_new)
        if obstacle(new_coordinates) == False: #check obstacle, do similar steps for each action
            if new_coordinates not in closed_list_dict: #check if not in visited dictionary, do similar steps for each action
                right_node = (cost_to_come_right, parent_coordinates_right, new_coordinates)
                open_list.put(right_node) #add to priority queue, do similar steps for each action

        #move up
        cost_to_come_up = current_node[0]+1
        parent_coordinates_up = current_node[2]
        x_new = current_node[2][0]
        y_new = current_node[2][1]+1
        new_coordinates = (x_new, y_new)
        if obstacle(new_coordinates) == False:
            if new_coordinates not in closed_list_dict:
                up_node = (cost_to_come_up, parent_coordinates_up, new_coordinates)
                open_list.put(up_node)

        #move down
        cost_to_come_down = current_node[0]+1
        parent_coordinates_down = current_node[2]
        x_new = current_node[2][0]
        y_new = current_node[2][1]-1
        new_coordinates = (x_new, y_new)
        if obstacle(new_coordinates) == False:
            if new_coordinates not in closed_list_dict:
                down_node = (cost_to_come_down, parent_coordinates_down, new_coordinates)
                open_list.put(down_node)

        #move up left
        cost_to_come_up_left = current_node[0]+1.4
        parent_coordinates_up_left = current_node[2]
        x_new = current_node[2][0]-1
        y_new = current_node[2][1]+1
        new_coordinates = (x_new, y_new)
        if obstacle(new_coordinates) == False:
            if new_coordinates not in closed_list_dict:
                up_left_node = (cost_to_come_up_left, parent_coordinates_up_left, new_coordinates)
                open_list.put(up_left_node)

        #move up right
        cost_to_come_up_right = current_node[0]+1.4
        parent_coordinates_up_right = current_node[2]
        x_new = current_node[2][0]+1
        y_new = current_node[2][1]+1
        new_coordinates = (x_new, y_new)
        if obstacle(new_coordinates) == False:
            if new_coordinates not in closed_list_dict:
                up_right_node = (cost_to_come_up_right, parent_coordinates_up_right, new_coordinates)
                open_list.put(up_right_node)

        #move down left
        cost_to_come_down_left = current_node[0]+1.4
        parent_coordinates_down_left = current_node[2]
        x_new = current_node[2][0]-1
        y_new = current_node[2][1]-1
        new_coordinates = (x_new, y_new)
        if obstacle(new_coordinates) == False:
            if new_coordinates not in closed_list_dict:
                down_left_node = (cost_to_come_down_left, parent_coordinates_down_left, new_coordinates)
                open_list.put(down_left_node)

        #move down right
        cost_to_come_down_right = current_node[0]+1.4
        parent_coordinates_down_right = current_node[2]
        x_new = current_node[2][0]+1
        y_new = current_node[2][1]-1
        new_coordinates = (x_new, y_new)
        if obstacle(new_coordinates) == False:
            if new_coordinates not in closed_list_dict:
                down_right_node = (cost_to_come_down_right, parent_coordinates_down_right, new_coordinates)
                open_list.put(down_right_node)
    

#backtracking to find the path
shortest_path=[]
current = goal_coordinates
while current != initial_coordinates:
    shortest_path.append(current)
    current = closed_list_dict[current]
shortest_path.append(initial_coordinates)
shortest_path.reverse() #reversing the generated list


c = [] #to store respective values from generated path
d = []
for i in range(len(shortest_path)):
    c.append(shortest_path[i][0])
    d.append(shortest_path[i][1])

#printing the map
plt.ylabel('Y')
plt.xlabel('X')
plt.axis([0 , 400 , 0 ,250])
start_point = patch.Circle(input_start_coordinates, radius=2, color='m')
goal_point = patch.Circle(input_goal_coordinates, radius=2, color='m')




#printing the obstacles
# obs_patch1 = np.array([[36, 185], [105, 100], [80, 180], [115, 210]])
obs_patch1 = patch.Polygon(([36, 185], [105, 100], [80, 180], [115, 210]), color = 'r')
obs_patch2 = patch.RegularPolygon((200, 100), 6, radius = 40.415, color='g')
obs_patch3 = patch.Circle((300, 185), radius=40, color='b')
# p = Polygon(obs_patch1, closed=False, color='r')
ax = plt.gca()
ax.add_patch(obs_patch1)
ax.add_patch(obs_patch2)
ax.add_patch(obs_patch3)
ax.add_patch(start_point)
ax.add_patch(goal_point)
plt.savefig('Map1.png')
# plt.show


#printing the map exploration
temp_x = 0
temp_y = 0
plt.title("Plotting Visited list")
for i in range(len(a)) :
    ax.add_patch(start_point)
    ax.add_patch(goal_point)
    if temp_x == goal_coordinates[0] and temp_y == goal_coordinates[1] :
        break
    if len(a)>100:
        plt.scatter(a[0:100] , b[0:100] , c='mediumturquoise' , s=1)
        plt.pause(0.0005)
        del a[:100]
        del b[:100]
    else :
        for j in range(len(a)):
            plt.scatter(a[j] , b[j] , c='mediumturquoise' , s=1)
            plt.pause(0.0005)
            temp_x = a[j]
            temp_y = b[j]
            if a[j] == goal_coordinates[0] and b[j] == goal_coordinates[1] :
                break
plt.savefig('Map2.png')

#printing the travelled path
plt.title("Travelling on the Shortest Path")
for i in range(len(c)):
    plt.scatter(c[i] , d[i] , c='yellow' , s=2, marker='D')
    plt.pause(0.00005)
plt.pause(3)
plt.savefig('Map3.png')
plt.show