import random
import time
from tkinter import *

# This is the 'Enemy' class; it is a blueprint for any potential enemies the player may fight
class Enemy:
    def __init__(self, name, health, maxHealth, attackValue, defenseValue):
        self.name = name
        self.image = PhotoImage(file= (self.name).lower() +".png")
        self.health = health
        self.maxHealth = maxHealth
        self.attackValue = attackValue
        self.defenseValue = defenseValue
        self.turn = False
        self.healthDisplayed = False

    # the attack method does a random amount of damgage based upon attack, and subracts that damage from the enemy(the player's) Health
    def attack(self, PLAYER, window):
        initialHealth = PLAYER.health
        damage = random.randint(self.attackValue - 5, self.attackValue + 5)
        damage = damage - (PLAYER.defenseValue + PLAYER.addedDefense)
        print("")
        if damage <= 0:  # ensures no negative damage
            damage = 0
        elif damage == self.attackValue + 5:  # critical hit if the max damage is done
            pass
        PLAYER.health = PLAYER.health - damage
        if PLAYER.health < 0:
            PLAYER.health = 0
        damage = initialHealth - PLAYER.health
        window.updateHealthBar(PLAYER)
        window.displayText("The %s attacks and does %s damage!" % (self.name, damage))

