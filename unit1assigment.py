import time
import random  # importing necissary modules

def guesses(numberwords):
    game = True  # setting up the while loop
    while game == True:
        if numberwords != 0:
            wordguess = input("what word do you see?")
            wordguess = wordguess.lower()  # defensive coding
        if numberwords == 0:
            print("congrats! you completed this word search!")
            game = False  # ending while loop
            quit()  # quiting the game
        if wordguess not in words:
            print("im sorry! that is not one of the words!")  # ensuring that the word is in the list of words
        else:
            if wordguess in guessedwords:
                print("You have already guessed this word!")
            if wordguess in words:
                guessedwords.append(wordguess)  # appends guess to a list of guessed words
                print("congrats! " + str(wordguess) + " was guessed correctly!")
                numberwords = numberwords - 1  # for ending the while loop once a
                print("you have " + str(numberwords) + " word(s) left to guess")

def indexcheck(currentpoints, pointslist):  # function for checking if a word can be inserted into the grid without being overlapped
    for point in currentpoints:
        if point in pointslist:
            return True
    return False

def indexfinder(length,numberwords,searchtype):
    indexvalues = []
    for y in range(numberwords):  # length is the number of words
        firstindex = random.randint(0,length-1)
        secondindex = random.randint(0,length-1)
        difference = length-secondindex  # lines 32-34 make sure that the word isnt made off the length of the grid
        pointslist = []  #empty list of points that will be filled with the r and c value of words inserted into the grid
        for x in range(secondindex, secondindex+(len(words[y]))):  # nested for loop to search for a place on the grid for a word
            pointslist.append([firstindex, x])  # appends the r value of the word (where the word starts, then appends the c value (the x) to the list of points
        while difference < len(words[y]) or indexcheck(pointslist, indexvalues):
            firstindex = random.randint(0, length-1)
            secondindex = random.randint(0, length-1)
            difference = length - secondindex   #lines 39 to 41 are so if the word is still off the grid, it searchs until it finds a place for the word to get placed
            pointslist = []  # resets point list
        temp = 0
        if searchtype == "e":
            for x in range(secondindex, secondindex + (len(words[y]))):
                pointslist.append([firstindex, x])  # appends the point where a word can be inserted to a list of points
                if difference >= len(words[0]):  # lines 47 to 50 are to ensure that if the word overlaps with an exsisting word, it finds a new point the word can be inserted * same for all lines that use this code
                    grid[firstindex][secondindex + temp] = words[y][temp]
                    indexvalues.append([firstindex, secondindex + temp])
                    temp += 1
        if searchtype == "m":
            oreintation = random.randint(0, 1)  # variable that determines the oreintation of the word in the wordsearch
            if oreintation == 0:
                words[y] = words[y][::-1]  #this makes it so the word can be placed in the grid backwards  * USED MULTIPLE TIMES
                for x in range(secondindex, secondindex + (len(words[y]))):
                    pointslist.append([firstindex, x])
                    if difference >= len(words[0]):
                        grid[firstindex][secondindex+temp] = words[y][temp]
                        indexvalues.append([firstindex,secondindex+temp])
                        temp+=1
            if oreintation == 1:
                for x in range(secondindex, secondindex + (len(words[y]))):
                    pointslist.append([firstindex, x])
                    if difference >= len(words[0]):
                        grid[firstindex][secondindex + temp] = words[y][temp]
                        indexvalues.append([firstindex, secondindex + temp])
                        temp += 1
        if searchtype == "h":
            oreintation = random.randint(0, 2)
            if oreintation == 0:
                words[y] = words[y][::-1]
                for x in range(secondindex, secondindex + (len(words[y]))):
                    pointslist.append([firstindex, x])
                    if difference >= len(words[0]):
                        grid[firstindex][secondindex + temp] = words[y][temp]
                        indexvalues.append([firstindex, secondindex + temp])
                        temp += 1
            if oreintation == 1:
                for x in range(secondindex, secondindex + (len(words[y]))):
                    pointslist.append([firstindex, x])
                    if difference >= len(words[0]):
                        grid[firstindex][secondindex + temp] = words[y][temp]
                        indexvalues.append([firstindex, secondindex + temp])
                        temp += 1

alpabet = "abcdefghijklmnopqrstuvwxyz"
grid = []
print("Hello and welcome to the wordsearch extravaganza!")
time.sleep(2)
print("On word search extravaganza you can choose between a easy word search, medium word search, and hard word search. ")
time.sleep(3)
while 1 == 1:  # whole code is put in a while loop for defensive coding
    searchtype = input("what word search would you like to choose? (h/m/e)")
    searchtype = searchtype.lower()  # defensive coding
    if searchtype == "e":
        print("The easy word search consists of a 7 x 7 grid with 5 words that are all 3 letters.")
        print("the words can be sideways only")
        choice = input("would you like to choose the hard word search? (y/n)")
        choice = choice.lower()  # defensive coding
        if choice == "y":
            guessedwords = []  # empty list that appends the users guess
            length = 7
            numberwords = 5
            print("very well then")
            print("")  # this is used for extra space between the print line on 22 and the word search
            file = open("easysearch.txt", "r")
            file = file.readlines()
            words = []  # empty list created to transfer words from the file to be put in the grid
            for y in range(0,5):
                index = random.randint(0,4)
                word = file[index].strip()
                del file[index]
                words.append(word)  # lines 116 to 119 pick a random word in the file and append it to the word list, then delete the word at the index from the file so it cant be used more then once* used more then once
            for i in range(length):
                grid.append([])  # lines 120 to 121 create an empty grid for the words to be put in *used more then once
                for j in range(length):
                    letter = random.randint(0, 25)
                    grid[i].append(alpabet[letter])  # lines 122 to 124 append random letters at a random index from the string in the variable named alphabet* used more then once
            indexfinder(length,numberwords, searchtype)  # called function to put words in the grid
            for i in grid:
                print(i)  # prints words in grid
            guesses(numberwords)  # called function for guessing the words
        if choice == "n":
            print("very well then")
        else:
            choice = input("would you like to choose the hard word search? (y/n)")  # defensive coding
    if searchtype == "m":
        print("The medium word search consists of a 9x9 grid with 10 words that are all 4 letters")
        print("The words can be sideways or backwards")
        choice = input("would you like to choose the medium word search? (y/n)")
        choice = choice.lower()  #defensive coding
        if choice == "y":
            guessedwords = []
            length = 9
            numberwords = 10
            print("very well then")
            print("")
            file = open("mediumsearch.txt", "r")
            file = file.readlines()
            words = []
            for y in range(0,numberwords):
                index = random.randint(0,4)
                word = file[index].strip()
                del file[index]
                words.append(word)
            for i in range(length):
                grid.append([])
                for j in range(length):
                    letter = random.randint(0, 25)
                    grid[i].append(alpabet[letter])
            indexfinder(length,numberwords, searchtype)
            for i in grid:
                print(i)
            guesses(numberwords)
    if searchtype == "h":
        print("The hard word search consists of a 12x12 grid with 15 words 6 letter words")
        print("The words can be sideways or backwards")
        choice = input("Would you like to choose the hard word search? y/n")
        choice = choice.lower()
        if choice == "y":
            guessedwords = []
            length = 12
            numberwords = 15
            print("very well then")
            print("")
            file = open("hardsearch.txt", "r")
            file = file.readlines()
            words = []
            for y in range(0, numberwords):
                index = random.randint(0, len(file)-1)
                word = file[index].strip()
                del file[index]
                words.append(word)
            for i in range(length):
                grid.append([])
                for j in range(length):
                    letter = random.randint(0, 25)
                    grid[i].append(alpabet[letter])
            indexfinder(length, numberwords, searchtype)
            for i in grid:
                print(i)
            guesses(numberwords)