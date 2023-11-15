def main():
    player_guess()

def player_guess():
    guess = input("Pick a number between 1 and 100 ")
    if int(guess) > 100:
        print("YOUR GUESS IS TOO HIGH. GUESS BETWEEN 1 AND 100\n")
        player_guess()
    if int(guess) <= 0:
        print("YOUR GUESS IS TOO LOW. GUESS BETWEEN 1 AND 100\n")
        player_guess()
    if int(guess) >= 1 <= 100:
        give_feedback(23, int(guess))
def give_feedback(secret_number, guess):
    for attempts in range(3):
            if guess == secret_number:
                print("YOU GUESSED THE NUMBER! CONGRATS!")
                attempts = 4
            if guess > secret_number:
                print("Your guess is too high. \n" + str(attempts) + " ATTEMPTS REMAINING\n")
                player_guess()
            if guess < secret_number:
                print("Your guess is too low. \n"+ str(attempts) + " ATTEMPTS REMAINING\n")
                player_guess()

if __name__ == "__main__":
    main()