import re # Used to import the RegEx module

txt = "My name is James Payne" # Creating a string with characters in it

x = re.search("^My.*Payne$", txt) # Searching for any text in a string that contains “Payne”

# If “Payne” is found, it will print the first part; if not, it will print the second part

if x:
  print("Are you Max Payne!")
else:
