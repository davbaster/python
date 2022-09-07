#anagrams


def anagramCheck(word1, word2):
    word1 = word1.lower().replace(" ","")#makes the message lowercase and no space
    word2 = word2.lower().replace(" ","")

    print(word1)
    print(word2)
    #txt = text[::-1]#reverse the message
    #Check if the word 1 has the same letters that word 2
    if not len(word1) == len(word2):
        print("It is not an anagram")
        return 0
  
    for letter in word1:
        if word2.find(letter) == -1:
            print("It is not an anagram")
            return 0
    
    for letter in word2:
        if word1.find(letter) == -1:
            print("It is not an anagram")
            return 0
    
    
    print("It is an anagram")


#starting app
word1 = input("Enter your first word: ")
word2 = input("Enter your second word: ")

anagramCheck(word1, word2)
