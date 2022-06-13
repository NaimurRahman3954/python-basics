# two player rock paper scissor game function
def rockPaperScissor():
    print("Enter your choice: \n 1. Rock \n 2. Paper \n 3. Scissor")
    choice = int(input())
    print("Enter your choice: \n 1. Rock \n 2. Paper \n 3. Scissor")
    choice2 = int(input())
    if choice == 1 and choice2 == 1:
        print("Both players chose rock. It's a tie!")
    elif choice == 1 and choice2 == 2:
        print("Player 2 wins! Paper beats rock.")
    elif choice == 1 and choice2 == 3:
        print("Player 1 wins! Rock beats scissor.")
    elif choice == 2 and choice2 == 1:
        print("Player 1 wins! Paper beats rock.")
    elif choice == 2 and choice2 == 2:
        print("Both players chose paper. It's a tie!")
    elif choice == 2 and choice2 == 3:
        print("Player 2 wins! Scissor beats paper.")
    elif choice == 3 and choice2 == 1:
        print("Player 2 wins! Rock beats scissor.")
    elif choice == 3 and choice2 == 2:
        print("Player 1 wins! Scissor beats paper.")


rockPaperScissor()
