import random

class GameBoard:
    def __init__(self, board):
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

    def get_user_shot(self):
        try:
            x_row = input("Enter a row number on board:")
            while x_row not in '123456':
                print("Not a valid input, please enter a row number on board:")

                y_col = input("Enter a column letter on board:").upper()
            return int(x_row) -1, GameBoard.get_letters_to_numbers()[y_col]
        except ValueError and KeyError:
            print("Not a valid input, please enter a column letter on board:")
            return self.get_user_shot()
