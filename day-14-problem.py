import time

# B, C, F, H, K, N, O, P, S, V

def main():
   start = time.time()
   solution2()
   end = time.time()
   print(end - start)

def solution2():
   file1 = open('day-14-data-test.txt', 'r')

   count = 0
   template = ""
   rules = {}
   for line in file1:
      if count == 0:
         template = line.strip()
         print(template)
      elif line != "\n":
         rule = line.strip().split('->')
         rules[rule[0].strip()] = rule[1].strip()
      count += 1
   
   for rule in sorted(rules.keys()):
      print(rule + ":" + rules[rule])
   # # B, C, F, H, K, N, O, P, S, V
   # polymer_dictionary = {
   #    'B': 0,
   #    'C': 0,
   #    'F': 0,
   #    'H': 0,
   #    'K': 0,
   #    'N': 0,
   #    'O': 0,
   #    'P': 0,
   #    'S': 0,
   #    'V': 0
   # }

   # # initial counts
   # for char in template:
   #    polymer_dictionary[char] += 1

   # # For each pair
   # for count in range(0, len(template) - 1):
   #    findSubPairs2(template[count:(count + 2)], rules, 10, polymer_dictionary)
   #    print(count)
   
   # print(polymer_dictionary)
   # print(max(polymer_dictionary.items(), key=lambda x: x[1])[1] - min(polymer_dictionary.items(), key=lambda x: x[1])[1])

def findSubPairs2(pair, rules, step, counts):
   if step != 0 :
      counts[rules[pair]] += 1
      findSubPairs2(pair[0] + rules[pair], rules, step - 1, counts)
      findSubPairs2(rules[pair] + pair[1], rules, step - 1, counts)

def findSubPairs(pair, rules, step, counts):
   if step != 0 :
      for rule in rules:
         if pair == rule[0]:
            counts[rule[1]] += 1
            findSubPairs(pair[0] + rule[1], rules, step - 1, counts)
            findSubPairs(rule[1] + pair[1], rules, step - 1, counts)

def solution1():
   file1 = open('day-14-data.txt', 'r')

   count = 0
   template = ""
   rules = []
   for line in file1:
      if count == 0:
         template = line.strip()
         print(template)
      elif line != "\n":
         rules.append([x.strip() for x in line.strip().split('->')])
      count += 1
   
   # B, C, F, H, K, N, O, P, S, V
   polymer_dictionary = {
      'B': 0,
      'C': 0,
      'F': 0,
      'H': 0,
      'K': 0,
      'N': 0,
      'O': 0,
      'P': 0,
      'S': 0,
      'V': 0
   }

   # initial counts
   for char in template:
      polymer_dictionary[char] += 1

   # For each pair
   for count in range(0, len(template) - 1):
      findSubPairs(template[count:(count + 2)], rules, 10, polymer_dictionary)
   
   print(polymer_dictionary)
   print(max(polymer_dictionary.items(), key=lambda x: x[1])[1] - min(polymer_dictionary.items(), key=lambda x: x[1])[1])

if __name__ == "__main__":
   main()