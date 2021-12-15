import time

def main():
   start = time.time()
   solution2()
   end = time.time()
   print(end - start)

def solution2():
   file1 = open('day-12-data.txt', 'r')
   paths = []

   for line in file1:
      paths.append(line.strip().split('-'))
   
   route_count = 0
   for path in paths:
      if 'start' in path:
         # this path is a starting point
         start_index = path.index('start')
         if start_index == 0:
            end_index = 1
         elif start_index == 1:
            end_index = 0
         previously_visited = []
         route_count += findRoutes2(path[end_index], paths, previously_visited)
   
   print(route_count)

def findRoutes2(start, paths, previously_visited):
   route_count = 0
   temp_previously_visited = previously_visited.copy()
   if start.islower() and start != 'end':
      if start not in temp_previously_visited:
         temp_previously_visited.append(start)
      elif -1 not in temp_previously_visited:
         temp_previously_visited.append(-1)
      else:
         # The new starting point was in the list of previously visited, but we've already visited a cave twice
         return 0
   
   if (start == 'end'):
      route_count = 1
   else:
      for path in paths:
         if start in path:
            # our current cave is in this path. check if we've been to the connected cave before or if it leads back to the start.
            start_index = path.index(start)
            if start_index == 0:
               end_index = 1
            elif start_index == 1:
               end_index = 0
            
            if (path[end_index] not in previously_visited) and (path[end_index] != 'start'):
               # we haven't been here and it's not headed back to the start. Keep going!
               route_count += findRoutes2(path[end_index], paths, temp_previously_visited)
            elif (path[end_index] in previously_visited) and (path[end_index] != 'start') and (-1 not in previously_visited):
               route_count += findRoutes2(path[end_index], paths, temp_previously_visited)


   return route_count

def solution1():
   file1 = open('day-12-data.txt', 'r')
   paths = []

   for line in file1:
      paths.append(line.strip().split('-'))
   
   route_count = 0
   for path in paths:
      if 'start' in path:
         # this path is a starting point
         start_index = path.index('start')
         if start_index == 0:
            end_index = 1
         elif start_index == 1:
            end_index = 0
         previously_visited = []
         route_count += findRoutes(path[end_index], paths, previously_visited)
   
   print(route_count)

def findRoutes(start, paths, previously_visited):
   route_count = 0
   temp_previously_visited = previously_visited.copy()
   if start.islower() and start != 'end':
      temp_previously_visited.append(start)
   
   if (start == 'end'):
      route_count = 1
   else:
      for path in paths:
         if start in path:
            # our current cave is in this path. check if we've been to the connected cave before or if it leads back to the start.
            start_index = path.index(start)
            if start_index == 0:
               end_index = 1
            elif start_index == 1:
               end_index = 0
            
            if (path[end_index] not in previously_visited) and (path[end_index] != 'start'):
               # we haven't been here and it's not headed back to the start. Keep going!
               route_count += findRoutes(path[end_index], paths, temp_previously_visited)

   return route_count

if __name__ == "__main__":
   main()