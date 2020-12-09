# FIXME 1: Complete the compare_answers function
def compare_answers(u1, u1a, u2, u2a):
    if u1a == u2a:
        return("It's a tie!")
    elif u1a == 'rock':
        if u2a == 'scissors':
            return("Rock wins! Good job " + u1)
        elif u2a == 'Paper':
            return("Paper wins! Good job " + u2)
        else:
            return(u2 + " made an invalid choice! You have not entered rock, paper or scissors.")
    elif u1a == 'paper':
        if u2a == 'rock':
            return("Paper wins! Good job " + u1)
        elif u2a == 'scissors':
            return("Scissors wins! Good job " + u2)
        else:
            return(u2 + " made an invalid choice! You have not entered rock, paper or scissors.")
    elif u1a == 'scissors':
        if u2a == 'paper':
            return("Scissors wins! Good job " + u1)
        elif u2a == 'rock':
            return("Rock wins! Good job " + u2)
        else:
            return(u2 + " made an invalid choice! You have not entered rock, paper or scissors.")
    else:
        return(u1 + " made an invalid choice! You have not entered rock, paper or scissors.")

if __name__ == "__main__":
    # FIXME 2a: Prompt the user to input the name of player 1
    firstPN = input("What's the first player's name?\n")
    # FIXME 2b: Prompt the user to input the name of player 2
    secPN = input("What's the second player's name?\n")
    # FIXME 2c: Prompt the user to input the choice of player 1
    firstPA = input(firstPN + " do you want to choose rock, paper or scissors?\n")
    # FIXME 2d: Prompt the user to input the choice of player 2
    secPA = input(secPN + " do you want to choose rock, paper or scissors?\n")
    # FIXME 2e: Call the function and print the result of the game
    print(compare_answers(firstPN, firstPA.lower(), secPN, secPA.lower()))

