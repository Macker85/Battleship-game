import random


class GameBoard:
    """
    Stores the values for generating the game board.
    Dictionary for storing number and letters for game board.
    """
    def __init__(self, board):
        self.board = board

    @staticmethod
    def get_letters_to_numbers():
        letter_to_numbers = {
            "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
        return letter_to_numbers

    def print_game(self):
        print("  A B C D E F")
        print(" -------------")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    """
    Class that is used to generate ships.
    Also used to generate player guesses.
    Hits also confirmed in this class.
    """
    def __init__(self, board):
        self.board = board

    def deploy_fleet(self):
        """
        For statement loops through ships positions.
        Generates random integers and assigns 'X' as a ship in location.
        """
        for i in range(4):
            self.x_row, self.y_col = random.randint(0, 5), random.randint(0, 5)
            while self.board[self.x_row][self.y_col] == 'X':
                self.x_row = random.randint(0, 5)
                self.y_col = random.randint(0, 5)
            self.board[self.x_row][self.y_col] = 'X'
        return self.board

    def get_user_shot(self):
        """
        Takes the users input and checks validation.
        Returns the input as invalid or hit or miss.
        """
        try:
            y_col = input("Enter your first co-ordinate(A-F): ").upper()
            if y_col:
                while y_col not in "ABCDEF":
                    print("invalid co-ordinate, enter a letter A-F")
                    y_col = input("Enter the first co-ordinate(A-F): ").upper()
                    continue
            else:
                while not y_col:
                    print("Invalid Input. Enter a letter A-F.")
                    y_col = input("Enter Co-Ordinate (A-F): ").upper()
                    while y_col not in "ABCDEF":
                        print("Invalid co-ordinate. Enter a letter A-F.")
                        y_col = input("Enter Co-Ordinate (A-F): ").upper()
                    continue
            x_row = input("Enter your second co-ordinate(1-6): ")
            if x_row:
                while x_row not in "123456":
                    print("Invalid co-ordinate. Enter a number 1-6.")
                    x_row = input("Enter Co-Ordinate (1-6): ")
                    continue
            else:
                while not x_row:
                    print("Empty Input. Enter a number 1-6.")
                    x_row = input("Enter Co-Ordinate (1-6): ")
                    while x_row not in "123456":
                        print("Invalid co-ordinate. Enter a number 1-6.")
                        x_row = input("Enter Co-Ordinate (1-6): ")
                    continue
            return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_col]
        except ValueError and KeyError:
            print("Not a valid input. Enter a letter or a number.")
            return self.get_user_shot()

    def count_direct_hits(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        direct_hit = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    direct_hit += 1
        return direct_hit


def StartGame():
    enemy_board = GameBoard([[" "] * 6 for i in range(6)])
    player_board = GameBoard([[" "] * 6 for i in range(6)])
    Battleship.deploy_fleet(enemy_board)
    turns = 15
    while turns > 0:
        GameBoard.print_game(player_board)
        player_x_row, player_y_col = Battleship.get_user_shot(object)
        while player_board.board[player_x_row][player_y_col] == "-" or player_board.board[player_x_row][player_y_col] == "X":
            print("You have already destroyed this location")
            player_x_row, player_y_col = Battleship.get_user_shot(object)
        if enemy_board.board[player_x_row][player_y_col] == "X":
            print("That is a direct hit!")
            player_board.board[player_x_row][player_y_col] = "X"
        else:
            print("That is a miss!")
            player_board.board[player_x_row][player_y_col] = "-"
        if Battleship.count_direct_hits(player_board) == 4:
            print("You sunk all enemy battleships!")
            break
        else:
            turns -= 1
            print(f"you have {turns} turns remaining")
            if turns == 0:
                print("You have run out of ammunition")
                GameBoard.print_game(player_board)
                break


if __name__ == '__main__':
    StartGame()