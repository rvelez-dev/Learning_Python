#even or odd number sorter, ask user for numbers (looped input) and sort them into two list (even or odd)

#initializng empty lists
users_input=[]
even=[]
odd =[]
#booleans for while loops
end= False
gameOver = False
while not gameOver:
    print("Enter a list of numbers, enter -1 to end loop ")
    while not end:
        #adding each number the user enters
        users_input.append(int(input("Enter your number: ")))
        last_number = users_input[-1]
        if last_number ==-1:
            #if the most recent number is a -1 pop it from the list and end loop
            users_input.pop()
            end = True

    #loop to go through users inputs and separate into an even or odd list
    for n in users_input:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    #printing lists
    print(f"The even numbers are: {even} ")
    print(f"The odd numbers are: {odd}")
    #giving the user an option to play again
    play= input("Would you like to go again? (Y/N)")
    if play == 'Y':
        #clearing the lists 
        even.clear()
        odd.clear()
        users_input.clear()
        end = False
    else:
        gameOver = True
