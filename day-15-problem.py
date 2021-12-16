import time
import sys

def main():
   start = time.time()
   solution1()
   end = time.time()
   print(end - start)

def solution1():
    file1 = open('day-15-data-test.txt', 'r')
    paths = []

    risk_levels = []
    for line in file1:
        risk_levels.append([int(x) for x in line.strip()])
    
    vertices = len(risk_levels) * len(risk_levels[0])

    distances = [sys.maxsize] * vertices
    distances[0] = 0
    spt_set = [False] * vertices

    for row in risk_levels:
        for column in row:
            min_vertex_index = minDistance(vertices, distances, spt_set)
            spt_set[min_vertex_index] = True

            for row2 in risk_levels:
                for column2 in row2:
                    vertex2 = (row2 + 1)*(column2 + 1) + 1
                    # calculate cost to get to each reachable node (above, below, left, right) and add that to distances[min_vertex_index]
                    # if that's < the cost of distances[vertex2], then dist[vertex2] = dist[min_vertex_index] + cost to reach min(above, below, left, right)

            vertex = (row + 1) * (column + 1) - 1
            

    [print(row) for row in risk_levels]

def minDistance(vertices, distances, spt_set):
    min_distance = sys.maxsize
    for vertex in range(vertices):
        if distances[vertex] < min_distance and spt_set[vertex] == False:
            min_distance = distances[vertex]
            min_index = vertex
    return min_index

if __name__ == "__main__":
   main()