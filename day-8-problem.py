import time

def main():
   start = time.time()
   solution2()
   end = time.time()
   print(end - start)

def solution2():
   file1 = open('day-8-data.txt', 'r')
   signal_wire_info = []

   for line in file1:
      signal_wire_info.append([x.split() for x in line.strip().split("|")])
   
   digits_index = 0
   output_index = 1
   total = 0
   for info in signal_wire_info:
      # print (info[digits_index])
      total += decode_entry(info[digits_index], info[output_index])
   
   print(total)


def decode_entry(digits, output):
   # 0:      1:      2:      3:      4:
   #  aaaa    ....    aaaa    aaaa    ....
   # b    c  .    c  .    c  .    c  b    c
   # b    c  .    c  .    c  .    c  b    c
   #  ....    ....    dddd    dddd    dddd
   # e    f  .    f  e    .  .    f  .    f
   # e    f  .    f  e    .  .    f  .    f
   #  gggg    ....    gggg    gggg    ....

   #   5:      6:      7:      8:      9:
   #  aaaa    aaaa    aaaa    aaaa    aaaa
   # b    .  b    .  .    c  b    c  b    c
   # b    .  b    .  .    c  b    c  b    c
   #  dddd    dddd    ....    dddd    dddd
   # .    f  e    f  .    f  e    f  .    f
   # .    f  e    f  .    f  e    f  .    f
   #  gggg    gggg    ....    gggg    gggg
   decoded_digits = ["","","","","","","","","","",]
   for digit in digits:
      if len(digit) == 2:
         # one
         decoded_digits[1] = digit
      elif len(digit) == 4:
         # four
         decoded_digits[4] = digit
      elif len(digit) == 3:
         # seven
         decoded_digits[7] = digit
      elif len(digit) == 7:
         # eight
         decoded_digits[8] = digit

   # now we know our base values... let's deduce
   for digit in digits:
      if len(digit) == 5:
         # two, three, or five
         if len(set(digit) & set(decoded_digits[7])) == 3:
            # three
            decoded_digits[3] = digit
         elif len(set(digit) & set(decoded_digits[4])) == 3:
            # five
            decoded_digits[5] = digit
         else:
            # two
            decoded_digits[2] = digit
      elif len(digit) == 6:
         # zero, six, or nine
         if len(set(decoded_digits[7]) & set(digit)) == 2:
            # six
            decoded_digits[6] = digit
         elif len(set(decoded_digits[4]) & set(digit)) == 4:
            # nine
            decoded_digits[9] = digit
         else:
            # zero
            decoded_digits[0] = digit
   
   output_ints = [0, 0, 0, 0]
   output_index = 0
   for digit in output:
      decoded_index = 0
      for decoded_digit in decoded_digits:
         if len(set(digit) & set(decoded_digit)) == len(set(decoded_digit)) == len(set(digit)):
            output_ints[output_index] = decoded_index
         decoded_index += 1
      output_index += 1

   output_strings = [str(i) for i in output_ints]
   return int("".join(output_strings))


def solution1():
   file1 = open('day-8-data.txt', 'r')
   signal_wire_info = []

   for line in file1:
      signal_wire_info.append([x.split() for x in line.strip().split("|")])
   
   output_index = 1
   count = 0
   for info in signal_wire_info:
      for output_digit in info[output_index]:
         if (len(output_digit) == 2) or (len(output_digit) == 3) or (len(output_digit) == 4) or (len(output_digit) == 7):
            count += 1

   print(count)

if __name__ == "__main__":
   main()