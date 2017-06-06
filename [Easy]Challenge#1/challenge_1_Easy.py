#Author: Keifer Edelmayer
#Github username: KeiferE
#Program Description:
'''
URL: https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/

Reddit Challenge [easy] #1

create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:

your name is (blank), you are (blank) years old, and your username is (blank)

for extra credit, have the program log this information in a file to be accessed later.

***Extra***

-added error handling for name, age, username input format
-added abilty to check and redo input before write to file occurs
-stores all user information collected in redditdata.txt


'''

while True:
    print("Please enter your first name, age, and reddit username in that order")

    try:
         inputString = raw_input()
         name, age, username = inputString.split()
    except ValueError:
         print("Not proper format please enter all three fields")
         continue

    print("Your name is " + name + ", you are " + age + " years old, and your username is " + username)
   
    print("Is this correct y/n?")
    redoInput = raw_input()
    if(redoInput is 'y'):
        break

print("Writing information to file ... see stored tuples in redditdata.txt")   

f = open('redditdata.txt', 'a')
f.write("%s %s %s\n" % (name, age, username))
f.close()
