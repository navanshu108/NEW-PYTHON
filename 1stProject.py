import random

options=("rock","paper","scissor")
player=()
computer=random.choice(options)


while player not in options:
    player =input("Enter a choice(rock,paper,scissor): ")
    
print(f"player :{player}")
print(f'computer: {computer}')

if computer==player :
    print("it's a tie")
elif computer=="rock" and player=="scissor" or computer=="paper" and player=="rock" or computer=="scissor" and player=="paper":
    print("you lose")
else:
    print("you win")
    
    