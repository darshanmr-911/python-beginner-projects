import random

COLORS = ("red", "blue", "green", "yellow")


def parse_guess(answer):
    """Return the guessed colors, or None when the player chooses to quit."""
    guess = answer.lower().replace(",", " ").split()
    if guess == ["q"]:
        return None
    if not guess or any(color not in COLORS for color in guess):
        raise ValueError("Use red, blue, green, or yellow.")
    return guess


def play_game():
    sequence = []
    score = 0

    print("\nRepeat each growing color sequence in the same order.")
    print("Available colors: red, blue, green, yellow. Enter q to quit.")

    while True:
        sequence.append(random.choice(COLORS))
        print(f"\nRound {len(sequence)} — remember this sequence:")
        print(" -> ".join(sequence))

        while True:
            answer = input("Repeat the colors, separated by spaces or commas: ")
            try:
                guess = parse_guess(answer)
                break
            except ValueError as error:
                print(error)

        if guess is None:
            print(f"You quit with a score of {score}.")
            return score
        if guess != sequence:
            print(f"Wrong sequence! The sequence was: {' -> '.join(sequence)}")
            print(f"Game over. Your score: {score}")
            return score

        score += 1
        print("Correct! Get ready for the next round.")


def main():
    print("=== Simon Says ===")
    while True:
        play_game()
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
