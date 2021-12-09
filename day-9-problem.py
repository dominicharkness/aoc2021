import time
import numpy as np

def main():
   start = time.time()
   solution2()
   end = time.time()
   print(end - start)

def solution2():
   file1 = open('day-9-data.txt', 'r')
   heightmap = []

   for line in file1:
      heightmap.append([int(x) for x in line.strip()])

   biggest_basins = [0, 0, 0]
   for row in range(0, len(heightmap)):
      for column in range(0, len(heightmap[row])):
         if isLowPoint(row, column, heightmap):
            basin_size = calculateBasinSize(row, column, heightmap)
            if basin_size > min(biggest_basins):
               biggest_basins.remove(min(biggest_basins))
               biggest_basins.append(basin_size)
   
   print(np.prod(biggest_basins))
   
def calculateBasinSize(row, column, heightmap):
   count = 1
   heightmap[row][column] = -1
   if row > 0:
      if heightmap[row - 1][column] != 9 and heightmap[row - 1][column] != -1:
         count += calculateBasinSize(row - 1, column, heightmap)
   if row < len(heightmap) - 1:
      if heightmap[row + 1][column] != 9 and heightmap[row + 1][column] != -1:
         count += calculateBasinSize(row + 1, column, heightmap)
   if column > 0:
      if heightmap[row][column - 1] != 9 and heightmap[row][column - 1] != -1:
         count += calculateBasinSize(row, column - 1, heightmap)
   if column < len(heightmap[row]) - 1:
      if heightmap[row][column + 1] != 9 and heightmap[row][column + 1] != -1:
         count += calculateBasinSize(row, column + 1, heightmap)
   
   return count

def isLowPoint(row, column, heightmap):
   height = heightmap[row][column]
   # check above
   low_point = True
   if row > 0:
      if height >= heightmap[row - 1][column]:
         low_point = False
   # check below
   if row < len(heightmap) - 1:
      if height >= heightmap[row + 1][column]:
         low_point = False
   # check left
   if column > 0:
      if height >= heightmap[row][column - 1]:
         low_point = False
   # check right
   if column < len(heightmap[row]) - 1:
      if height >= heightmap[row][column + 1]:
         low_point = False
   
   return low_point

def solution1():
   file1 = open('day-9-data.txt', 'r')
   heightmap = []

   for line in file1:
      heightmap.append([int(x) for x in line.strip()])

   risk = 0
   num_low_points = 0
   for row in range(0, len(heightmap)):
      for column in range(0, len(heightmap[row])):
         if isLowPoint(row, column, heightmap):
            risk += (1 + heightmap[row][column])
            num_low_points += 1

   print(num_low_points)
   print(risk)

if __name__ == "__main__":
   main()