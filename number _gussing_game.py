# its a number gussing game where user guess a number.


import random
secret_number = random.randint(1,100)

gusses = 0

while True:
  gusses += 1
  user_num = int(input("Enter a number: "))
  distance = abs(secret_number - user_num)

  if user_num == secret_number:
    print("congratulations your guess is correct! ")

    break
  
  elif distance <= 5:
    print("very close.")

  elif distance > 30:
        print("very far!.")

  elif user_num > secret_number:
    print("Number is to high. ")
    
  elif user_num < secret_number:
    print("Number is to low. ")
  
print(f"You got it in {gusses} gusses")

