import time

def main():
   start = time.time()
   solution1()
   end = time.time()
   print(end - start)

def solution2():
   file1 = open('day-6-data-test.txt', 'r')
   lantern_fish = []

   for line in file1:
      lantern_fish = [x for x in line.strip().split(",")]

   days = 1

   # lantern_fish = [[6, days]]
   # lantern_fish = [[int(fish), days] for fish in lantern_fish]

   count = 0
   start = time.time()
   while len(lantern_fish) != 0:
      # print(lantern_fish)
      current_fish = lantern_fish.pop()
      for day in range(0, current_fish[1]):
         if current_fish[0] == 0:
            current_fish[0] = 6
            lantern_fish.append([8, current_fish[1] - (day + 1)])
         else:
            current_fish[0] -= 1
         
      count += 1

      # print(count)

   # print(lantern_fish)
   # print(lantern_fish)
   print(count)


def solution1():
   file1 = open('day-6-data-test.txt', 'r')
   lantern_fish = []

   for line in file1:
      lantern_fish = [x for x in line.strip().split(",")]

   lantern_fish = [int(fish) for fish in lantern_fish]

   # create buckets
   fish_counters = [0, 0, 0, 0, 0, 0, 0, 0, 0]
   temp_fish_counters = [0, 0, 0, 0, 0, 0, 0, 0, 0]

   for fish in lantern_fish:
      fish_counters[fish] += 1

   for day in range(0, 256):
      # save index 0
      spawning_fish = fish_counters[0]
      for index in range(0, len(fish_counters)):
         if index == (len(fish_counters) - 1):
            # We've now moved every counter up. Handle the spawning fish.
            fish_counters[8] = spawning_fish
            fish_counters[6] = fish_counters[6] + spawning_fish
         else:
            fish_counters[index] = fish_counters[index + 1]
   
   sum = 0
   for counter in fish_counters:
      sum += counter
   print(sum)

if __name__ == "__main__":
   main()