print("Welcome to my computer quiz!")
playing = input("Do you want to play? Y/N: ")

if playing != "Y":
    quit()

print("Alright, Let's play! :) ")

answer_1 = input("What does CPU stand for? ")
if answer_1 == "central processing unit" or "Central Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")

answer_2 = input("What does GPU stand for? ")
if answer_2 == "graphics processing unit" or "Graphics Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")

answer_3 = input("What does RAM stand for? ")
if answer_3 == "random access memory" or "Random Access Memory":
    print("Correct!")
else:
    print("Incorrect!")

answer_4 = input("What does PSU stand for? ")
if answer_4 == "power supply unit" or "Power Supply Unit":
    print("Correct!")
else:
    print("Incorrect!")

answer_5 = input("What does HDD stand for? ")
if answer_5 == "hard disk drives" or "Hard Disk Drive":
    print("Correct!")
else:
    print("Incorrect! ")

answer_6 = input("What does SSD stand for: ")
if answer_6 == "solid state drives" or "Solid State Drives":
    print("Correct!")
else:
    print("Incorrect!")
