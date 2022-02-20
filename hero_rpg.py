# In this simple RPG game, the hero fights the goblin. He has the options to:

# This set of code is part 1, steps 1 - 9 (modified for part 2).
#

#from socket import herror

#=============================================================================

# ==>   select an enemy and place their name in the last line   <== #

#=============================================================================


import random

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        
        if self.health > 0:
            return True
        else:
            return False
        
    def attack(self, enemy): 
        if(self.character_name == "goblin" or self.character_name == "zombie" or self.character_name == "medic" or self.character_name == "shadow" or self.character_name == "behemoth" or self.character_name == "golem"):
            enemy.health -= self.power
#            print(self.getPower(enemy))
    def getPower(self, enemy):
        if(enemy.character_name == "goblin" or enemy.character_name != "zombie" or enemy.character_name == "medic" or enemy.character_name == "shadow" or enemy.character_name == "behemoth" or enemy.character_name == "golem"):
            r = random.randint(1,5)
            if r == 1:
                self.power = self.power * 2
                enemy.health -= self.power
                print(f"{self.character_name} does double damage!")
                self.power = self.power / 2
            else:
                enemy.health -= self.power
        # if enemy.character_name != "zombie":
        #     enemy.health -= self.power
        
        if(self.character_name == "hero"):
            print(f"You do {self.power} damage to the {enemy.character_name}.")
        
        # elif(self.character_name == "goblin" or self.character_name == "zombie" or self.character_name == "medic" or self.character_name == "shadow" or self.character_name == "behemoth" or self.character_name == "golem"):
        #     print(f"The {self.character_name} does {self.power} damage to you.")

    
    def print_status(self):
        if self.character_name == "hero":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == "goblin":
            print(f"The rancid {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "zombie":
            print(f"The shambling {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "medic":
            print(f"The stoic {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "shadow":
            print(f"The wispy {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "behemoth":
            print(f"The daunting {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "golem":
            print(f"The awkward {self.character_name} has {self.health} health and {self.power} power.")

#------------------------------------

class Hero(Character):
    def __init__(self, health, power):
        self.character_name = "hero"
        super(Hero, self).__init__(health, power)

#------------------------------------

class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = "goblin"
        super(Goblin, self).__init__(health, power)

#------------------------------------

class Zombie(Character):
    def __init__(self, health, power):
        self.character_name = "zombie"
        super(Zombie, self).__init__(health, power)
        
#------------------------------------

class Medic(Character): #20% chance to regain 2HP when attacked
    def __init__(self, health, power):
        self.character_name = "medic"
        super(Medic, self).__init__(health, power)

#------------------------------------

class Shadow(Character): #has 1HP but can only be hit with a 10% chance
    def __init__(self, health, power):
        self.character_name = "shadow"
        super(Shadow, self).__init__(health, power)

#------------------------------------

class Behemoth(Character):  #custom character, 15HP and 10% chance to do 30 damage(KO)
    def __init__(self, health, power):
        self.character_name = "behemoth"
        super(Behemoth, self).__init__(health, power)

#------------------------------------

class Golem(Character): #custom character, 25HP
    def __init__(self, health, power):
        self.character_name = "golem"
        super(Golem, self).__init__(health, power)

#------------------------------------

#character stats(health, power)
hero = Hero(100, 5)      
goblin = Goblin(100, 2)
zombie = Zombie(100, 1)
medic = Medic(100, 2)
shadow = Shadow(1, 2)
behemoth = Behemoth(15, 30)
golem = Golem(25, 2)

#------------------------------------
# #Item Shop addition (not sure how to add it yet)
# class Item_Shop:
#     def __init__(self, price, armor, healing, evade):
#         self.price = price
#         self.armor = armor
#         self.healing = healing
#         self.evade = evade

# #------------------------------------

# class SuperTonic(Item_Shop):  #restores 10HP to Hero
#     def __init__(self, healing):

# #------------------------------------

# class Armor(Item_Shop):       #adds 2 armor points to Hero
#     def __init__(self, armor):

# #------------------------------------

# class Evade(Item_Shop):       #adds 3 evade points to the Hero
#     def __init__(self, evade):

# #------------------------------------

# class Protection(Item_Shop):  #reduced damage by 10HP
#     def __init__(self, protection):

# #------------------------------------

# class 

# #------------------------------------
# supertonic = SuperTonic
# armor = Armor
# evade = Evade

#------------------------------------

def main(enemy):
    
    
    while enemy.alive() > 0 and hero.alive(): 
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. Attack the {enemy.character_name}!")
        print("2. Act like a tree.")
        print("3. Point somewhere and yell 'SQUIRREL!'!")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            
            hero.getPower(enemy) 

            if not enemy.alive():
                print(f"The {enemy.character_name} is dead.")
        elif raw_input == "2":
            print("Why? You're obviously not a tree.")
            pass
        elif raw_input == "3":
            print("You got away... Coward!")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            
            enemy.attack(hero) 
            
            if not hero.alive():
                print("You are dead.")
        

main(zombie) # <<< choose a character
