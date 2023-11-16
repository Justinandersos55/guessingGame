import random

def main():
    attempts = 0
    x = generate_random_number()
    player_guess(x,attempts)


def generate_random_number():
    secret_number = random.randint( 1,100 )
    return(secret_number)


def player_guess(secret_number, attempts):
    guess = input("Pick a number between 1 and 100 ")
    if guess.isdigit():
        if int(guess) >= 101:
            print("YOUR GUESS IS TOO HIGH. GUESS BETWEEN 1 AND 100\n")
            player_guess(secret_number,attempts)
        elif int(guess) <= 0:
            print("YOUR GUESS IS TOO LOW. GUESS BETWEEN 1 AND 100\n")
            player_guess(secret_number,attempts)
        elif int(guess) >= 1 <= 100:
            attempts+=1
            give_feedback(secret_number,int(guess),attempts)
            return(guess)
        else: 
            print("ENTER A VALID NUMBER BETWEEN 1 AND 100")
            player_guess(secret_number,attempts)
    else:
        print("PLEASE RETURN A VALID VARIABLE")
        player_guess(secret_number,attempts)
def give_feedback(secret_number, guess,attempts):
    if attempts <3:
            if guess == secret_number:
                print("YOU GUESSED THE NUMBER! CONGRATS!")
            if guess > secret_number:
                print("Your guess is too high. \n" + str(3-attempts) + " ATTEMPTS REMAINING\n")
                player_guess(secret_number,attempts)
            if guess < secret_number:
                print("Your guess is too low. \n"+ str(3-attempts) + " ATTEMPTS REMAINING\n")
                player_guess(secret_number,attempts)
    if int(3-attempts) <= 0:
        print(str(secret_number)+ " WAS THE CORRECT ANSWER!\n")

if __name__ == "__main__":
    main()