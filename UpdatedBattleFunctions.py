
from character import *
from enemy import *

def isDead(Object):
    if Object.health <= 0:
        return True
    else:
        return False

def victory(player, adversary, window, master):
    window.hideEnemy()
    window.displayCharacterXPBar(player)
    window.displayText("You have defeated the %s!" % (adversary.name))
    master.update()
    time.sleep(2)
    player.XP += adversary.xpValue
    print(str(player.XP))
    window.hideCharacterXPBar()
    window.displayCharacterXPBar(player)
    window.displayText("%s experience earned!" % (str(adversary.xpValue)))
    master.update()





def battle(player, adversary, window, master):
    if not adversary.healthDisplayed:
        window.displayEnemy(adversary, player)
        adversary.healthDisplayed = True
    if player.turn:
        if not isDead(player):
            player.addedDefense = 0
            window.displayBattleMenu(player, adversary, master)
            window.displayText("Decide what you want to do.")
        else:
            window.hideBattleMenu()
            window.displayText("YOU HAVE DIED")
            master.update()

    elif adversary.turn:
        window.hideBattleMenu()
        master.update()
        time.sleep(2)
        if player.isFleeing:
            print("this message should not show")
        elif not isDead(adversary):
            adversary.attack(player, window)
            player.turn = True
            adversary.turn = False
            master.update()
            time.sleep(2.5)
            battle(player, adversary, window, master)
        else:
            victory(player, adversary, window, master)


# the isDead function basically returns true if something is dead




