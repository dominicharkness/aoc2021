def main():
   solution2()

def solution1():
   file1 = open('day-2-data.txt', 'r')
   horizontal_position = 0
   depth = 0

   for line in file1:
      command = line.split()
      if (command[0] == 'forward'):
         horizontal_position += int(command[1])
      elif (command[0] == 'down'):
         depth += int(command[1])
      elif (command[0] == 'up'):
         depth -= int(command[1])
   
   print(horizontal_position)
   print(depth)
   print(horizontal_position * depth)

def solution2():
   file1 = open('day-2-data.txt', 'r')
   horizontal_position = 0
   depth = 0
   aim = 0

   for line in file1:
      command = line.split()
      if (command[0] == 'forward'):
         horizontal_position += int(command[1])
         depth += (aim * int(command[1]))
      elif (command[0] == 'down'):
         aim += int(command[1])
      elif (command[0] == 'up'):
         aim -= int(command[1])
   
   print(horizontal_position)
   print(depth)
   print(aim)
   print(horizontal_position * depth)
   
if __name__ == "__main__":
   main()