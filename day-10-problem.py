import time

def main():
   start = time.time()
   solution2()
   end = time.time()
   print(end - start)

def solution2():
   file1 = open('day-10-data.txt', 'r')
   nav_system = []
   for line in file1:
      nav_system.append([x for x in line.strip()])

   incomplete_lines = []
   for line in nav_system: 
      corrupted_char = detectCorruptedLine(line)
      if corrupted_char == '':
         incomplete_lines.append(line)
   
   scores = []
   for line in incomplete_lines:
      scores.append(calculateCompletionScore(findCompletionCharacters(line)))
   middle_index = (len(scores) - 1)/2
   scores.sort()
   print(scores[int(middle_index)])

def calculateCompletionScore(closing_chars):
   running_score = 0
   while len(closing_chars) != 0:
      char = closing_chars.pop()
      running_score *= 5
      if char == ')':
         running_score += 1
      elif char == ']':
         running_score += 2
      elif char == '}':
         running_score += 3
      elif char == '>':
         running_score += 4
   return running_score

def findCompletionCharacters(line):
   expected_closing_chars = []
   for char in line:
      if len(expected_closing_chars) == 0:
         # we havent seen any opens yet... expect one
         appendClosingChar(char, expected_closing_chars)
      else:
         if char == ')' or char == ']' or char == '}' or char == '>':
            expected_closing_chars.pop()
         else:
            # must be an open char, add its closer to the list
            appendClosingChar(char, expected_closing_chars)
   return expected_closing_chars

def solution1():
   file1 = open('day-10-data.txt', 'r')
   nav_system = []
   for line in file1:
      nav_system.append([x for x in line.strip()])
   
   score = 0
   for line in nav_system: 
      corrupted_char = detectCorruptedLine(line)
      if corrupted_char != '':
         score += calculateScore(corrupted_char)
   print(score)

def calculateScore(char):
   if char == ')':
      return 3
   elif char == ']':
      return 57
   elif char == '}':
      return 1197
   elif char == '>':
      return 25137

def detectCorruptedLine(line):
   expected_closing_chars = []
   for char in line:
      if len(expected_closing_chars) == 0:
         # we havent seen any opens yet... expect one
         appendClosingChar(char, expected_closing_chars)
      else:
         if char == ')' or char == ']' or char == '}' or char == '>':
            if char != expected_closing_chars.pop():
               return char
         else:
            # must be an open char, add its closer to the list
            appendClosingChar(char, expected_closing_chars)
   return ''

def appendClosingChar(open_char, closing_char_list):
   if open_char == '(':
      closing_char_list.append(')')
   elif open_char == '[':
      closing_char_list.append(']')
   elif open_char == '{':
      closing_char_list.append('}')
   elif open_char == '<':
      closing_char_list.append('>')

if __name__ == "__main__":
   main()