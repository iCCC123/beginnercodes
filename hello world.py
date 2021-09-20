import mysql.connector
loop = True
while loop:
    Name = input("Name : ")
    Age = input("Age : ")
    if int(Age) >= 35:
        print(Name.title() + "," + " please, proceed to Qatar Vaccination Center")
    else:
        print(Name.title() + "," + " please contact 16000 for assistance")
    if Name == "ty":
        break
