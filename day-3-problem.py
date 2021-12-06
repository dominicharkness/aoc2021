BIT_ONE_MASK = 0x800
BIT_TWO_MASK = 0x400
BIT_THREE_MASK = 0x200
BIT_FOUR_MASK = 0x100
BIT_FIVE_MASK = 0x080
BIT_SIX_MASK = 0x040
BIT_SEVEN_MASK = 0x020
BIT_EIGHT_MASK = 0x010
BIT_NINE_MASK = 0x008
BIT_TEN_MASK = 0x004
BIT_ELEVEN_MASK = 0x002
BIT_TWELVE_MASK = 0x001

BIT_MASKS = [BIT_ONE_MASK, BIT_TWO_MASK, BIT_THREE_MASK, BIT_FOUR_MASK, BIT_FIVE_MASK, BIT_SIX_MASK, BIT_SEVEN_MASK, BIT_EIGHT_MASK, BIT_NINE_MASK, BIT_TEN_MASK, BIT_ELEVEN_MASK, BIT_TWELVE_MASK]

def main():
   solution2()

def solution1():
   # numbers are 12-bit
   file1 = open('day-3-data.txt', 'r')
   one_count = [0,0,0,0,0,0,0,0,0,0,0,0]
   zero_count = [0,0,0,0,0,0,0,0,0,0,0,0]

   for line in file1:
      encoded_value = int(line.split()[0], 2)
      current_bit = 0
      for bit_mask in BIT_MASKS :
         if encoded_value & bit_mask != 0:
            one_count[current_bit] += 1
         else:
            zero_count[current_bit] += 1
         current_bit += 1
   
   bit_position = 0
   most_common_bit = [0,0,0,0,0,0,0,0,0,0,0,0]
   least_common_bit = [0,0,0,0,0,0,0,0,0,0,0,0]
   for count in one_count:
      if one_count[bit_position] > zero_count[bit_position]:
         most_common_bit[bit_position] = 1
      else:
         least_common_bit[bit_position] = 1
      bit_position += 1

   # print(most_common_bit)
   # print(least_common_bit)
   
   print(one_count)
   print(zero_count)
   gamma_rate = int(''.join(str(bit) for bit in most_common_bit), 2)
   epsilon_rate = int(''.join(str(bit) for bit in least_common_bit), 2)
   print(gamma_rate * epsilon_rate)

def solution2():
   # numbers are 12-bit
   file1 = open('day-3-data.txt', 'r')
   encoded_values = []

   for line in file1:
      encoded_value = int(line.split()[0], 2)
      encoded_values.append(encoded_value)
   
   oxygen_generator_rating = filterListUsingMostCommon(encoded_values, 0)[0]
   print(oxygen_generator_rating)
   co2_scrubber_rating = filterListUsingLeastCommon(encoded_values, 0)[0]
   print(co2_scrubber_rating)

   print(oxygen_generator_rating * co2_scrubber_rating)

def filterListUsingMostCommon(encoded_values, bit_position):
   new_list = []
   if len(encoded_values) == 1:
      return encoded_values

   most_common_bit = determineMostCommonBit(encoded_values, bit_position)
   # print(most_common_bit)

   for value in encoded_values:
      if most_common_bit == 1:
         if value & BIT_MASKS[bit_position] != 0:
            new_list.append(value)
      else:
         if value & BIT_MASKS[bit_position] == 0:
            new_list.append(value)
   return filterListUsingMostCommon(new_list, bit_position + 1)

def filterListUsingLeastCommon(encoded_values, bit_position):
   new_list = []
   if len(encoded_values) == 1:
      return encoded_values

   least_common_bit = determineLeastCommonBit(encoded_values, bit_position)
   # print(least_common_bit)

   for value in encoded_values:
      if least_common_bit == 1:
         if value & BIT_MASKS[bit_position] != 0:
            new_list.append(value)
      else:
         if value & BIT_MASKS[bit_position] == 0:
            new_list.append(value)
   return filterListUsingLeastCommon(new_list, bit_position + 1)

def determineMostCommonBit(encoded_values, bit_position):
   one_count = 0
   zero_count = 0
   for encoded_value in encoded_values:
      if encoded_value & BIT_MASKS[bit_position] != 0:
         one_count += 1
      else:
         zero_count += 1
   if one_count >= zero_count:
      return 1
   else:
      return 0

def determineLeastCommonBit(encoded_values, bit_position):
   one_count = 0
   zero_count = 0
   for encoded_value in encoded_values:
      if encoded_value & BIT_MASKS[bit_position] != 0:
         one_count += 1
      else:
         zero_count += 1
   if one_count >= zero_count:
      return 0
   else:
      return 1

if __name__ == "__main__":
   main()