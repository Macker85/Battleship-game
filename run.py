import random

import colorama
from colorama import Fore, Back
colorama.init()

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("CREDS.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("battleship usernames")

username = SHEET.worksheet("usernames")

MARKER = '~' * 45


def login():
    """
    Loads login and welcome screen.
    Asks user if they have played the game before.
    Looks for username and password, checks if correct.
    """
    while True:
        print(MARKER)
        print("           Welcome to Battleship")
        print("        A game of logic and chance")
        print("   Deploy your fleet and prepare for battle")
        print("Board size 6 x 6. Ships to sink = 5. turns 20 ")
        print(MARKER)
        return_player = input("Have you played before? Y/N \n").upper()

        if str(return_player) == 'Y':
            known_player()
        elif str(return_player) == 'N':
            new_player()

        if validate_user(return_player):
            break
    return return_player


def validate_user(return_player: str):
    """
    Checks for acceptable input
    Alert error if not
    return_player (str): user input
    """
    try:
        str(return_player)
        if return_player not in {"y", "n"}:
            raise ValueError("Invalid entry.")
    except ValueError as e:
        print(f"{e} entry must be Y/N. Please try again.")
        return False

    return True


def new_player():
    """
    Directs player to create username and password.
    Stores input in Google Sheet.
    """
    user_login = SHEET.worksheet("usernames")
    pass_login = SHEET.worksheet("passwords")
    new_user = input("\nUsername: \n")
    user_list = str.split(new_user)
    user_login.append_row(user_list)
    print(f"Welcome {new_user}, good luck")
    new_pass = input("Enter password:\n")
    pass_list = str.split(new_pass)
    pass_login.append_row(pass_list)
    print("Password saved.\n")
    start_game()


def known_player():
    """
    Return user must enter username and password.
    Checks value against info stored in Google Sheet.
    If invalid, return to log in.
    """
    user_login = SHEET.worksheet("usernames")
    pass_login = SHEET.worksheet("passwords")
    known_user = input("\nUsername: \n")
    check_known = user_login.find(known_user)
    if check_known is None:
        print("User not found, please check your details and try again.\n")
        login()
    else:
        print(f"Welcome back {known_user}.\n")
    known_pass = input("Password: \n")
    check_pass = pass_login.find(known_pass)
    if check_pass is None:
        print("Password incorrect, please try again.\n")
        login()
    else:
        print("Password verified.")
    start_game()


class GameBoard:
    """
    Stores the values for generating the game board.
    Dictionary for storing number and letters for game board.
    """
    def __init__(self, board):
        self.board = board

    @staticmethod
    def get_letters_to_numbers():
        """
        converts letter to numbers to read in terminal
        Returns converted numbers
        """
        letter_to_numbers = {
            "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
        return letter_to_numbers

    def print_game(self):
        """
        prints out board and adds colour to terminal.
        """
        print(f"\n{Fore.CYAN}{Back.BLACK}  A B C D E F ")
        print(" ^^^^^^^^^^^^^")
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
        for i in range(5):
            self.x_row, self.y_col = random.randint(0, 5), random.randint(0, 5)
            self.board[self.x_row][self.y_col] = '@'
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
                    y_col = input("Enter Co-Ordinate (A-F): \n").upper()
                    while y_col not in "ABCDEF":
                        print("Invalid co-ordinate. Enter a letter A-F.")
                        y_col = input("Enter Co-Ordinate (A-F): ").upper()
                    continue
            x_row = input("Enter your second co-ordinate(1-6): \n")
            if x_row:
                while x_row not in "123456":
                    print("Invalid co-ordinate. Enter a number 1-6.")
                    x_row = input("Enter Co-Ordinate (1-6): ")
                    continue
            else:
                while not x_row:
                    print("Empty Input. Enter a number 1-6.")
                    x_row = input("Enter Co-Ordinate (1-6): \n")
                    while x_row not in "123456":
                        print("Invalid co-ordinate. Enter a number 1-6.")
                        x_row = input("Enter Co-Ordinate (1-6): \n")
                    continue
            return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_col]
        except ValueError and KeyError:
            print("Not a valid input. Enter a letter or a number.")
            return self.get_user_shot()

    def get_enemy_shot(self):
        """
        Generates computer guess.
        Taken from random integer and letter.
        Returns guess co-ordinate
        """
        y_col = random.choice([
            "A", "B", "C", "D", "E", "F"
        ]).upper()
        x_row = random.randint(0, 5)
        return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_col]

    def count_direct_hits(self):
        """
        Confirms hit with location 'X'
        Returns a direct hit on a battleship
        """
        direct_hit = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    direct_hit += 1
        return direct_hit


def start_game():
    """
    Lauch game.
    Generate player board and enemy board.
    Load ships.
    Defines turn limit
    """
    enemy_board = GameBoard([[" "] * 6 for i in range(6)])
    enemy_target_board = GameBoard([[" "] * 6 for i in range(6)])
    player_board = GameBoard([[" "] * 6 for i in range(6)])
    player_target_board = GameBoard([[" "] * 6 for i in range(6)])
    Battleship.deploy_fleet(enemy_board)
    Battleship.deploy_fleet(player_board)
    turns = 20
    enemy_turns = 20
    while turns > 0:
        GameBoard.print_game(player_target_board)
        GameBoard.print_game(enemy_target_board)
        player_x_row, player_y_col = Battleship.get_user_shot(object)
        while (
            player_target_board.board[player_x_row][player_y_col] == "-"
            or player_target_board.board[player_x_row][player_y_col] == "X"
        ):
            print("You have already destroyed this location")
            player_x_row, player_y_col = Battleship.get_user_shot(object)
        if player_board.board[player_x_row][player_y_col] == "@":
            print("That is a direct hit!")
            player_target_board.board[player_x_row][player_y_col] = "X"
        else:
            print("That is a miss!")
            player_target_board.board[player_x_row][player_y_col] = "-"
            turns -= 1
        if Battleship.count_direct_hits(player_target_board) == 5:
            print("You sunk all enemy battleships!")
            break
        print(f"you have {turns} turns remaining")
        if turns == 0:
            print("You have run out of ammunition")
            GameBoard.print_game(player_target_board)
        enemy_x_row, enemy_y_col = Battleship.get_enemy_shot(object)
        while (
            enemy_target_board.board[enemy_x_row][enemy_y_col] == "-"
            or enemy_target_board.board[enemy_x_row][enemy_y_col] == "X"
        ):
            enemy_x_row, enemy_y_col = Battleship.get_enemy_shot(object)
        if enemy_board.board[enemy_x_row][enemy_y_col] == "@":
            print("The enemy has sunk one of your ships!")
            enemy_target_board.board[enemy_x_row][enemy_y_col] = "X"
        else:
            print("The enemy has missed!")
            enemy_target_board.board[enemy_x_row][enemy_y_col] = "-"
            enemy_turns -= 1
        if Battleship.count_direct_hits(enemy_target_board) == 5:
            print("Your fleet has been destroyed!")
            break
        if turns == 0:
            print("The enemy is out of ammunition.")
            GameBoard.print_game(enemy_target_board)
    end_game()


def end_game() -> str:
    """
    Runs well ships are sunk.
    Runs when turns run out.
    Asks user to play again or exit.
    """
    print("Game over!")
    play_again = input("Play again? Y/N: \n").upper()

    if str(play_again) == 'Y':
        start_game()
    elif str(play_again) == 'N':
        print("Thank you for playing, see you next time.")
        quit()
    elif str(play_again) not in {"Y", "N"}:
        print("please enter Y/N.")
        end_game()


if __name__ == '__main__':
    login()