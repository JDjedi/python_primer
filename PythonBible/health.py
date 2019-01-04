import random 

health = 50
# difficulty slider: 1 = easy, 2 = medium, 3 = hard
difficulty = 2

potion_health = int(random.randint(25, 50) / difficulty)

health = health + potion_health
print(health)
