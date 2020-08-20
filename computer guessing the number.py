import random as rd
print("1.before starting the game fix a number in between 1 and 100 in your mind.\n2.after starting the dont change the your fixed number.")
start,end=0,100
c=1
correct="Y"
while(correct=="Y"):
    computer_guess=rd.randint(start,end)
    print("computer guess number is:",computer_guess)
    instructions=input("if number is too large(L) or too small(S) or correct(C):")
    while(instructions!="C"):
        if(instructions=="L"):
            end=computer_guess-1
            computer_guess = rd.randint(start, end)
            print("computer guess number is:", computer_guess)
            instructions = input("if number is too large(L) or too small(S) or correct(C):")
        elif(instructions=="S"):
            start= computer_guess+1
            computer_guess = rd.randint(start, end)
            print("computer guess number is:",computer_guess)
            instructions = input("if number is too large(L) or too small(S) or correct(C):")
        c+=1
    print("great! computer guessed the number ", str(c), "times..")
    correct = input("do u want to play again(Y or N): ")
    if (correct == "N"):
        c=1
        print("Thanks for playing...")



