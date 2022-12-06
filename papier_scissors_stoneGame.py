import random
gamechoise=["papier","scissors","stone"]
papier = gamechoise[0]
scissors = gamechoise[1]
stone = gamechoise[2]
compscore = 0
userscore = 0
i=0
while True : 
    comp = random.choice(gamechoise)
    user= input(" Please select input a choise for gaming: papier, scissors or stone?")
    if user == papier :
        if comp == stone :
         userscore += 1
         print(compscore)  
         print(userscore)
        elif comp == scissors: 
         compscore += 1
         print(compscore)  
         print(userscore)
        elif user == scissors :
            if comp == papier: 
             userscore += 1
             print(compscore)  
             print(userscore)
            elif comp == stone:
             compscore += 1
             print(compscore)  
             print(userscore)
        elif user == stone :
            if comp == papier:
             compscore += 1
             print(compscore)  
             print(userscore)
            elif comp == scissors:
             userscore += 1
             print(compscore)  
             print(userscore)
             
    i += 1
    if i == 10 :
     break
 
  
print( userscore )
print( compscore )

if userscore < compscore :
    print("Computer Wın !!")

elif userscore == compscore :
    print("Game is TIE !!")
else:
    print("You WIN!!!")