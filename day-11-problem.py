import time

def main():
   start = time.time()
   solution2()
   end = time.time()
   print(end - start)

def solution2():
   file1 = open('day-11-data.txt', 'r')
   energy_levels = []

   for line in file1:
      energy_levels.append([int(x) for x in line.strip()])

   flash_count = 0
   for step in range(0, 300):
      # Before each step, cache the flash count
      previous_flash_count = flash_count
      for row in range(0, len(energy_levels)):
         for column in range(0, len(energy_levels[row])):
            flash_count += flashOctopus(row, column, energy_levels)
      
      # After we've gone through the map, we need to unflag our flashed octopus
      # again so they start counting energy levels
      for row in range(0, len(energy_levels)):
         for column in range(0, len(energy_levels[row])):
            if energy_levels[row][column] == -1:
               energy_levels[row][column] = 0
      
      # After each step, check to see if all the octopus flashed
      if ((flash_count - previous_flash_count) == 100):
         break
   
   print(step + 1)

def solution1():
   file1 = open('day-11-data.txt', 'r')
   energy_levels = []

   for line in file1:
      energy_levels.append([int(x) for x in line.strip()])

   flash_count = 0
   for step in range(0, 100):
      for row in range(0, len(energy_levels)):
         for column in range(0, len(energy_levels[row])):
            flash_count += flashOctopus(row, column, energy_levels)
      
      # After we've gone through the map, we need to unflag our flashed octopus
      # again so they start counting energy levels
      for row in range(0, len(energy_levels)):
         for column in range(0, len(energy_levels[row])):
            if energy_levels[row][column] == -1:
               energy_levels[row][column] = 0
   
   print(flash_count)

def flashOctopus(row, column, map):
   flash_count = 0
   if map[row][column] != -1:
      map[row][column] += 1

   if map[row][column] > 9:
      map[row][column] = -1
      # Flash this octopus
      flash_count += 1
      # Above
      if row > 0:
         # Above and to the left
         if column > 0:
            flash_count += flashOctopus(row - 1, column - 1, map)
         
         # Above and to the right
         if column < len(map[row]) - 1:
            flash_count += flashOctopus(row - 1, column + 1, map)
         
         # Above middle
         flash_count += flashOctopus(row - 1, column, map)
      
      # Below
      if row < len(map) - 1:
         # Below to the left
         if column > 0:
            flash_count += flashOctopus(row + 1, column - 1, map)
         
         # Below to the right
         if column < len(map[row]) - 1:
            flash_count += flashOctopus(row + 1, column + 1, map)
         
         # Below middle
         flash_count += flashOctopus(row + 1, column, map)
      
      # Left
      if column > 0:
         flash_count += flashOctopus(row, column - 1, map)
      
      # Right
      if column < len(map[row]) - 1:
         flash_count += flashOctopus(row, column + 1, map)
      
   return flash_count


if __name__ == "__main__":
   main()