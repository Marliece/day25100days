import random

def rollDice(sides):
  random_number = random.randint(1, sides)
  return random_number

def rollDice2():
  dice6 = random.randint(1, 6)
  dice8 = random.randint(1, 8)
  health = dice6 * dice8
  return health

print("⚔ Character Sats Generator ⚔")
print()
while True:
  name = input("Name your warrior: ")
  hp = rollDice2()
  print("Their health is:",hp,"hp")
  print()
  again = input("Do you want to create another character? ")
  if again == "yes":
    continue
  else:
    break