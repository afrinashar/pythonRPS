import random

def player(prev_play, opponent_history=[]):
    # Reset history at the start of a new match
    if prev_play == "":
        opponent_history.clear()

    # Store opponent move
    opponent_history.append(prev_play)

    # First move → random
    if len(opponent_history) <= 1:
        return random.choice(["R", "P", "S"])

    # Helper function to counter a move
    def counter(move):
        return {"R": "P", "P": "S", "S": "R"}[move]

    # -----------------------------------
    # Strategy 1: Pattern Detection
    # -----------------------------------
    pattern_length = 4  # works well for Quincy & others

    if len(opponent_history) > pattern_length:
        recent_pattern = opponent_history[-pattern_length:]

        # Search previous occurrences of this pattern
        for i in range(len(opponent_history) - pattern_length - 1):
            if opponent_history[i:i+pattern_length] == recent_pattern:
                predicted_move = opponent_history[i+pattern_length]
                return counter(predicted_move)

    # -----------------------------------
    # Strategy 2: Counter opponent's most frequent move
    # -----------------------------------
    move_counts = {
        "R": opponent_history.count("R"),
        "P": opponent_history.count("P"),
        "S": opponent_history.count("S")
    }

    predicted_move = max(move_counts, key=move_counts.get)

    return counter(predicted_move)
