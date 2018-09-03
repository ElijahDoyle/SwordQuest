import random
import time
from UpdatedBattleFunctions import *
# the Character class acts as the base for the player, with methods like attack, displayInventory, etc.
class Character:
    def __init__(self, name):
        self.xp = 0
        self.name = name
        self.addedDefense = 0
        self.health = 20  # current amount of health
        self.maxHealth = 20  # max amount of health
        self.armor = ["Hat",
                      2]  # in self.armor and self.weapon, the first index in the list is the Weapon itself, and the second is the value
        self.weapon = ["Fists", 5]
        self.attackValue = self.weapon[1]  # equals the value of the weapon
        self.defenseValue = self.armor[1]  # equals the value of the armor
        self.isFleeing = False  # the state in which the player is fleeing or not (initially set to False
        self.inventory = {
            "Gold": {"Amount": 5, "Description": "Gold Pieces"},  # gold to potentially be used in a shop
            "Stick": {"Amount": 1, "Description": "Just a stick"},  # just a stick
            "Health Potion": {"Amount": 2, "Description": "Heals 5 health" }
        }
        self.spells = {}  # dictionary of spells known by the player with associated damage values
        self.defending = False
        self.addedDefense = 0
        self.turn = True
            # the displayInventory method does just that, prints out all items with their amount/description

    def displayInventory(self):
        print("")
        for key in self.inventory:
            print(key, " : ", self.inventory[key])

    # the addInventory adds an item to the inventory and a value to the new key
    def addInventory(self, newItem, newValue):
        self.inventory[newItem] = newValue

    # the attack method does a random amount of damgage based upon attack, and subracts that damage from the enemy Health
    def attack(self, ENEMY, window, master):
        beforehealth = ENEMY.health
        damage = random.randint(self.attackValue - 5, self.attackValue + 5)  # this allows for variation in attacks
        damage = damage - ENEMY.defenseValue
        if damage <= 0:  # this if statement ensures you don't do negative damage
            damage = 0

        elif damage == self.attackValue + 5:
            pass# an attack is a 'critical hit' when it does the max amount of damage
        ENEMY.health = ENEMY.health - (damage)  # this actually does the damage
        if ENEMY.health < 0:  # this if statement ensures an enemy doesn't have negative health
            ENEMY.health = 0

        damage = beforehealth - ENEMY.health
        window.updateHealthBar(ENEMY)
        window.displayText("You attack the enemy with your %s and do %s damage!" % (self.weapon[0], damage))
        self.turn = False
        ENEMY.turn = True

        battle(self, ENEMY, window, master)

    # the flee method just gives the player a chance to escape
    def flee(self, ENEMY, window, master):
        chanceOfEscape = random.randint(0, 5)
        if chanceOfEscape == 1:
            window.displayText("Got Away Safely!")
            self.isFleeing = True
            self.turn = False
            ENEMY.turn = True
            battle(self, ENEMY, window, master)

        else:
            window.displayText("The %s blocked the way!" % (ENEMY.name))
            self.turn=False
            ENEMY.turn=True
            battle(self, ENEMY, window, master)

    # the defend method creates a value that will be subracted from the enemy's attack for 1 turn
    def defend(self, ENEMY, window, master):
        self.addedDefense = random.randint(1, 5)
        self.turn=False
        ENEMY.turn=True
        window.displayText("You ready your defenses.")
        battle(self, ENEMY, window, master)

    # the magic method will do something when i work it out
    def magic(self):
        if len(self.spells) > 0:
            return True
        else:
            print("")
            time.sleep(1)
            print(self.name + " doesn't know any spells yet!")
            time.sleep(3)
            print("")
            return False
                    # TODO : FIGURE THIS OUtT
    # this allows players to use an item from their inventory
    def useItem(self):
        self.displayInventory()
        print("")
        print("If you want to choose a different action type 'exit'.")
        isValid = False
        while not isValid:
            print("")
            choice = (input("Which item would you like to use? ")).lower()
            print("")
            time.sleep(1)
            if choice == "gold":
                print("What are you going to do, pay him off?")
                print("")
                time.sleep(3)
                print("Choose another Item...")
                isValid = False
            elif choice == "stick":
                print("This is a stick...")
                time.sleep(3)
                print("What are you going to do with a stick?")
                print("")
                time.sleep(3)
                print("Choose another Item...")
                isValid = False
            elif choice == "health potion":
                print(self.name + " used a health potion!")
                print("")
                time.sleep(3)
                hlthGained = self.maxHealth - self.health
                if hlthGained > 5:
                    hlthgained = 5
                print("+%s health!" % (hlthGained))
                print("")
                self.health += 5
                if self.health > 20:
                    self.health = 20
                    time.sleep(2)
                print("Player Health: ", self.health, " / ", self.maxHealth)
                del self.inventory["Health Potion"]
                isValid = True
                break
            elif choice == ('exit'):
                isValid = True
                return False
                break

            else:
                print("That is not in your inventory")
                time.sleep(2)
                continue

    def usePotion(self, window, ENEMY, master):

        if (self.maxHealth - self.health) > 5:
            self.health += 5
            window.displayText("5 Health restored")
        else:
            window.displayText(str(self.maxHealth - self.health) + " Health restored")
            self.health = self.maxHealth
        (self.inventory["Health Potion"])["Amount"] -= 1
        window.updateHealthBar(self)
        window.potionButton.config(text="x" + str((self.inventory["Health Potion"])["Amount"]) + " Health Potions")

        window.hideCharacterInventory()
        window.displayCharacterInventory(self, ENEMY, master)




