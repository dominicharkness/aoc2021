import time

def main():
   start = time.time()
   solution2()
   end = time.time()
   print(end - start)

def solution2():
   # this took 3 minutes to run on my computer which means it probably wasn't the
   # "correct" solution, but meh
   file1 = open('day-7-data.txt', 'r')
   crab_positions = []

   for line in file1:
      crab_positions = [int(x) for x in line.strip().split(",")]

   # print(crab_positions)
   print(min(crab_positions))
   print(max(crab_positions))

   min_position_and_fuel_cost = [0, 0]
   count = 0
   for position in range(min(crab_positions), max(crab_positions)):
      fuel = 0
      for crab in crab_positions:
         fuel_cost = 0
         for i in range(min([position, crab]), max([position, crab])):
            fuel_cost += ((i + 1) - min([position, crab]))
         fuel += fuel_cost
      if count == 0:
         # first iteration, save the result
         min_position_and_fuel_cost = [position, fuel]
      elif min_position_and_fuel_cost[1] > fuel:
         # new minimum
         min_position_and_fuel_cost = [position, fuel]
      count += 1
      print(position)
   
   print(min_position_and_fuel_cost)

def solution1():
   file1 = open('day-7-data.txt', 'r')
   crab_positions = []

   for line in file1:
      crab_positions = [int(x) for x in line.strip().split(",")]

   min_position_and_fuel_cost = [0, 0]
   count = 0
   for position in range(min(crab_positions), max(crab_positions)):
      fuel = 0
      for crab in crab_positions:
         fuel += abs(position - crab)
      if count == 0:
         # first iteration, save the result
         min_position_and_fuel_cost = [position, fuel]
      elif min_position_and_fuel_cost[1] > fuel:
         # new minimum
         min_position_and_fuel_cost = [position, fuel]
      count += 1
   
   print(min_position_and_fuel_cost)

if __name__ == "__main__":
   main()