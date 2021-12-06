def main():
   solution2()

def solution2():
   file1 = open('day-5-data.txt', 'r')
   lines = []
   w, h = 1000, 1000
   grid = [[0 for x in range(w)] for y in range(h)] 

   for line in file1:
      temp = [x for x in line.strip().split("-> ")]
      lines.append([x.strip().split(",") for x in temp])
      # print(line)
   
   for line in lines:
      # if x1 == x2
      if (line[0][0]) == (line[1][0]):
         for x in range(min(int(line[0][1]),int(line[1][1])), max(int(line[0][1]),int(line[1][1])) + 1):
            grid[x][int(line[0][0])] += 1
      # if y1 == y2
      elif (line[0][1]) == (line[1][1]):
         for x in range(min(int(line[0][0]), int(line[1][0])), max(int(line[0][0]), int(line[1][0])) + 1):
            grid[int(line[0][1])][x] += 1
      # 45 degree line (|x1 - x2| == |y1 - y2|)
      elif abs(int(line[0][0]) - int(line[1][0])) == abs(int(line[0][1]) - int(line[1][1])):
         # positive or negative slope?
         # print(line)
         if ((int(line[0][0]) < int(line[1][0])) and int(line[0][1]) < int(line[1][1])):
            # x1 < x2 and y1 < y2 so the slope is positive. Start at x1, y1 and work your way up.
            x = int(line[0][0])
            y = int(line[0][1])
            while x <= int(line[1][0]):
               grid[y][x] += 1
               x += 1
               y += 1
         if ((int(line[0][0]) > int(line[1][0])) and int(line[0][1]) < int(line[1][1])):
            # x1 > x2 and y1 < y2 so the slope is negative. Start at x1, y1 and work your way down.
            x = int(line[0][0])
            y = int(line[0][1])
            while x >= int(line[1][0]):
               grid[y][x] += 1
               x -= 1
               y += 1
         if ((int(line[0][0]) > int(line[1][0])) and int(line[0][1]) > int(line[1][1])):
            # x1 > x2 and y1 > y2 so the slope is negative. Start at x1, y1 and work your way down.
            x = int(line[0][0])
            y = int(line[0][1])
            while x >= int(line[1][0]):
               grid[y][x] += 1
               x -= 1
               y -= 1
         if ((int(line[0][0]) < int(line[1][0])) and int(line[0][1]) > int(line[1][1])):
            # x1 < x2 and y1 > y2 so the slope is negative. Start at x1, y1 and work your way down.
            x = int(line[0][0])
            y = int(line[0][1])
            while x <= int(line[1][0]):
               grid[y][x] += 1
               x += 1
               y -= 1
               
   
   count = 0
   for row in grid:
      for column in row:
         if column >= 2:
            count += 1   
      # print(row)
   
   print(count)

def solution1():
   file1 = open('day-5-data.txt', 'r')
   lines = []
   w, h = 1000, 1000
   grid = [[0 for x in range(w)] for y in range(h)] 

   for line in file1:
      temp = [x for x in line.strip().split("-> ")]
      lines.append([x.strip().split(",") for x in temp])
   
   for line in lines:
      # if x1 == x2
      if (line[0][0]) == (line[1][0]):
         for x in range(min(int(line[0][1]),int(line[1][1])), max(int(line[0][1]),int(line[1][1])) + 1):
            grid[x][int(line[0][0])] += 1
      # if y1 == y2
      elif (line[0][1]) == (line[1][1]):
         for x in range(min(int(line[0][0]), int(line[1][0])), max(int(line[0][0]), int(line[1][0])) + 1):
            grid[int(line[0][1])][x] += 1
   
   count = 0
   for row in grid:
      for column in row:
         if column >= 2:
            count += 1   
   
   print(count)



if __name__ == "__main__":
   main()