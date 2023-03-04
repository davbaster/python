#Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

def wordFinder(word1, string):
    word1 = word1.lower().replace(" ","")#makes the message lowercase and no space
    string = string.lower().replace(" ","")

    #print(word1)
    #print(string)
    #txt = text[::-1]#reverse the message
    #Check if the word 1 has the same letters that word 2
    for letter in word1:
        if string.find(letter) == -1:
            print("Word is not contained in the string")
            return 0
    
    
    print("Word is contained in the string")


#starting app
word1 = input("Enter your first word: ")
string = input("Enter your string: ")

wordFinder(word1, string)
