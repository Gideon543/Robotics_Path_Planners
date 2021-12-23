from testCase5 import *
from testCase4 import *
from testCase3 import *
from testCase2 import *
from testCase1 import *

'''
1. Get the starting node.
2. Check if the node is within the specified boundaries and is not visited.
4. Update the node by adding one to it.
3. Find the neighbours of the node and append them to the queue (fringe)

'''

# Wavefront algorithm for path planning.
def wavefront (startGoal, endGoal, graph, adjacency):
    fringe = []
    visited = []

# Determine the boundaries of the graph to prevent index-out-of-range error
    columnBoundary = len(graph[0])
    rowBoundary = len(graph)

# Set the value of the root node to 2   
    graph[endGoal[0]][endGoal[1]] = 2
    fringe.append(endGoal)

# BFS implmentation - Get non-one neighbours for each node as long as they are within the boundaries.
# Also update their with the value of their parent node plus 1.
    while fringe != []:
        currentNode = fringe.pop(0)
        neighbours = neighbourConnectivity(currentNode, adjacency) # specify the neighbour-connectivity

        for move in neighbours:
            if (0 <= move[0] < rowBoundary) and (0 <= move[1] < columnBoundary): # Check boundaries for each adjacent node
            # Update the node if it is free
                if graph[move[0]][move[1]] == 0:
                    graph[move[0]][move[1]] = graph[currentNode[0]][currentNode[1]] + 1
            
            # Mark node as visisted   
                if move not in visited and graph[move[0]][move[1]] !=1:
                    visited.append(move)
                    fringe.append(move)

    displayUpdatedGraph(graph)
    path = findPath(graph,rowBoundary,columnBoundary, startGoal, adjacency)           
    return path

# Return the 8 adjacent neighbours of the current node if adjacency is True, and 4 if False
def neighbourConnectivity (currentNode, adjacency):
    if adjacency == True:
        return [
            (currentNode[0] - 1 , currentNode[1] -1),(currentNode[0] - 1 , currentNode[1] +1),(currentNode[0] + 1 , currentNode[1] -1),
            (currentNode[0] + 1 , currentNode[1] +1),(currentNode[0] - 1 , currentNode[1] +0),(currentNode[0] + 1 , currentNode[1] +0), 
            (currentNode[0] + 0 , currentNode[1] -1),(currentNode[0] - 0 , currentNode[1] +1)
        ]
    return [
            (currentNode[0] - 1 , currentNode[1] +0),(currentNode[0] + 1 , currentNode[1] +0), 
            (currentNode[0] + 0 , currentNode[1] -1),(currentNode[0] - 0 , currentNode[1] +1)
        ]


# DFS implementation - Recursively finds nodes with values less than their parent's value until the end goal is reached.
def findPath(graph, rowBoundary, columnBoundary, start_goal, adjacency):
    fringe = []
    fringe.append(start_goal)
    visited = []
    while fringe != []:
         currentNode = fringe.pop()
         neighbours = neighbourConnectivity(currentNode, adjacency) # Get neighbours of parent/current node.
         for move in neighbours:
             if move not in visited:
                 if (0 <= move[0] < rowBoundary) and (0 <= move[1] < columnBoundary):
                 # When neighbour's value is less than parent's by one, add it to the fringe and mark it as vistited.    
                    if graph[move[0]][move[1]] == graph[currentNode[0]][currentNode[1]] - 1 and graph[move[0]][move[1]] >= 2:
                        visited.append(move)
                        fringe.append(move)
    return visited         

    
def displayUpdatedGraph(matrix):
    for item in matrix:
        print(item)


# Testing the algorithm

# When both end and start goals are on the same column of the graph but with obstacle between them
graph1 = wavefront(start_goal1, end_goal1, world_map1, adjacency1)
print(graph1)
print()

# When both end and start goals are on the same column of the graph
graph2 = wavefront(start_goal2, end_goal2, world_map2, adjacency2)
print(graph2)
print()

# When end and start goals are at the opposite corners of the graph
graph3 = wavefront(start_goal3, end_goal3, world_map3, adjacency3)
print(graph3)
print()

# When both end goals are in the middle region - (8 neighbour connectivity)
graph4 = wavefront(start_goal4, end_goal4, world_map4, adjacency4)
print(graph4)
print()

# When start and endgoals are at the corners of the graph - (8 neighbour connectivity)
graph5 = wavefront(start_goal5, end_goal5, world_map5, adjacency5)
print(graph5)
print()

