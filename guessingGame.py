import random
def main():
    x = generate_random_number()
    

def generate_random_number():
    secret_number = random.randint( 1,100 )
    return(secret_number)

if __name__ == "__main__":
    main()