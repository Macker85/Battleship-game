# Battleships

Battleships is a game of logic, with players attempting to sink each others fleet by guessing co-ordinates.
This version uses a a board generated using Python lists and incorporates a logic engine to allow the computer to fire back at the user.

(Developer: Stuart Wall)

![Start screen](docs/battleships_start.png)

[Live webpage](https://ci-pp3-battleships-clinelly.herokuapp.com/)

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
3. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [PEP8 validation](#pep8-validation)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgments](#acknowledgments)

## Project Goals 
The project goal is to create a logic game using Python.

### User Goals

The application user wants to play a logic game.

### Site Owner Goals
The Battleships game is played on grids on which each player's fleet of battleships are marked. The locations of the fleets are concealed from the other player. Players call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
The application provides a working battleships game for a single user to play against the computer.

## User Experience

### Target Audience
- Younger users who like playing games.
- Users who are looking for a game to pass time on during a break.
- Older users who are looking for a logic challenge.

### User Requirements and Expectations

### User Stories
1. To create a personal username.
2. To be able to return to the game with my username and password.
3. To have an immersive experience.
4. To have real-time feedback when playing the game.
5. To be able to play the game against a computer opponent.
6. To be told when the game has been won or lost.
7. To be able to easily replay the game if wanted.

## Technical Design

### Flowchart
<details><summary>Login</summary>
<img src="docs/logic_diagrams/login_chart.jpeg">
</details>
<details><summary>Game</summary>
<img src="docs/logic_diagrams/game_chart.jpeg">
</details>

### Data Modelling
- The data stored in the Google Spreadsheet is a combination of a username and password entered by the user on the login page.

- A new user will enter their choice of username and password which will be stored in the spreadsheet 'user_data_sheet' in the worksheet 'username'. Their password will be stored in the same spreadsheet but in the 'password' worksheet.

- A returning user will type in their username, the function will check the 'username' worksheet for a matching value and return a welcome message if true. The user will be prompted for a password and the function will, once again, check the 'password' worksheet for a matching value. If the function returns both inputs then the user will be allowed to play the game.

- If the returning user inputs do not match, the user will be taken to the start of the login function where they can try again or enter a new set of credentials.


## Technologies Used

### Languages
- Python 3

### Frameworks & Tools
- LucidChart
- Heroku
- Google Drive: Used as a cloud hosting platform for the spreadsheet.
- Google Spreadsheet: Used because Python does not have a built in library to store data in an external spreadsheet.
- pycodestyle: Used as a validation tool instead of pep8 online.
- gitHub
- Gitpod
- Git

## Features

### Welcome Message
- Shows a welcome message.
User Stories covered: 3, 4
<img src="docs/features/welcome_screen.png">

### Username/Password Input
- Prompts a user to input a username and password.
- Returning users can have their credentials recoved from a spreadsheet.
User Stories covered: 1,3
<img src="docs/features/username_password.png">

### Battleships Screen 
- Shows an ASCII art warship and logo.
User Stories covered: 3
<img src="docs/features/main_screen.png">

### Game Board
- Shows the generated game boards for the user and the computer.
User Stories covered: 3, 4, 5
<img src="docs/features/game_board.png">

### Game Inputs
- Allows the user to input their guesses and feedsback the result.
- Shows the computer's guess.
User Stories covered: 3, 4, 5
<img src="docs/features/game_inputs.png">

### Game Over
- Shows the end-of-game state to the user once a victory condition has been met.
- Allows user to retry the game or to quit the program.
User Stories covered: 4, 6, 7
<img src="docs/features/game_over.png">


## Validation

### PEP8 validation
At the time of creation, the PEP8 online Python validation website was inoperative. To validate the code, a PEP8 validator that is built into the GitPod Workspace was used.

1. Run the command 'pip3 install pycodestyle'. (Note that this extension may already be installed, in which case this command will do nothing.)
2. In the workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
3. Type the word 'linter' into the search bar that appears. 
4. Click on 'Python: Select Linter' from the filtered results.
5. Select 'pycodestyle' from the list.
6. PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside the terminal.

There were no errors or warnings flagged in login.py.
There were no errors or warnings flagged in test_login.py
15 yellow warnings were flagged in run.py. These are down to the symbol combinations used in the ASCII art and logo. These are printed direct to the console and not used in any functions.


### Testing user stories

1. To create a personal username.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Welcome Screen. | Input 'Y' to set up a new profile. Enter username. | Accepts input and stores username to spreadsheet. | Working as implemented. |

<details><summary>Welcome Screen</summary>
<img src="docs/user_testing/user_test_1_username.png">
</details>

2. To be able to return to the game with my username and password.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Welcome Screen. | Input 'N' and type in username and password. | Accepts input and checks spreadseet for the input values. | Working as implemented. 

<details><summary>Welcome Screen</summary>
<img src="docs/user_testing/user_test_2_return.png">
</details>

3. To have an immersive experience.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Welcome Screen. | Input username. | Console prints message welcoming the user as Admiral. | Working as implemented. |
| Main Screen. | Shows after user inputs username and password. | Console prints ASCII warship and game logo. | Working as implemented. |
| Game Board. | Generates upon game start. | Generates a board similar to the board game. | Working as implemented. |
| Game Inputs. | User inputs co-ordinates to fire on. | Feedback uses military terminology. | Working as implemented. |

<details><summary>Welcome Screen</summary>
<img src="docs/user_testing/user_test_3_welcome.png">
</details>
<details><summary>Main Screen</summary>
<img src="docs/user_testing/user_test_3_main_screen.png">
</details>
<details><summary>Game Board</summary>
<img src="docs/user_testing/user_test_3_boards.png">
</details>
<details><summary>Game Inputs</summary>
<img src="docs/user_testing/user_test_3_inputs.png">
</details>

4. To have real-time feedback when playing the game.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Welcome Screen. | Input username and password. | Console feedsback messages to user. | Working as implemented. |
| Game Board. | Generates at the start of the game and refreshes after every turn. | Game board is printed and updated with user and computer inputs after each turn. | Working as implemented. |
| Game Inputs. | User inputs their choice of co-ordinates. Computer does the same. | Results are printed back to the user after each turn. | Working as implemented. |

<details><summary>Welcome Screen</summary>
<img src="docs/user_testing/user_test_4_login.png">
</details>
<details><summary>Game Board</summary>
<img src="docs/user_testing/user_test_4_board.png">
</details>
<details><summary>Game Inputs</summary>
<img src="docs/user_testing/user_test_4_inputs.png">
</details>


5. To be able to play the game against a computer opponent.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Board. |  Generates at the start of the game and refreshes after every turn. | Game board is printed and updated with user and computer inputs after each turn. | Working as implemented. |
| Game Inputs. | Computer generates a shot after the user has taken a turn. | Results are updated on the board and printed back to the user after each computer turn. | Working as implemented. |

<details><summary>Game Board</summary>
<img src="docs/user_testing/user_test_5_board.png">
</details>
<details><summary>Game Inputs</summary>
<img src="docs/user_testing/user_test_5_input.png">
</details>


6. To be told when the game has been won or lost.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Inputs. | After a game over condition is met. | Game over condition is printed back to the user. | Working as implemented. |
| Game Over. | After a game over condition is met. | Results are updated on the board and printed back to the user after each computer turn. | Working as implemented. |

<details><summary>Game Inputs</summary>
<img src="docs/user_testing/user_test_6_inputs.png">
</details>
<details><summary>Game Over</summary>
<img src="docs/user_testing/user_test_6_game_over.png">
</details>

7. To be able to easily replay the game if wanted.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Over. | After a game over condition is met. User inputs Y or N | Input of Y re-runs the game. Input of N exits the program. | Working as implemented. |

<details><summary>Game Over</summary>
<img src="docs/user_testing/user_test_7_replay.png">
</details>

## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| New and Old User functions activated twice. | Moved the function calls to the Login function if/elif statements. |
| Missile counter decreased by two each round. | Seperated missile variable into two; one for the user and computer. |
| Check Login function would not validate user input. | Changed syntax of the Login function if/elif statements. |

## Deployment
Use the following steps to deploy the poject to Heroku:
1. Use the "pip freeze -> requiremnts.txt" command in the gitPod terminal; to save any libraries that need to be installed to the project files in Heroku.
2. Login or create a Heroku account.
3. Click the "New" button in the upper right corner and select "Create New App".
4. Choose an app name and your region and click "Create App". Note: the app name must be unique.
5. Go to the "Settings" tab, add the python build pack and then the node.js build pack. This is to ensure the project functions correctly with the Code Institute pre-installed template.
6. Create a "Config VAR" with the 'CREDS' key and the enter the value of the creds.json file.
7. Create a second "Config VAR" with the key of 'PORT' and value of '8000'
8. Go to the "Deploy" tab and pick GitHub as a deployment method.
9. Search for a repository to connect to.
10. Click enable automatic deploys and then deploy branch.
11. Wait for the app to build and then click on the "View" link.

You can fork the repository by following these steps:
1. Go to the GitHub repository.
2. Click on the Fork button in the upper right-hand corner.

You can clone the repository by following these steps:
1. Go to the GitHub repository.
2. Locate the Code button above the list of files and click it.
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard.
4. Open Git Bash.
5. Change the current working directory to the one where you want the cloned directory.
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY).
7. Press Enter to create your local clone.

## Credits

### Media
- ASCII art: https://asciiart.website/index.php?art=transportation/nautical

### Code
- Code Institute Python lessons.
- Code Institute Love Sandwiches project.
- Knowledge Mavens https://www.youtube.com/watch?v=alJH_c9t4zw&t=673s
- Corey Schafer https://www.youtube.com/watch?v=6tNS--WetLI

## Acknowledgments
I would like to take the opportunity to thank:
- My mentor Mo Shami for his feedback, advice, guidance and support.
- My beautiful wife, Megan, for her continued love and support.
- Jim, Sawyer, and the other fantasic members of Code Institute's community team.
- The great people of class June '22 for their ideas and humour.