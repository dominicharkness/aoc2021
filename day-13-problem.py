import time

def main():
   start = time.time()
   solution2()
   end = time.time()
   print(end - start)

def solution2():
   file1 = open('day-13-data-test.txt', 'r')
   paths = []

   reading_coordinates = True
   coordinates = []
   folding_instructions = []
   for line in file1:
      if line == "\n":
         reading_coordinates = False
      
      if reading_coordinates:
         coordinates.append([int(x) for x in line.strip().split(',')])
      elif line != "\n":
         folding_instructions.append(line.strip().split('='))
   
   # Figure out how big the grid needs to be
   max_x = 0
   max_y = 0
   for coordinate in coordinates:
      if coordinate[0] > max_x:
         max_x = coordinate[0]
      if coordinate[1] > max_y:
         max_y = coordinate[1]

   # create the grid
   grid = [[0 for i in range(0, max_x + 1)] for j in range(0, max_y + 1)]

   # populate the grid with coordinates
   for coordinate in coordinates:
      grid[coordinate[1]][coordinate[0]] = 1
   
   for instruction in folding_instructions:
      if instruction[0] == "fold along y":
         # create new grid
         y_axis = int(instruction[1])
         new_grid = [[0 for i in range(0, len(grid) + 1)] for j in range(0, y_axis)]

         row_index = 0
         for row in grid:
            if row_index < y_axis:
               # fill in above the fold
               new_grid[row_index] = row.copy()
            else:
               # fill in below the fold
               column_index = 0
               for column in row:
                  if column == 1:
                     new_grid[len(grid) - row_index - 1][column_index] = 1
                  column_index += 1
            row_index += 1

         grid = new_grid.copy()
      elif instruction[0] == "fold along x":
         # create new grid
         x_axis = int(instruction[1])
         new_grid = [[0 for i in range(0, x_axis)] for j in range(0, len(grid))]

         row_index = 0
         for row in grid:
            column_index = 0
            for column in row:
               if column_index < x_axis:
                  # fill in to the left of the fold
                  new_grid[row_index][column_index] = grid[row_index][column_index]
               else:
                  if column == 1:
                     new_grid[row_index][len(row) - column_index - 1] = 1
               column_index += 1
            row_index += 1
         
         grid = new_grid.copy()
   
   [print(row) for row in grid]

def solution1():
   file1 = open('day-13-data.txt', 'r')
   paths = []

   reading_coordinates = True
   coordinates = []
   folding_instructions = []
   for line in file1:
      if line == "\n":
         reading_coordinates = False
      
      if reading_coordinates:
         coordinates.append([int(x) for x in line.strip().split(',')])
      elif line != "\n":
         folding_instructions.append(line.strip().split('='))
   
   # Figure out how big the grid needs to be
   max_x = 0
   max_y = 0
   for coordinate in coordinates:
      if coordinate[0] > max_x:
         max_x = coordinate[0]
      if coordinate[1] > max_y:
         max_y = coordinate[1]

   # create the grid
   grid = [[0 for i in range(0, max_x + 1)] for j in range(0, max_y + 1)]

   # populate the grid with coordinates
   for coordinate in coordinates:
      grid[coordinate[1]][coordinate[0]] = 1
   
   # fold once
   # instruction = folding_instructions[0]
   # if instruction[0] == "fold along y":
   #    # create new grid
   #    y_axis = int(instruction[1])
   #    new_grid = [[0 for i in range(0, len(grid) + 1)] for j in range(0, y_axis)]

   #    row_index = 0
   #    for row in grid:
   #       if row_index < y_axis:
   #          # fill in above the fold
   #          new_grid[row_index] = row.copy()
   #       else:
   #          # fill in below the fold
   #          column_index = 0
   #          for column in row:
   #             if column == 1:
   #                new_grid[len(grid) - row_index - 1][column_index] = 1
   #             column_index += 1
   #       row_index += 1

   #    # count the 1s
   #    total_dots = sum([sum(row) for row in new_grid])
   #    print(total_dots)
   #    grid = new_grid.copy()
   #    new_grid.clear()
   
   # fold twice
   instruction = folding_instructions[0]
   if instruction[0] == "fold along x":
      # create new grid
      x_axis = int(instruction[1])
      new_grid = [[0 for i in range(0, x_axis)] for j in range(0, len(grid))]

      row_index = 0
      for row in grid:
         column_index = 0
         for column in row:
            if column_index < x_axis:
               # fill in to the left of the fold
               new_grid[row_index][column_index] = grid[row_index][column_index]
            else:
               if column == 1:
                  new_grid[row_index][len(row) - column_index - 1] = 1
            column_index += 1
         row_index += 1
      
      # [print(row) for row in new_grid]
      # count the 1s
      total_dots = sum([sum(row) for row in new_grid])
      print(total_dots)
   
   # [print(row) for row in grid]

if __name__ == "__main__":
   main()