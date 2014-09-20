<<<<<<< HEAD
import random
=======
#Give the user a list of ingredients for a mixed drink and give them 4 names of drinks to choose from

=======
>>>>>>> origin/master
#Give the user a list of ingredients for a mixed drink and give them 4 names
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

<<<<<<< HEAD

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
    index = randrange(8)
    print(rez[index])
    answer = rez2[index]
    y = []
    
    
        

        

        



        
        
=======
>>>>>>> origin/master
