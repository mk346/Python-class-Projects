secret_word ="trouser"
guess= ""
count=0
guess_limit = 3
out_of_guesses= False
print("HINT: I have two legs but i cant walk")

while guess!= secret_word and not(out_of_guesses):
    if count<guess_limit:
        guess = input("Enter Your Guess: ")
        count+=1

    else:
        out_of_guesses= True
if out_of_guesses:
    print("You are Remaining with: " + str(guess_limit - count) + "\t Guesses")
    print("Out of Guesses, You Lose!")
else:
    print("You Win!")
  