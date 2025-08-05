import random
cum = random.randint(1,100)

while True : 
    number = int(input("Guess The Number : "))
    if cum == number :
      print("You Guess the Write number!!!!!!!")
      break
    
    elif number > cum :
       print("Highhh Number,Try lower")
    
    else : 
      print("Lower Number,Try Higher")
        
