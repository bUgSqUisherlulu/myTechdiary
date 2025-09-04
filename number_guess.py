import random
print("Welcome to the Number Guessing Game!")
name=input("Enter player name: ")
plays=int(input("How many times do you want to play? "))
for i in range(plays):
    
    randomnumber=random.randint(1,50)
    Guessednumber=int(input("Enter a number between 1 and 50: "))
    if Guessednumber==randomnumber:
        print("You Won!!"+name)
        break
    else:
        print ("You Lost!!"+ name+" The number was", randomnumber)




