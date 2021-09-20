import random

friends = input("name: ")
myfriends = friends.split(", ")

#when using the len function, always make sure to start counting from zero(0).

participants = random.randint(0, len(myfriends) - 1)

#now that the line above prints a number, you want that number to select an item on
#the list aka the list split from "myfriends"

finalpayer = myfriends[participants]

print(f"{finalpayer} will pay our meals!")