def main():
   solution2()

def solution2():
   file1 = open('day-1-data.txt', 'r')
   count = 0
   increased_count = 0
   previous_sum = 0
   current_sum = 0
   window = [0, 0, 0]
   window_index = 0

   for line in file1:
      window[window_index] = int(line.strip())
      window_index += 1
      if window_index == 3:
         window_index = 0
      previous_sum = current_sum
      current_sum = sum(window)
      
      if count > 2:
         if previous_sum < current_sum:
            increased_count += 1

      count += 1
   print(increased_count)



def solution1():
   file1 = open('day-1-data.txt', 'r')
   count = 0
   increased_count = 0
   previous_value = 0
   

   for line in file1:
      current_value = int(line.strip())
      if count != 0:
         if previous_value < current_value:
            increased_count += 1
      count += 1
      previous_value = current_value
   
   print(increased_count)


   
if __name__ == "__main__":
   main()