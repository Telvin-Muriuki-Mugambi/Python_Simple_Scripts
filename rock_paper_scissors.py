import random

# Track if the player wants to keep playing
playing = True

while playing:
    print("\n\t1: Rock")    #1 = Rock
    print("\t2: Paper")     #2 = Paper
    print("\t3: Scissors")  #3 = Scissors

    computer = random.randint(1, 3)
    
    # Validation loop to handle non-integer or out-of-bounds inputs
    try:
        player = int(input("Please choose 1, 2 or 3: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Game logic
    if player == computer:
        print("This is a draw!!")
    elif player == 1 and computer == 2:
        print("You lose. Paper beats Rock!!")
    elif player == 1 and computer == 3:
        print("You win. Rock beats Scissors")
    elif player == 2 and computer == 1:
        print("You win. Paper beats Rock!!")
    elif player == 2 and computer == 3:
        print("You lose. Scissors beats Paper!!")
    elif player == 3 and computer == 1:
        print("You lose. Rock beats Scissors!!")
    elif player == 3 and computer == 2:
        print("You win. Scissors beats Paper!!")
    else:
        print("Invalid input")
        continue  # Skip the replay prompt if input was invalid

    # Check if the player wants to continue
    # Uses .lower() to accept 'no', 'No', 'N', etc.
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again in ["no", "n"]:
        playing = False
        print("\nThanks for playing! Goodbye.")
