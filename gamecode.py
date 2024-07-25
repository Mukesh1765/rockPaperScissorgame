import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
'''

paper = '''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rpc = [rock, paper, scissors]
print("welcome to rock paper and scissors game!")
entered_number = int(input("enter 1 for rock , enter 2 for paper, enter 3 for scissors :"))
random_number = random.randint(1, 3)
if entered_number > 4 or entered_number < 1:
    print("invalid input")
else:
    if random_number == entered_number:
        chosen = rpc[random_number-1]
        print(f"you chose {chosen}")
        print(f"computer chose {chosen}")
        print("its a tie")
    else :
        if rpc[random_number-1] == rock and rpc[entered_number-1] == scissors:
            chosen = rpc[entered_number - 1]
            print(f"you chose {chosen}")
            chosen = rpc[random_number - 1]
            print(f"computer chose {chosen}")
            print("you lose")
        elif rpc[random_number-1] == paper and rpc[entered_number-1] == rock:
            chosen = rpc[entered_number - 1]
            print(f"you chose {chosen}")
            chosen = rpc[random_number - 1]
            print(f"computer chose {chosen}")
            print("you lose")
        elif rpc[random_number-1] == scissors and rpc[entered_number-1] == paper:
            chosen = rpc[entered_number - 1]
            print(f"you chose {chosen}")
            chosen = rpc[random_number - 1]
            print(f"computer chose {chosen}")
            print("you lose")
        elif rpc[random_number-1] == scissors and rpc[entered_number-1] == rock:
            chosen = rpc[entered_number - 1]
            print(f"you chose {chosen}")
            chosen = rpc[random_number - 1]
            print(f"computer chose {chosen}")
            print("you win")
        elif rpc[random_number-1] == rock and rpc[entered_number-1] == paper:
            chosen = rpc[entered_number - 1]
            print(f"you chose {chosen}")
            chosen = rpc[random_number - 1]
            print(f"computer chose {chosen}")
            print("you win")
        elif rpc[random_number-1] == paper and rpc[entered_number-1] == scissors:
            chosen = rpc[entered_number - 1]
            print(f"you chose {chosen}")
            chosen = rpc[random_number - 1]
            print(f"computer chose {chosen}")
            print("you win")

print("have a good day")
input()