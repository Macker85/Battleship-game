import random

class GameBoard:
    def__init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        letter_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
        return letter_to_numbers

    def print_game(self):
        print(" A B C D E F G")
        print(" -------------")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number +=1

class Battleship:
    def __init__(self, board):
        self.board = board

    def make_ships(self):
        for i in range(4):
            self.x_row, self.y_col = random.randint(0, 5), random.randint(0, 5)
            while self.board[self.x_row][self.y_col] == 'X':
                self.board[self.x_row][self.y_col] = random.randint(0, 5), random.randint(0, 5)
            self.board[self.x_row][self.y_col] = 'X'
        return self.board


