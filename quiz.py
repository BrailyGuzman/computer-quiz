print("Welcome to my computer quiz!")
playing = input("Do you want to play? Y/N: ")

if playing != "Y":
    quit()

print("\nAlright, Let's play! :) ")
score = 6

answer_1 = input("\nWhat does CPU stand for? ").upper()
if answer_1 == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")
    score - 1
    
answer_2 = input("\nWhat does GPU stand for? ").upper()
if answer_2 == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")
    score - 1
    
answer_3 = input("\nWhat does RAM stand for? ").upper()
if answer_3 == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")
    score - 1

answer_4 = input("\nWhat does PSU stand for? ").upper()
if answer_4 == "power supply unit":
    print("Correct!")
else:
    print("Incorrect!")
    score - 1
    
answer_5 = input("\nWhat does HDD stand for? ").upper()
if answer_5 == "hard disk drives":
    print("Correct!")
else:
    print("Incorrect! ")
    score - 1
    
answer_6 = input("\nWhat does SSD stand for: ").upper()
if answer_6 == "solid state drives":
    print("Correct!")
else:
    print("Incorrect!")
    score - 1
    
print(f"You Have Completed The Quiz. Your Score is {score}/10")
