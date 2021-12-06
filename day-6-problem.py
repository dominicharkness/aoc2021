import time

def main():
   start = time.time()
   solution2()
   end = time.time()
   print(end - start)

def solution2():
   file1 = open('day-6-data.txt', 'r')
   lantern_fish = []

   for line in file1:
      lantern_fish = [int(x) for x in line.strip().split(",")]

   # create buckets
   fish_counters = [0, 0, 0, 0, 0, 0, 0, 0, 0]

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

   print(sum(fish_counters))


def solution1():
   file1 = open('day-6-data.txt', 'r')
   lantern_fish = []

   for line in file1:
      lantern_fish = [x for x in line.strip().split(",")]

   lantern_fish = [int(fish) for fish in lantern_fish]

   for day in range(0, 80):
      count = 0
      fish_to_add = 0
      for fish in lantern_fish:
         if lantern_fish[count] == 0:
            lantern_fish[count] = 6
            fish_to_add += 1
         else:
            lantern_fish[count] -= 1
         count += 1
      
      for new_fish in range(0, fish_to_add):
         lantern_fish.append(8)
      
      # print(lantern_fish)
   
   print(len(lantern_fish))

if __name__ == "__main__":
   main()