# === Simon Says · sequence memory game ===
# Repeat the growing color sequence to score points.

import random

# These are the colors that can appear in the game
colors = ("red", "blue", "green", "yellow")
sequence = []
score = 0

print("=== Simon Says ===")
print("Repeat the growing sequence using spaces or commas.")
print("Available colors: red, blue, green, yellow. Enter q to quit.")

while True:
    # Add one new color to the sequence for this round
    sequence.append(random.choice(colors))
    print(f"\nRound {len(sequence)} — remember this sequence:")
    print(" -> ".join(sequence))

    # Ask again if the player enters a color that is not in the game
    while True:
        answer = input("Repeat the colors: ").lower().replace(",", " ").split()
        if answer == ["q"]:
            answer = None
            break
        if answer and all(color in colors for color in answer):
            break
        print("Use red, blue, green, or yellow.")

    # Stop if the player chooses to quit
    if answer is None:
        print(f"You quit with a score of {score}.")
        break

    # Compare the entire guess with the sequence
    if answer != sequence:
        print(f"Wrong sequence! It was: {' -> '.join(sequence)}")
        print(f"Game over. Your score: {score}")
        break

    score += 1
    print("Correct! Get ready for the next round.")
