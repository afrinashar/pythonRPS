import random

def play(player1, player2, num_games, verbose=False):
    p1_score = 0
    p2_score = 0
    prev_play1 = ""
    prev_play2 = ""

    for _ in range(num_games):
        move1 = player1(prev_play2)
        move2 = player2(prev_play1)

        prev_play1 = move1
        prev_play2 = move2

        if move1 == move2:
            pass
        elif (move1 == "R" and move2 == "S") or \
             (move1 == "P" and move2 == "R") or \
             (move1 == "S" and move2 == "P"):
            p1_score += 1
        else:
            p2_score += 1

        if verbose:
            print(f"Player1: {move1}  Player2: {move2}")

    win_rate = p1_score / num_games * 100
    print(f"Player1 win rate: {win_rate}%")
    return win_rate


# ---------------------------------------
# Bots
# ---------------------------------------

def quincy(prev_play, counter=[0]):
    moves = ["R", "R", "P", "P", "S"]
    move = moves[counter[0] % len(moves)]
    counter[0] += 1
    return move


def abbey(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    if not opponent_history:
        return random.choice(["R", "P", "S"])

    most_common = max(set(opponent_history), key=opponent_history.count)
    return {"R": "P", "P": "S", "S": "R"}[most_common]


def kris(prev_play):
    if prev_play == "":
        return random.choice(["R", "P", "S"])
    return prev_play


def mrugesh(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < 10:
        return random.choice(["R", "P", "S"])

    last_10 = opponent_history[-10:]
    most_common = max(set(last_10), key=last_10.count)
    return {"R": "P", "P": "S", "S": "R"}[most_common]
