<!-- Download the zip file to a folder of your choice and extract the zip file

In it open the "Dijkstra.py" file in any IDE of your choice, preferably VS Code
Hit the run button in the IDE and the code will prompt you for inputs, give the necessary inputs
If acceptable inputs are given, the code will run and execute the Dijkstra algorithm and generate the shortest path
Once the path is generated, it will plot all the visited nodes and then the path of the travel
You can try for different inputs as required, as long as they are accepted by the program -->
# DIJKSTRA - Path Planning Algorithm for a Point Robot

The task was to designing a point robot that would traverse a map where the obstacels are already known to us. <br>
We have a point robot that can move in eight directions and each action would have its respective costs.
![Action Set](./images/Action_Set.jpg)

## Defining the map
We use the concepts of Algebraic Half planes to define the free space and the obstacles.<br>
![Obstacle Map](./images/Obstacle_Map.png)

## Exploring the Map
Use the defined actions set and as per the cost for each step, we traverse the graph
```
Action Sets = {(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1),(1,-1),(-1,-1)}
```
In each action set generated we check if the new position is going to end up in the obstacle space.
![Exploration Map](./images/Exploration_Map.png)

## Optimal path
After we explore the entire map, we use backtracking to find the path with the least cost. <br> The operation of the algorithm is shown below. <br>
![Shortest Path Map](./images/Shortest_Path_Map.png)

## Usage
Clone the repo to your local machine
```
git clone
```

[Video Output](images/Video_Output.mp4)