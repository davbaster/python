#palindrome

text = input("Enter your message: ")
#hola
text = text.lower()#makes the message lowercase
txt = text[::-1]#reverse the message


print(txt)
if text.replace(" ","") == text[::-1].replace(" ",""):#remove spaces in both, and compare
    print("It's a palindrome")
else:
     print("It is not a palindrome")
