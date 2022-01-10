pswd = "sheesh"  # Only have to change the "pswd" value
guess: str = ""
guess_count = 0
guess_limit = 5
num_guess = "Invalid response. Letters only!"
null_guess = "Invalid response. Don't be scared, hazard a guess!"
no_like = "Likeness = 0. You have " + str(guess_limit - guess_count) + " guesses remaining. Please try again!"
like1 = "Likeness = 1. You have " + str(guess_limit - guess_count) + " guesses remaining. Please try again: "
like2 = "Likeness = 2. You have " + str(guess_limit - guess_count) + " guesses remaining. Please try again: "
like3 = "Likeness = 3. You have " + str(guess_limit - guess_count) + " guesses remaining. Please try again: "
like4 = "Likeness = 4. You have " + str(guess_limit - guess_count) + " guesses remaining. Please try again: "
like5 = "Likeness = 5. You have " + str(guess_limit - guess_count) + " guesses remaining. Please try again: "

out_of_guesses = False  # Starting value for guess count function

while guess != pswd and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(f"Your word is {str(len(pswd))} letters. Please enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
    if out_of_guesses:
        print("Out of guesses...you lose!")
        break
    if guess.isnumeric():
        print(num_guess)
    if not guess:
        print(null_guess)
        continue
    if guess == pswd:
        print("GREAT JOB, YOU WON!")
    else:
        if guess[0:4] == pswd[0:4] or guess[1:5] == pswd[1:5]:
            print(like5)
        elif guess[0] == pswd[0] and guess[2:5] == pswd[2:5] or guess[0:1] == pswd[0:1] and guess[3:5] == pswd[3:5]:
            print(like5)
        elif guess[0:2] == pswd[0:2] and guess[4:5] == pswd[4:5]:
            print(like5)
        else:
            if guess[0:3] == pswd[0:3]:
                print(like4)
            elif guess[1:4] == pswd[1:4]:
                print(like4)
            elif guess[2:5] == pswd[2:5]:
                print(like4)
            elif guess[0] == pswd[0] and guess[2:4] == pswd[2:4]:
                print(like4)
            elif guess[0] == pswd[0] and guess[3:5] == pswd[3:5]:
                print(like4)
            elif guess[1] == pswd[1] and guess[3:5] == pswd[3:5]:
                print(like4)
            elif guess[0:1] == pswd[0:1] and guess[4:5] == pswd[4:5]:
                print(like4)
            elif guess[0] == pswd[0] and guess[2] == pswd[2] and guess[4:5] == pswd[4:5]:
                print(like4)
            elif guess[1:2] == pswd[1:2] and guess[4:5] == pswd[4:5]:
                print(like4)
            else:
                if guess[0:2] == pswd[0:2] or guess[1:3] == pswd[1:3] or guess[2:4] == pswd[2:4] or guess[3:5] == pswd[3:5]:
                    print(like3)
                elif guess[0] == pswd[0] and guess[2:3] == pswd[2:3] or guess[0] == pswd[0] and guess[3:4] == pswd[3:4]:
                    print(like3)
                elif guess[0] == pswd[0] and guess[4:5] == pswd[4:5] or guess[1] == pswd[1] and guess[3:4] == pswd[3:4]:
                    print(like3)
                elif guess[1] == pswd[1] and guess[4:5] == pswd[4:5] or guess[2] == pswd[2] and guess[4:5] == pswd[4:5]:
                    print(like3)
                else:
                    if guess[0] and guess[4] == pswd[0] and guess[1] and guess[5] != pswd[5] and guess[2] and guess[3] != pswd[3]:
                        print(like2)
                    elif guess[1] and guess[5] == pswd[5] and guess[0] and guess[4] != pswd[0] and guess[2:3] != pswd[2:3]:
                        print(like2)
                    elif guess[2:3] == pswd[2:3] and guess[0] and guess[4] != pswd[0] and guess[1] and guess[5] != pswd[5]:
                        print(like2)
                    else:
                        if guess[0] == pswd[0] and guess[1:5] != pswd[1:5]:
                            print(like1)
                        elif guess[1] == pswd[1] and guess[0] != pswd[0] and guess[2:5] != pswd[2:5]:
                            print(like1)
                        elif guess[2] == pswd[2] and guess[0:1] != pswd[0:1] and guess[3:5] != pswd[3:5]:
                            print(like1)
                        elif guess[3] == pswd[3] and guess[0:2] != pswd[0:2] and guess[4:5] != pswd[4:5]:
                            print(like1)
                        elif guess[4] == pswd[4] and guess[0:3] != pswd[0:3] and guess[5] != pswd[5]:
                            print(like1)
                        elif guess[5] == pswd[5] and guess[0:4] != pswd[0:4]:
                            print(like1)
                        else:
                            print(no_like)