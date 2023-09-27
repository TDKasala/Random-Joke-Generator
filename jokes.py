# Importing the random function
import random

# Creating an empty list called jokes_list
jokes_list = []

# creating jokes as strings and append them as items to the list created above
joke1 = "I have a Polish friend who is a sound technician.And a Czech one too. And a Czech one too."
jokes_list.append(joke1)

joke2 = "What do you call a sick eagle? Illegal."
jokes_list.append(joke2)

joke3 = '''Saw a man standing on one leg at an ATM. 
Confused, I asked him what he was doing...
He said: “Just checking my balance.'''
jokes_list.append(joke3)

joke4 = '''How do you make the number one disappear?
You just add a G and it's gone.'''
jokes_list.append(joke4)

joke5 = '''I can't believe someone broke into my house and stole all of my fruit.
I am peachless.'''
jokes_list.append(joke5)

# Using the random.choice() to display a random joke from the list 
# Source : https://pynative.com/python/random/
print(random.choice(jokes_list))