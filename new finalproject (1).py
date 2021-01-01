import turtle
import time
from copy import deepcopy
import random

def checker(board, letter):
    return ((board["a1"] == board["a2"] == board["a3"] == letter) or
            (board["b1"] == board["b2"] == board["b3"] == letter) or
            (board["c1"] == board["c2"] == board["c3"] == letter) or
            (board["a1"] == board["b1"] == board["c1"] == letter) or
            (board["a2"] == board["b2"] == board["c2"] == letter) or
            (board["a3"] == board["b3"] == board["c3"] == letter) or
            (board["a1"] == board["b2"] == board["c3"] == letter) or
            (board["a3"] == board["b2"] == board["c1"] == letter))


def marker_placement(board):
    try:
        t.speed(0)
        marker_x = 0
        for i in list(deepcopy(board)):
            if board[i] != " ":
                y_values = {'a': 270, 'b': 70, 'c': -130}
                for letter in ["a", "b", "c"]:
                    if i[0] == letter:
                        marker_y = y_values[letter]
                        if i[1] == "1":
                            marker_x = -225
                        elif i[1] == "2":
                            marker_x = -25
                        elif i[1] == "3":
                            marker_x = 175
                t.hideturtle()
                t.up()
                t.goto(marker_x, marker_y)
                t.down()
                if board[i] == "X":
                    t.color("red")
                    t.write("X", font=("arial", 50))
                    t.color("black")
                elif board[i] == "O":
                    t.color("blue")
                    t.write("O", font=("arial", 50))
                    t.color("black")
                t.up()
    except Exception:
        pass



def cpu_turn(board, cpu_choice, user_choice, difficulty):
    global count
    count = count + 1
    if difficulty != 3:
        for i in board.keys():
            copy_board = deepcopy(board)
            if copy_board[i] == " ":
                copy_board[i] = cpu_choice
                if checker(copy_board, cpu_choice) == True:
                    board[i] = cpu_choice
                    return True
        for i in board.keys():
            copy_board = deepcopy(board)
            if copy_board[i] == " ":
                copy_board[i] = user_choice
                if checker(copy_board, user_choice) == True:
                    board[i] = cpu_choice
                    return False
        if difficulty == 1:
            corners_of_board = ["a1", "a3", "c1", "c3"]
            for corner in corners_of_board:
                if board[corner] == " ":
                    board[corner] = cpu_choice
                    return False
                else:
                    continue
            if board["b2"] == " ":
                board["b2"] = cpu_choice
                return False

            sides_of_board = ["b1", "a2", "b3", "c2"]
            for side in sides_of_board:
                if board[side] == " ":
                    board[side] = cpu_choice
                    return False
                else:
                    continue
    if difficulty == 3 or difficulty == 2:
        temp_board_list = list(deepcopy(board))
        while True:
            randomized_location = random.choice(temp_board_list)
            if board[randomized_location] == " ":
                board[randomized_location] = cpu_choice
                break


def get_mouse_click_coor(x, y):
    global location, count, turn, winner, potential_winner
    potential_winner = "User"
    if not winner or count < 9:
        if turn:
            turn = False
            if y >= -200:
                if 200 <= y <= 400:
                    letter = "a"
                elif 0 <= y <= 199:
                    letter = "b"
                elif -200 <= y <= -1:
                    letter = "c"
                if 100 <= x <= 300:
                    location = letter + "3"
                elif -100 <= x <= 99:
                    location = letter + "2"
                elif -300 <= x <= -101:
                    location = letter + "1"
            if board[location] == ' ':
                board[location] = user_choice
                marker_placement(board)
                count = count + 1
                winner = checker(board, user_choice)
                if winner:
                    replay_menu()

                else:
                    if count == 9 and winner == False:
                        potential_winner = "Tie"
                        replay_menu()

                    potential_winner = "CPU"
                    cpu_turn(board, cpu_choice, user_choice, difficulty)
                    time.sleep(0.5)
                    marker_placement(board)
                    winner = checker(board, cpu_choice)
                    if winner:
                        replay_menu()
                    else:
                        if count == 9 and winner == False:
                            potential_winner = "Tie"
                            replay_menu()
                    turn = True
            else:
                turn = True

def quitgame():
    turtle.Screen().bye()
    exit()

def replay_menu():
    turtle.clearscreen()
    t.up()
    turtle.bgcolor("light green")
    if potential_winner == "Tie":
        t.goto(-70, 50)
        t.write("It's a tie!", font=("arial", 25))
    else:
        t.goto(-240, 50)
        t.write("  And the winner is... the %s!" % potential_winner, font=("arial", 25))
    time.sleep(1)
    turtle.listen()
    t.goto(-200, -100)
    t.write("Click 'y' to rerun the game\n                    or\n              'q' to quit", font=("arial", 25))
    turtle.onkey(maingame, "y")
    turtle.onkey(quitgame, "q")
    turtle.done()


def instructions():
    t = turtle.Pen()
    turtle.clearscreen()
    turtle.bgcolor("light salmon")
    t.goto(-250, -200)
    t.write("                 INSTRUCTIONS: \n\n\n The goal of the game is to match\n"
            "three of your selected marker (X or O)\n"
            " in a row. However, the programed CPU \n"
            "Player will be competing against you\n"
            "also trying to get 3 markers in a row\n"
            "and blocking your markers. If you nor\n"
            " the CPU player can match 3 markers in\n"
            "a row and the board is full, the game\n"
            " ends as a tie! You place markers by\n"
            "clicking the corresponding grid spot with\n"
            "your mouse. For more, follow the on-screen\n"
            "instructions later provided.\n\n\n  Click 'r' to return to the home screen!", font=("comic sans", 20))

    turtle.listen()
    turtle.onkey(main_menu, "r")

t = turtle.Pen()
winner = "Tie"


def maingame():
    global winner, t, user_choice, cpu_choice, count, difficulty, turn, location, board
    t = turtle.Pen()
    turtle.setup(600, 800)
    turtle.clearscreen()
    turtle.bgcolor("wheat")
    t.speed(0)
    t.up()
    for i in range(2):
        t.goto(-100, -200)
        t.down()
        t.goto(-100, 600)
        t.up()
    t.goto(100, -200)
    t.down()
    t.goto(100, 600)
    t.up()
    t.goto(-300, 200)
    t.down()
    t.goto(300, 200)
    t.up()
    t.goto(-300, 0)
    t.down()
    t.goto(300, 0)
    t.up()
    t.goto(-300, -200)
    t.down()
    t.goto(300, -200)
    t.up()

    count = 0
    board = {'a1': " ", 'a2': " ", 'a3': " ",
             'b1': " ", 'b2': " ", 'b3': " ",
             'c1': " ", 'c2': " ", 'c3': " "}
    location = ' '

    screen = turtle.Screen()

    difficulty = "0"
    while difficulty not in [1, 2, 3]:
        try:
            difficulty = int(
                screen.textinput("", "What difficulty do you want to play on?\n 1 = Hard, 2 = Medium, 3 = Easy"))
        except Exception:
            continue

    user_choice = ""
    cpu_choice = ""
    while user_choice not in ["x", "o"]:
        user_choice = screen.textinput("", "Will your marker be X's or O's?\n Type 'x' or 'o'")
    user_choice = user_choice.upper()
    if user_choice == "X":
        cpu_choice = "O"
    else:
        cpu_choice = "X"

    starter = random.choice(["User", "CPU"])
    who_starts = turtle.Pen()
    who_starts.hideturtle()
    who_starts.up()
    who_starts.goto(0, 70)
    who_starts.dot(500, "gray")
    who_starts.goto(-175, 50)
    who_starts.write("%s Starts" % starter, font=("arial", 50))
    time.sleep(1)
    who_starts.clear()

    turn = False
    if starter == "CPU":
        cpu_turn(board, cpu_choice, user_choice, difficulty)
        marker_placement(board)
        turn = True
    else:
        turn = True

    winner = False

    t = turtle.Pen()
    t.hideturtle()
    turtle.onscreenclick(get_mouse_click_coor)
    turtle.mainloop()


def gamestart():
    global t, count, board, location, winner
    turtle.clearscreen()
    t.hideturtle()
    t.up()
    maingame()

def main_menu():
    turtle.clearscreen()
    turtle.setup(600, 800)
    turtle.bgcolor("light blue")
    t.hideturtle()
    turtle.hideturtle()
    t.up()
    t.speed(0)
    t.goto(-200, 200)
    t.write("TIC TAC TOE\n  By: Ash. S", font=("comic sans", 50, "bold"))
    t.goto(-210, -20)
    t.write('  Click "i" for Instructions\n                     Or\n            "s" to start!',
            font=("comic sans", 25, "bold"))
    turtle.listen()
    turtle.onkey(instructions, 'i')
    turtle.onkey(gamestart, "s")

main_menu()
turtle.done()

