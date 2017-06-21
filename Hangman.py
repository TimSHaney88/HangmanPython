

#hangman game
import random

play = 'Y'
while play == 'Y' or play == 'y':
    
    #words  =["write", "that", "program"]
    infile = open("hangman.txt", "r") #open file
    s = infile.read()
    print(s)
    words = s.split()
    
    
    random.shuffle(words)
    print(words)

    correctCount = 0
    word = words[0]
    wordToWin = len(word)
    displayList = []
    guessedList = []
    for u in word:
        displayList.append('*')
    
    count = 0
    while count < 7:
        
        
        
        guess = input("Enter a letter in word: "+str(displayList))
        found = False
        i=0
        while i<len(guessedList):
            if guess == guessedList[i]:
                print(guess, " is already guessed.")
                found = True
                break
            i = i + 1
        counter = 0
        if found == False:
            guessedList.append(guess)
            incorrectGuess = True
            for j in word:
                if guess == j:
                    displayList.pop(counter)
                    incorrectGuess = False
                    displayList.insert(counter, j)
                    correctCount = correctCount + 1
            
               
                counter = counter + 1
            if incorrectGuess == True:
                count = count + 1
        if correctCount == wordToWin:
            print("You Win! ")
            play = input("Do you want to play again? ")
            break
    if count == 5:
        print("You lose! ")
        play = input("Do you want to play again? ")
   
        

