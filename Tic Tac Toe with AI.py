import random
import os
from playsound import playsound

def sum(a, b, c):
    return a + b + c

def play_sound(file_name):
    sound_dir = r"E:\Tic Tac Toe with AI\Sound Effects"
    sound_path = os.path.join(sound_dir, file_name)
    try:
        playsound(sound_path)
    except Exception as e:
        print(f"🔇 Could not play sound: {e}")

def printBoard(xState, zState):
    symbols = []
    for i in range(9):
        if xState[i]:
            symbols.append('X')
        elif zState[i]:
            symbols.append('O')
        else:
            symbols.append(str(i))
    print("\n")
    print(f" {symbols[0]} | {symbols[1]} | {symbols[2]} ")
    print("---|---|---")
    print(f" {symbols[3]} | {symbols[4]} | {symbols[5]} ")
    print("---|---|---")
    print(f" {symbols[6]} | {symbols[7]} | {symbols[8]} ")
    print("\n")

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            return 'X'
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            return 'O'
    return None

def isDraw(xState, zState):
    return all(x or z for x, z in zip(xState, zState))

def getValidInput(xState, zState, name):
    while True:
        try:
            value = int(input(f"{name}, enter a position (0-8): "))
            if value < 0 or value > 8:
                print("⚠️ Enter a number between 0 and 8.")
                play_sound("error.mp3")
            elif xState[value] or zState[value]:
                print("⚠️ This position is already taken.")
                play_sound("error.mp3")
            else:
                return value
        except ValueError:
            print("⚠️ Invalid input. Use numbers only.")
            play_sound("error.mp3")

def getComputerMove(xState, zState, computer_symbol):
    player_symbol = 'O' if computer_symbol == 'X' else 'X'

    def evaluate(xState, zState):
        winner = checkWin(xState, zState)
        if winner == computer_symbol:
            return 1
        elif winner == player_symbol:
            return -1
        elif isDraw(xState, zState):
            return 0
        return None

    def minimax(xState, zState, is_maximizing):
        result = evaluate(xState, zState)
        if result is not None:
            return result

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if not xState[i] and not zState[i]:
                    if computer_symbol == 'X':
                        xState[i] = 1
                    else:
                        zState[i] = 1
                    score = minimax(xState, zState, False)
                    if computer_symbol == 'X':
                        xState[i] = 0
                    else:
                        zState[i] = 0
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if not xState[i] and not zState[i]:
                    if player_symbol == 'X':
                        xState[i] = 1
                    else:
                        zState[i] = 1
                    score = minimax(xState, zState, True)
                    if player_symbol == 'X':
                        xState[i] = 0
                    else:
                        zState[i] = 0
                    best_score = min(score, best_score)
            return best_score

    best_move = None
    best_score = -float('inf')
    for i in range(9):
        if not xState[i] and not zState[i]:
            if computer_symbol == 'X':
                xState[i] = 1
            else:
                zState[i] = 1
            score = minimax(xState, zState, False)
            if computer_symbol == 'X':
                xState[i] = 0
            else:
                zState[i] = 0
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def save_score_to_file(score):
    with open("scores.txt", "w") as f:
        for name, points in score.items():
            f.write(f"{name}: {points}\n")

def playHumanVsComputer(score):
    player_name = input("Enter your name: ").strip()
    while True:
        player_symbol = input(f"{player_name}, do you want to be X or O? ").upper()
        if player_symbol in ['X', 'O']:
            break
        else:
            print("❌ Invalid choice. Please choose X or O.")

    computer_symbol = 'O' if player_symbol == 'X' else 'X'
    print(f"{player_name} is {player_symbol}. Computer is {computer_symbol}.\n")

    while True:
        xState = [0] * 9
        zState = [0] * 9
        turn = 1 if player_symbol == 'X' else 0

        while True:
            printBoard(xState, zState)
            if (turn == 1 and player_symbol == 'X') or (turn == 0 and player_symbol == 'O'):
                print(f"{player_name}'s Turn")
                value = getValidInput(xState, zState, player_name)
                if player_symbol == 'X':
                    xState[value] = 1
                else:
                    zState[value] = 1
            else:
                print("Computer's Turn...")
                value = getComputerMove(xState, zState, computer_symbol)
                print(f"Computer chose position {value}")
                if computer_symbol == 'X':
                    xState[value] = 1
                else:
                    zState[value] = 1

            winner = checkWin(xState, zState)
            if winner:
                printBoard(xState, zState)
                if winner == player_symbol:
                    print(f"🏆 {player_name} ({winner}) won!")
                    play_sound("win.mp3")
                    score[player_name] = score.get(player_name, 0) + 1
                else:
                    print(f"🤖 Computer ({winner}) won!")
                    play_sound("win.mp3")
                    score["Computer"] = score.get("Computer", 0) + 1
                break
            if isDraw(xState, zState):
                printBoard(xState, zState)
                print("🤝 It's a draw!")
                play_sound("draw.mp3")
                score["Draws"] = score.get("Draws", 0) + 1
                break
            turn = 1 - turn

        again = input("Do you want to play another round? (y/n): ").lower()
        if again != 'y':
            break

def playHumanVsHuman(score):
    player1_name = input("Enter Player 1 name: ").strip()
    player2_name = input("Enter Player 2 name: ").strip()
    while True:
        player1_symbol = input(f"{player1_name}, do you want to be X or O? ").upper()
        if player1_symbol in ['X', 'O']:
            break
        else:
            print("❌ Invalid choice. Please choose X or O.")

    player2_symbol = 'O' if player1_symbol == 'X' else 'X'
    print(f"{player1_name} is {player1_symbol}. {player2_name} is {player2_symbol}.\n")

    while True:
        xState = [0] * 9
        zState = [0] * 9
        turn = 1 if player1_symbol == 'X' else 0

        while True:
            printBoard(xState, zState)
            if (turn == 1 and player1_symbol == 'X') or (turn == 0 and player1_symbol == 'O'):
                print(f"{player1_name}'s Turn")
                value = getValidInput(xState, zState, player1_name)
                if player1_symbol == 'X':
                    xState[value] = 1
                else:
                    zState[value] = 1
            else:
                print(f"{player2_name}'s Turn")
                value = getValidInput(xState, zState, player2_name)
                if player2_symbol == 'X':
                    xState[value] = 1
                else:
                    zState[value] = 1

            winner = checkWin(xState, zState)
            if winner:
                printBoard(xState, zState)
                if winner == player1_symbol:
                    print(f"🏆 {player1_name} ({winner}) won!")
                    play_sound("win.mp3")
                    score[player1_name] = score.get(player1_name, 0) + 1
                else:
                    print(f"🏆 {player2_name} ({winner}) won!")
                    play_sound("win.mp3")
                    score[player2_name] = score.get(player2_name, 0) + 1
                break
            if isDraw(xState, zState):
                printBoard(xState, zState)
                print("🤝 It's a draw!")
                play_sound("draw.mp3")
                score["Draws"] = score.get("Draws", 0) + 1
                break
            turn = 1 - turn

        again = input("Do you want to play another round? (y/n): ").lower()
        if again != 'y':
            break

def mode_selection():
    print("🎮 Welcome to Advanced Tic Tac Toe!")
    print("Select Game Mode:")
    print("1. Human vs Computer")
    print("2. Human vs Human")
    while True:
        choice = input("Enter 1 or 2 to start: ")
        if choice == '1':
            return 'computer'
        elif choice == '2':
            return 'human'
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

def showFinalScore(score):
    print("\n📊 Final Scoreboard:")
    for player, points in score.items():
        print(f"{player}: {points}")
    save_score_to_file(score)
    print("🏑 Scores saved to scores.txt. Thanks for playing!")

def main():
    score = {}
    while True:
        mode = mode_selection()
        if mode == 'computer':
            playHumanVsComputer(score)
        elif mode == 'human':
            playHumanVsHuman(score)

        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            showFinalScore(score)
            break

if __name__ == "__main__":
    main()
