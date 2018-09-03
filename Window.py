from tkinter import *
from tkinter.ttk import Progressbar
from character import *
from enemy import *
from UpdatedBattleFunctions import *


class GameWindow:
    def __init__(self, master, char):


        self.settingBox = Frame(master, height=450, width=1000, background="white")
        self.settingBox.pack(side=TOP)
        self.settingBox.pack_propagate(0)


        self.battleOptionsBox = Frame(self.settingBox, height=450, width=200, background="grey")
        self.battleOptionsBox.pack(side=LEFT)
        self.battleOptionsBox.pack_propagate(0)

        self.settingBoxCanvas = Canvas(self.settingBox, height=450, width=596)
        self.settingBoxCanvas.pack(side=LEFT)
        self.settingBoxCanvas.pack_propagate(0)
        self.canvasImg = PhotoImage(file="cave.png")
        self.background = self.settingBoxCanvas.create_image(300, 225,image=self.canvasImg)


        self.rightMenuBox = Frame(self.settingBox, height=450, width=200, background="grey")
        self.rightMenuBox.pack(side=RIGHT)
        self.rightMenuBox.pack_propagate(0)

        self.bottomFrame = Frame(master, height=150, width=1000, background="green")
        self.bottomFrame.pack(side=BOTTOM)

        self.playerHealthArea = Frame(self.bottomFrame, height=150, width=200, background="grey")
        self.playerHealthArea.pack(side=LEFT)
        self.playerHealthArea.pack_propagate(0)

        self.textArea = Frame(self.bottomFrame, height=150, width=600, background="black")
        self.textArea.pack(side=LEFT)
        self.textArea.pack_propagate(0)

        self.firstLineText = Label(self.textArea, text="",font=("helvetica", 20), fg="white", bg="black")
        self.firstLineText.pack(side=TOP)
        self.secondLineText = Label(self.textArea, text="", font=("helvetica", 20), fg="white", bg="black")
        self.secondLineText.pack()
        self.thirdLineText = Label(self.textArea, text="", font=("helvetica", 20), fg="white", bg="black")
        self.thirdLineText.pack()

        self.enemyHealthArea = Frame(self.bottomFrame, height=150, width=200, background="grey")
        self.enemyHealthArea.pack(side=LEFT)
        self.enemyHealthArea.pack_propagate(0)

        self.playerHealthTitle = Label(self.playerHealthArea, text="Health", font=("Helvetica", 25), bg="grey")
        self.playerHealthTitle.pack(side=TOP)

        self.playerHealthText = Label(self.playerHealthArea, text=str(char.health) + " / " + str(char.maxHealth),
                                      font=("Helvetica", 20), bg="Grey")
        self.playerHealthText.pack()

        self.healthBarVar = IntVar()
        self.healthBarVar.set(char.health)
        self.playerHealthBar = Progressbar(self.playerHealthArea, orient=HORIZONTAL, length=100, variable=self.healthBarVar,
                                           maximum=char.maxHealth)
        self.playerHealthBar.pack()

        self.testHealthButton = Button(self.playerHealthArea, text="test", command=lambda: self.decreaseHealth(char))
        self.testHealthButton.pack()

    def displayEnemyHealth(self, ENEMY, charact):
        self.enemyHealthTitle = Label(self.enemyHealthArea, text=ENEMY.name + " Health", font=("Helvetica", 20), bg="grey")
        self.enemyHealthTitle.pack(side=TOP)

        self.enemyImage = self.settingBoxCanvas.create_image(300, 225, image=ENEMY.image)

        self.enemyHealthText = Label(self.enemyHealthArea, text=str(ENEMY.health) + " / " + str(ENEMY.maxHealth),
                                      font=("Helvetica", 20), bg="Grey")
        self.enemyHealthText.pack()
        self.enemyHealthBarVar = IntVar()
        self.enemyHealthBarVar.set(ENEMY.health)
        self.enemyHealthBar = Progressbar(self.enemyHealthArea, orient=HORIZONTAL, length=100, variable=self.enemyHealthBarVar,
                                           maximum=ENEMY.maxHealth)
        self.enemyHealthBar.pack()

        self.testEnemyHealthButton = Button(self.enemyHealthArea, text="test", command=lambda: ENEMY.attack(charact, self))
        self.testEnemyHealthButton.pack()



    def hideEnemyHealth(self):
        self.enemyHealthText.pack_forget()
        self.enemyHealthTitle.pack_forget()
        self.enemyHealthBar.pack_forget()
        self.testEnemyHealthButton.pack_forget()
        self.settingBoxCanvas.delete(self.enemyImage)

    def decreaseHealth(self, CHARACTER):
        if CHARACTER.health > 0:
            CHARACTER.health -= 1
            self.updateHealthBar(CHARACTER)

    def updateHealthBar(self, CHARACTER):
        if isinstance(CHARACTER, Character):
            self.healthBarVar.set(CHARACTER.health)
            self.playerHealthText.config(text=str(CHARACTER.health) + " / " + str(CHARACTER.maxHealth))

        elif isinstance(CHARACTER, Enemy):
            self.enemyHealthBarVar.set(CHARACTER.health)
            self.enemyHealthText.config(text=str(CHARACTER.health) + " / " + str(CHARACTER.maxHealth))

    def displayText(self, text):
        self.firstLineText.config(text='')
        self.secondLineText.config(text='')
        self.thirdLineText.config(text='')

        if len(text) > 40:
            count = 0
            self.firstLine = ''
            self.secondLine = ''
            self.thirdLine = ""
            self.firstLineFull=False
            self.secondLineFull=False
            for i in text:
                count += 1
                if count <= 38:
                    self.firstLine = self.firstLine + i
                elif count > 38 and i != " " and not self.firstLineFull:
                    self.firstLine = self.firstLine + i
                elif count > 38 and i == " ":
                    self.firstLineFull=True

                if self.firstLineFull and not self.secondLineFull and count < 90:
                    self.secondLine = self.secondLine + i
                elif self.firstLineFull and count > 80 and i != " " and not self.secondLineFull:
                    self.secondLine = self.secondLine + i
                elif count > 85 and i == " ":
                    self.secondLineFull = True

                if count > 90 and self.firstLineFull and self.secondLineFull:
                    self.thirdLine = self.thirdLine + i
        else:
            self.firstLine = text
            self.secondLine = ''
            self.thirdLine = ""

        self.firstLineText.config(text=self.firstLine)
        self.secondLineText.config(text=self.secondLine)
        self.thirdLineText.config(text=self.thirdLine)

    def displayBattleMenu(self, char, ENEMY, master):
        self.battleMenuTitle = Label(self.battleOptionsBox, text="Battle Menu", font=("helvetica", 28), bg="grey")
        self.battleMenuTitle.pack(side=TOP)

        self.attackButton = Button(self.battleOptionsBox, text="Attack", width=8, font=("helvetica", 20), pady=2,
                                   command=lambda: char.attack(ENEMY, self, master))
        self.attackButton.pack()
        self.attackButton.bind("<Enter>", self.attackDescription)

        self.defendButton = Button(self.battleOptionsBox, text="Defend", width=8, font=("helvetica", 20), pady=2,
                                   command=lambda: char.defend(ENEMY, self, master))
        self.defendButton.pack()
        self.defendButton.bind("<Enter>", self.defendDescription)

        self.useItemButton = Button(self.battleOptionsBox, text="Use Item", width=8, font=("helvetica", 20), pady=2,
                                    command=lambda: self.displayCharacterInventory(char, ENEMY, master))
        self.useItemButton.pack()
        self.useItemButton.bind("<Enter>", self.useItemDescription)

        self.magicButton = Button(self.battleOptionsBox, text="Magic", width=8, font=("helvetica", 20), pady=2)
        self.magicButton.pack()
        self.magicButton.bind("<Enter>", self.magicDescription)

        self.fleeButton = Button(self.battleOptionsBox, text="Flee", width=8, font=("helvetica", 20), pady=2,
                                 command=lambda: char.flee(ENEMY, self, master))
        self.fleeButton.pack()
        self.fleeButton.bind("<Enter>", self.fleeDescription)

    def hideBattleMenu(self):
        self.useItemButton.pack_forget()
        self.attackButton.pack_forget()
        self.magicButton.pack_forget()
        self.fleeButton.pack_forget()
        self.defendButton.pack_forget()
        self.battleMenuTitle.pack_forget()

    def displayCharacterInventory(self, CHARACTER, ENEMY, master):

        self.hideBattleMenu()
        self.inventoryTitle = Label(self.battleOptionsBox, text="Inventory", font=("helvetica", 28), bg="grey")
        self.inventoryTitle.pack(side=TOP)
        for key in CHARACTER.inventory:
            if key == "Gold" and (CHARACTER.inventory["Gold"])["Amount"] > 0:
                self.goldButton = Button(self.battleOptionsBox, text="x" + str((CHARACTER.inventory["Gold"])["Amount"])
                                                                     + " Gold", width=8, font=("helvetica", 20), pady=2,
                                         command=lambda: self.displayText("What are you gonna do, pay him off?"))
                self.goldButton.pack()
                self.goldButton.bind("<Enter>",
                                     lambda e: self.displayText((CHARACTER.inventory["Gold"])["Description"]))
            if key == "Stick" and (CHARACTER.inventory["Stick"])["Amount"] > 0:
                self.stickButton = Button(self.battleOptionsBox, text="x" + str((CHARACTER.inventory["Stick"])["Amount"]) + " Stick", width=8, font=("helvetica", 20), pady=2,
                                          command=lambda: self.displayText("This is a stick... what could you possibly accomplish with this?"))
                self.stickButton.pack()
                self.stickButton.bind("<Enter>",
                                      lambda e: self.displayText((CHARACTER.inventory["Stick"])["Description"]))
            if key == "Health Potion" and (CHARACTER.inventory["Health Potion"])["Amount"] > 0:
                self.potionButton = Button(self.battleOptionsBox,
                                          text="x" + str((CHARACTER.inventory["Health Potion"])["Amount"]) + " Health \nPotions", width=8,
                                          font=("helvetica", 20), pady=4,
                                          command=lambda : CHARACTER.usePotion(self, ENEMY, master))
                self.potionButton.pack()
                self.potionButton.bind("<Enter>",
                                      lambda e: self.displayText((CHARACTER.inventory["Health Potion"])["Description"]))

        self.backToBattleMenuButton = Button(self.battleOptionsBox, text="Back",  font=("helvetica", 20), pady=2,
                                             command=lambda: self.backToBattleMenu(CHARACTER, ENEMY, master))
        self.backToBattleMenuButton.pack(side=BOTTOM)

    def hideCharacterInventory(self):
        self.goldButton.pack_forget()
        self.potionButton.pack_forget()
        self.stickButton.pack_forget()
        self.inventoryTitle.pack_forget()
        self.backToBattleMenuButton.pack_forget()

    def backToBattleMenu(self, CHARACTER, ENEMY, master):
        self.hideCharacterInventory()
        self.displayBattleMenu(CHARACTER, ENEMY, master)

    def attackDescription(self, event):
        self.displayText("Attack the enemy with your weapon.")
    def defendDescription(self, event):
        self.displayText("Ready yourself to defend against the enemy.")
    def useItemDescription(self, event):
        self.displayText("Open your inventory and use an Item.")
    def magicDescription(self, event):
        self.displayText("Open your spell list, if you have unlocked magic.")
    def fleeDescription(self, event):
        self.displayText("Attempt to flee from the battle.")
root = Tk()

root.title("SwordQuest Test")
root.geometry("1000x600")
dude = Character("Test Character")
testEnemy = Enemy("Skeleton", 20, 20, 4, 2)
testGameWindow = GameWindow(root, dude)

battle(dude, testEnemy, testGameWindow, root)


root.mainloop()

