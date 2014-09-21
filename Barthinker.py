import random
#Give the user a list of ingredients for a mixed drink and give them 4 names of drinks to choose from
#of drinks to choose from
#Open file1, which will contain the lists of ingredients.
#Randomly select one from file1.
#Open file2 which contains the list of drinks.
#generate a list of answers including the corresponding answer. This list will add the drinks in a random order BUT must include the correct answer.
#Print the list of answers to the screen and ask which drink the ingredients
#would be used to make. The user can input the answer by typing in the name of the drink?
#Do this 5 times making sure that after a line has been randomly selected
#from the file1, that it is not selected again and also that the answer to the
#corresponding list of ingredients is placed in a random order.


#open ingredients
ingr = open('ingredients.txt')
rez = []

#open names
names = open('names.txt')
rez2 = []

#add all the names to a list called rez2
for lines in names:
    rez2.append(lines)
    
    
#add every line from ingredients to a list called ingr and
#create a variable called index which holds a number between 0 and 8(inclusive).
#print the ingredients at this index of the list.
#the name corresponding to these ingredients are held int the variable answer
#Now create a list of size 4 which includes the answer and 3 wrong answers.
#Then print the ingredients and the 4 possible answers.

for line in ingr:
    rez.append(line)

score = 0
    
for x in range(0,8):
    y = False
    while y == False :
        index = random.randint(0,12-x)
        ind1 = random.randint(0,12-x)
        ind2 = random.randint(0,12-x)
        ind3 = random.randint(0,12-x)
        if ( (index != ind1) and (ind1 != ind2) and (ind2 != ind3) and (ind1 != ind3) and (index != ind2) and (index != ind3) ): y = True        
    drinks = [rez2[ind1], rez2[index], rez2[ind2], rez2[ind3]]
    random.shuffle(drinks)
    for i in range(0,4):
        print(str(i+1) +  ". " + (drinks[i]))
    guess = int(input("Type in the number of the drink that contains these ingredients: " + rez[index]))
    if (guess - 1 ==  (drinks.index(rez2[index]))): print ("You scored a point! Your score is now " + str(score))
    else: print ("You got it wrong. Your score is " + str(score))
    rez2.remove(rez2[index])
    rez.remove(rez[index])

    
        

        

        



        
        

