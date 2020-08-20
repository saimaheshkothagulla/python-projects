import random as rd
random_num=rd.randint(1,100)
correct="Y"
while(correct=="Y"):
    guess=int(input("guess the number between 1 and 100: "))
    c=1
    while(random_num!=guess):
        if(random_num>guess):
            print("its to short....")
            guess = int(input("guess the number between 1 and 100: "))
        else:
            print("its to long....")
            guess = int(input("guess the number between 1 and 100: "))
        c+=1
    print("great! you guessed the number ",str(c),"times..")
    correct=input("do u want to play again(Y or N): ")
    if(correct=="N"):
        print("Thanks for playing...")









