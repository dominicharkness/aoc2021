def main():
   solution2()

def solution2():
   file1 = open('day-4-data.txt', 'r')
   count = 0
   drawn_numbers = []
   current_board = []
   boards = []

   for line in file1:
      if count == 0:
         drawn_numbers = [int(x) for x in line.strip().split(",")]
         print(drawn_numbers)
      elif line != "\n":
         current_board.append([int(x) for x in line.strip().split()])
      else:
         boards.append(current_board[:][:])
         current_board.clear()
      count += 1
   
   # draw the numbers
   for number in drawn_numbers:
      # mark boards
      count = 0
      for board in boards:
         markBoard(number, boards[count])
         count += 1

      # check for bingos
      count = 0
      for board in boards:
         if checkBingo(boards[count]):
            print("BINGO")
            if (len(boards) == 2):
               # The last board has bing
               scoreBoard(boards[count], number)
               return
            else:
               del boards[count]
               continue
         else:
            print("NOT BINGO")
         count += 1
      
   print(number)
   print(len(boards))
   print(boards)


def solution1():
   file1 = open('day-4-data.txt', 'r')
   count = 0
   drawn_numbers = []
   current_board = []
   boards = []

   for line in file1:
      if count == 0:
         drawn_numbers = [int(x) for x in line.strip().split(",")]
         print(drawn_numbers)
      elif line != "\n":
         current_board.append([int(x) for x in line.strip().split()])
      else:
         boards.append(current_board[:][:])
         current_board.clear()
      count += 1
   
   # draw the numbers
   for number in drawn_numbers:
      count = 0
      for board in boards:
         markBoard(number, board)
         if checkBingo(board):
            print("BINGO")
            scoreBoard(board, number)
            return
         count += 1
      print ("NOT_BINGO")

def markBoard(number, board):
   row_count = 0
   for row in board:
      column_count = 0
      for column in row:
         if column == number:
            board[row_count][column_count] = 'x'
         column_count += 1
      row_count += 1

def checkBingo(marked_board):
   # check rows
   for row in marked_board:
      row_total = 0
      for column in row:
         if column == 'x':
            row_total += 1
         if row_total == 5:
            #bingo!
            return True
   
   # check columns
   for column in range(5):
      column_total = 0
      # print(marked_board)
      for row in marked_board:
         if row[column] == 'x':
            column_total += 1
         if column_total == 5:
            #bingo!
            return True

def scoreBoard(board, number):
   print(board)
   sum = 0
   for row in board:
      for column in row:
         if column != 'x':
            sum += column
   print(sum)
   print(number)
   print(sum * number)

if __name__ == "__main__":
   main()