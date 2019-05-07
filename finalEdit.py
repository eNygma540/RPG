#-------------------------------------------------------------------------+
#Program name: IT209_A9.py                                                |
#Authors: Brendon Lugo                                                    |
#          William Duggleby                                               |
#Date Written: 4/17/19                                                    |
#Purpose: Assignment 9 for IT209 and George Mason University              |  
#-------------------------------------------------------------------------+
print("Welcome to the start of Assignment 9...")
from os import system, name
import random
#clear function created by mohit_negi @ Geeksforgeeks.com
#https://www.geeksforgeeks.org/clear-screen-python/
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

class Char():
    def __init__(self, Name, Hp, Att, Sp):   #Added Sp for Speical Move funcationality
        self.Name= str(Name)
        self.Hp= int(Hp)
        self.Att= int(Att)
        self.Sp = int(Sp)
        #self.Bag = []                       #Change from UML Char has bag rather than UI

    def __str__(self):
        print("**put ascii drawing here**")

    #def Access_Bag(Bag):
        #for i in bag:
            #print i

    def Use_Ability(self,Move, Move_Cost, Name, Type):
        if self.Mag >= Move_Cost:
            self.Mag -= Move_Cost
            if Type == "Att":
                Move_Type = "Att"
                print(self.name,' uses ',Name,'! Dealing',Move,'damage. Now ',self.name,'has',self.Mag,' Mag left.')
                return Move_Type
                #self.Att += Move
            if Type == "Hp":
                Move_Type = "Hp"
                print(self.name,' uses ',Name,'! Gaining',Move,"health. Now ",self.name,'has',self.Mag,' Mag left.')
                return Move_Type
                #self.Hp += Move
        else:
            print("You do not have enough Magic for that!")

class Mage(Char):
    def __init__(self, Name, Hp, Att, Sp, Mag, c_type, Move_Cost):
        super().__init__(Name, Hp, Att, Sp)
        self.Mag = 4
        self.c_type = 'm'
        self.Move_Cost = 1

    def __str__(self):
        print("put drawing in here")

    def Ability(self):
        Name = "FireBall"
        Move = self.Sp + 3
        #Move_Cost = 1
        Type = "Att"
        return self.Use_Ability(Move, self.Move_Cost, Name, Type)

class Knight(Char):
    def __init__(self, Name, Hp, Att, Sp, Mag, c_type, Move_Cost):
        super().__init__(Name, Hp, Att, Sp)
        self.Mag = 4
        self.c_type = 'k'
        self.Move_Cost = 1

    def __str__(self):
        print("put drawing in here")

    def Ability(self):
        Name = "Heal"
        Move = self.Sp + 2
        #Move_Cost = 1
        Type = "Hp"
        return self.Use_Ability(Move, self.Move_Cost, Name, Type)

class Archer(Char):
    def __init__(self, Name, Hp, Att, Sp, Mag, c_type, Move_Cost):
        super().__init__(Name, Hp, Att, Sp)
        self.Mag = 4
        self.c_type = 'a'
        self.Move_Cost = 1

    def __str__(self):
        print("put drawing in here")

    def Ability(self):
        Name = "Rain Arrows"
        Move = self.Sp + 2
        #Move_Cost = 1
        Type = "Att"
        return self.Use_Ability(Move, self.Move_Cost, Name, Type)
#---------------Character Class Above, Enemy Below -----------------------------------
class Mob():
    def __init__(self, Hp, Att):   #Added Sp for Speical Move funcationality
        self.Hp= int(Hp)              #Removed Name, mobs dont have uquie names
        self.Att= int(Att)
            
class Dragon(Mob):
    def __init__(self,Hp, Att, ID):
        super().__init__(Hp, Att)
        self.ID = str(ID)
        self.Moves= ["Fire Breath","Dragon's Claw","Tail Whip","Glazing Stare"]
        
    def __str__(self):
        return(dragon)

    def openmsg(self):
        return("An adolesent dragon appears!")

class Wolf(Mob):
    def __init__(self, Hp, Att, ID):
        super().__init__(Hp, Att)
        self.ID = str(ID)
        self.Moves= ["a loud howl","a fierce bite","a swift claw","a powerful tail Whip"]
        
    def __str__(self):
        return(wolfImg)

    def openmsg(self):
        return("A wild wolf appears!")

class Zombie(Mob):
    def __init__(self, Hp, Att, ID):
        super().__init__(Hp, Att)
        self.ID = str(ID)
        self.Moves= ["a fierce bite","a heavy claw","a loud screech","a decaying burst of ancient energy"]
        
    def __str__(self):
        return(zombieImg)
        
    def openmsg(self):
        return("A wild zombie appears!")

class Boss(Mob):
    def __init__(self, Hp, Att, ID):
        super().__init__(Hp, Att)
        self.ID = str(ID)
        self.Moves= ["Python Mastery","Lazer Eyes","Fire Breath","One Inch Punch"]
        
    def __str__(self):
        return(profImg)
        
    def openmsg(self):
        return("The storm is upon you! The edge of the storm is quickly gaining ground on you,\ntry as you might you are not able to out run it. The sky turns dark around you, and thick, heavy droplets\n rain down against your skin. Lighting crackles and momentairy lights your path.\nYou breifly see a figure standing before you. They seem to be the epicentor of the storm..." +
               "\mThe rain bends and curves around the figure, creating a sphere of air with no rain. This sphere extends itself\ntowards you and blocks the rain from falling, allowing you to see. \n\nI am the gurdian of this world, and you have tresspassed here long enough.\nIts time to send you where you belong.\n\nNow that you can clearly see, you read the name tag on the figure. It says Professor Shuman, Python Master.\nBefore you have time to speak he attacks!")

#-------------------Enemies Above, Biome Below--------------------
class Biome():
    def __init__(self,Forest_Area, Mountian_Area, Sand_Area, choice):
        self.Forest_Area = Forest_Area
        self.Mountian_Area = Mountian_Area
        self.Sand_Area = Sand_Area
        self.choice = "G"
        
    def PickArea(self, Area):
        if Area.lower() == "f":
            self.choice = "f"

        elif Area.lower() == "m":
            self.choice = "m"
            
        elif Area.lower() == "d":
            self.choice = "d"
        else:
            print("You entered an incorrect choice.")

    def setChoice(self,new):
        self.choice = new
        return self.choice

    def PickAreaEvent(self,choice):
        if choice == "F":
            Event = random.choice(self.Forest_Area)
            print('''
You find yourself in an area that you recognize as''',Event)
        elif choice == "M":
            Event = random.choice(self.Mountian_Area)
            print('''
You find yourself in an area that you recognize as''',Event)
        elif choice == "D":
            Event = random.choice(self.Sand_Area)
            print('''
You find yourself in an area that you recognize as''',Event)
            

        
#---------BIOME CLASS ABOVE, ITEMS CLASS BELOW------------------------
class Items():
    def __init__(self,knightems,archItems,mageItems):
            self.knightems = knightems
            self.archItems = archItems
            self.mageItems = mageItems

    def getItems(self):
        if Player.c_type == "k":
            print("You find one:",random.choice(list(self.knightems)),"!")
        elif Player.c_type == "m":
            print("You find one:",random.choice(list(self.mageItems)),"!")
        elif Player.c_type == "a":
            print("You find one:",random.choice(list(self.archItems)),"!")
            
gameItems= Items({'Apple':1,"Rubber Chicken":2,"Turkey leg":3, "Dagger":4,"Chipotle":5,"Broadsword":6,"Big Mac":7,"Greataxe":8},
                 {'Apple':1,"Nerf bow":2,"Turkey leg":3, "longbow":4,"Chipotle":5,"Crossbow":6,"Big Mac":7,"Magic bow":8},
                 {'Apple':1,"Useless stick":2,"Turkey leg":3, "Magic wand":4,"Chipotle":5,"Spellbook":6,"Big Mac":7,"Choatic staff":8}
                  )

#---------ITEMS CLASS ABOVE, CONTROLLER CLASS BELOW------------------------

class controller():
    def __init__(self, turnCount, bag, title, choose, Player):
        self.turnCount = 0
        self.bag = []
        self.title = title
        self.choose = choose
        self.Player = ""

    def TriggerItem(self):
        if Player.c_type == "k":
            PlayerItems = {'Apple':1,"Rubber Chicken":2,"Turkey leg":3, "Dagger":4,"Chipotle":5,"Broadsword":6,"Big Mac":7,"Greataxe":8}
        elif Player.c_type == "m":
            PlayerItems = {'Apple':1,"Nerf bow":2,"Turkey leg":3, "longbow":4,"Chipotle":5,"Crossbow":6,"Big Mac":7,"Magic bow":8}
        elif Player.c_type == "a":
            PlayerItems = {'Apple':1,"Useless stick":2,"Turkey leg":3, "Magic wand":4,"Chipotle":5,"Spellbook":6,"Big Mac":7,"Choatic staff":8}
            
        itemPickup = random.randint(1,10)
        if itemPickup in range(1,4):
            pick = random.randint(0,7)
            current_item = []
            current_item.append(list(PlayerItems)[pick - 1])
          
            if pick%2 == 0:
                print("You found a", current_item," that you are now wielding and your attack is now", pick)
                Player.Att += pick
            else:
                print("You found a", current_item," that you consume quickly and gain the following hp:",pick)
                Player.Hp += pick
        else:
            controller.TriggerMob()
    
    def TriggerMob():
        itemPickup = random.randint(1,10)
        if itemPickup in range(1,3):
            zombieMob = Zombie(8,2,"Zombie")
            BattleMob = zombieMob
            controller.TriggerBattle(BattleMob,zombieAtt,wolfAtt,dragonAtt)
        elif itemPickup in range(4,6):
            wolfMob = Wolf(10,2,"Wolf")
            BattleMob = wolfMob
            controller.TriggerBattle(BattleMob,zombieAtt,wolfAtt,dragonAtt)
        elif itemPickup in range(7,9):
            dragonMob = Dragon(14,3,"Dragon")
            BattleMob = dragonMob
            controller.TriggerBattle(BattleMob,zombieAtt,wolfAtt,dragonAtt)
        else:
            print("Oof, bad luck... You didn't find anything.")

    def TriggerBattle(BattleMob,zombieAtt,wolfAtt,dragonAtt):
        BattleMob = BattleMob
        print(BattleMob)
        print(BattleMob.openmsg())
        while BattleMob.Hp > 0 and Player.Hp > 0:
            BattleMob_Turn = random.randint(1,2)
            if BattleMob_Turn == 1:
                Player.Hp -= BattleMob.Att
                if Player.Hp >0:
                    if BattleMob.ID == 'Zombie':
                        print(zombieAtt)
                    elif BattleMob.ID == 'Wolf':
                        print(wolfAtt)
                    elif BattleMob.ID =='Dragon':
                        print(dragonAtt)
                    print("The enemy attacks with",random.choice(BattleMob.Moves),
                                  "- You have", Player.Hp,"health remaining.")
                else:
                    if BattleMob.ID == 'Zombie':
                        print(zombieAtt)
                    elif BattleMob.ID == 'Wolf':
                        print(wolfAtt)
                    elif BattleMob.ID =='Dragon':
                        print(dragonAtt)
                    print("The enemy attacks with a",random.choice(BattleMob.Moves),
                                  "- You have 0 health. You died!!")
                    input("...")
                    break
            else:
                print("The ",BattleMob.ID," attack missed you!")
            if Player.Hp < 1:
                self.turnCount = 6
                break
            else:
                pass
            print("\n\nWhat will you do?")
            print("Player Health:",Player.Hp)
            print("Player Attack:",Player.Att,)
            print("You have",Player.Mag,"Magic left. Player Special Cost:",Player.Move_Cost,)
            action = input("\n1. for basic Attack\n2. to use your Special:") #put validtoin here
            if action == "1":
                BattleMob.Hp -= Player.Att
                if Player.c_type == 'm':
                    print(mageAtt)
                elif Player.c_type == 'k':
                    print(knightAtt)
                elif Player.c_type =='a':
                    print(archerAtt)
                print("You attack the",BattleMob.ID,"!")
                
                if BattleMob.Hp <= 0:
                    print("The enemy has lost all its health!!")
                else:
                    print("\nThe enemy now has",BattleMob.Hp,"health remaining.")
            elif action == "2":
                Move_Type = []
                Move_Type.append(Player.Ability())
                if Move_Type[0] == "Att":
                    BattleMob.Hp -= Player.Att + Player.Sp
                    if Player.c_type == 'm':
                        print(mageSp)
                    elif Player.c_type =='a':
                        print(archerSp)
                else:
                    Player.Hp += Player.Sp + 2
                    if Player.c_type == 'k':
                        print(knightSp)
                
        if Player.Hp >0:
            print("You defeated a",BattleMob.ID)
        elif Player.Hp <= 0:
            control.turnCount += 10
            clear()
            print(gameOver)
            print(graveStone)
            controller.endCredits()
            input("Hit enter to leave the game....")

##################################
    def TriggerBoss(BattleMob):
        BattleMob = BattleMob
        print(BattleMob.openmsg())
        input("Hit enter to move continue...")
        print(BattleMob)
        while BattleMob.Hp > 0 and Player.Hp > 0:
            BattleMob_Turn = random.randint(1,4)
            if BattleMob_Turn < 4:
                Player.Hp -= BattleMob.Att
                if Player.Hp >0:
                    attack = random.choice(BattleMob.Moves)
                    if attack == "Python Mastery":
                        print(ShumanPM)
                    elif attack == "Lazer Eyes" :
                        print(ShumanLE)
                    elif attack == "Fire Breath":
                        print(ShumanFB)
                    elif attack == "One Inch Punch":
                        print(ShumanOip)
                    print("The enemy attacks with",attack,
                                  "- You have", Player.Hp,"health remaining.")
                else:
                    attack = random.choice(BattleMob.Moves)
                    if attack == "Python Mastery":
                        print(ShumanPM)
                    elif attack == "Lazer Eyes" :
                        print(ShumanLE)
                    elif attack == "Fire Breath":
                        print(ShumanFB)
                    elif attack == "One Inch Punch":
                        print(ShumanOip)
                    print("The enemy attacks with",attack,
                                  "- You have 0 health. You died!!")
                    input("...")
                    break
            else:
                print(BattleMob.ID," missed you!")
            if Player.Hp < 1:
                self.turnCount = 6
                break
            else:
                pass
            print("\n\nWhat will you do?")
            print("Player Health:",Player.Hp)
            print("Player Attack:",Player.Att,)
            print("You have",Player.Mag,"Magic left. Player Special Cost:",Player.Move_Cost,)
            action = input("\n1. for basic Attack\n2. to use your Special:") #put validtoin here
            if action == "1":
                BattleMob.Hp -= Player.Att
                if Player.c_type == 'm':
                    print(mageAtt)
                elif Player.c_type == 'k':
                    print(knightAtt)
                elif Player.c_type == 'a':
                    print(archerAtt)
                print("You attack",BattleMob.ID,"!")
                if BattleMob.Hp <= 0:
                    print("The enemy has lost all its health!!")
                else:
                    print("\nThe enemy now has",BattleMob.Hp,"health remaining.")
                
                if BattleMob.Hp <= 0:
                    print("The enemy has lost all its health!!")
                    print("\nCongrats! You defeated Professor Shuman, guardian of the world.")
                else:
                    print("\nThe enemy now has",BattleMob.Hp,"health remaining.")
            elif action == "2":
                Move_Type = []
                Move_Type.append(Player.Ability())
                if Move_Type[0] == "Att":
                    BattleMob.Hp -= Player.Att + Player.Sp
                    if Player.c_type == 'm':
                        print(mageSp)
                    elif Player.c_type =='a':
                        print(archerSp)
                else:
                    Player.Hp += Player.Sp + 2
                    if Player.c_type == 'k':
                        print(knightSp)
        if Player.Hp >0:
            print("You defeated",BattleMob.ID)
            control.turnCount = 7
            exit
        elif Player.Hp <= 0:
            control.turnCount =+ 10
            exit

###################################

    def PlayerClass(self):
        if self.turnCount == 0:
            time.sleep(5)
            print(title)
            time.sleep(4)
            clear()
            print(choose)
            time.sleep(3)

            classType = input('''
            --- Knight
            --- Mage
            --- Archer
            Enter 1 of the above class choices: ''')        
            while classType.lower() not in("knight","mage","archer"):                   #Validation for which class
                print("Please Enter a Valid Class")
                classType = input('''
            --- Knight
            --- Mage
            --- Archer
            Enter 1 of the above class choices: ''')
            Char.name = input("What is your name?: ")
            if classType.lower() == "knight":
                PlayerK = Knight(name,11,2,4,5,'k',1)
                self.Player = PlayerK
                return self.Player
            elif classType.lower() == "archer":
                PlayerA = Archer(name,5,3,4,5,'a',1)
                self.Player = PlayerA
                return self.Player
            elif classType.lower() == "mage":
                PlayerM = Mage(name,8,4,4,5,'m',1)
                self.Player = PlayerM
                return self.Player
            
    def startWorld(self):
        clear()
        if Player.c_type == 'm':
            print(wizardImg)
        elif Player.c_type == 'a':
            print(archerImg)
        elif Player.c_type == 'k':
            print(knightImg)
        
        print("Welcome, ",self.Player.name,"...")
        print('''
        Before you, you see mountains made of a dark black rock. They look dangerous,
        but the reward has to be worth it... right?
        To the left you notice an large forest. Probably some cute squirrels or something
        To your right you see a desert in the distance. Looks dry. I bet there's a nice
        tanning spot down this way.
        ''')
        choice = input(
        '''
        -- Mountains
        -- Forest
        -- Desert
        Would you like to go to the mountains, forest, or desert?(F,M,D): ''')
        while choice.upper() not in("F","M","D"):                                           #Validation for which area
            print("Please pick a valid choice:")
            choice = input(
            '''
            -- Mountains
            -- Forest
            -- Desert
            Would you like to go to the mountains, forest, or desert?(F,M,D): ''')
        if choice.upper() == "F":                                                         #Valor text about which area to choose
            cloud = "Forest"
            print("""
            With the wind in your hair and bugs chittering around you, you head towards the 
            large forest. You have spent some time travelling along the well worn dirt path
            beneath your feat when your senses spot something. That cute squireel perhaps?
            You stop and gather in your surroundings...""")
                
        elif choice.upper() == "M":
            cloud = "Mountains"
            print("""
            You decide to head towards the mountain made of dark rock. As you get closer you
            spot a winding trail that grips to the mountains edge. By the time you have made it
            to the begining of the trail, the air is cold and stale. Something about this
            mountain makes your skin crawl. You decied to stop, catch your breath, and take
            in your surroundings...
            """)
        elif choice.upper() == "D":
            cloud = "Desert"
            print("""
            You trod on down the slopes towards the desert. With the sand blowing past your
            face and the sun beating down your neck you feel confident in your choice.
            As you walk, you begin to notice high dunes besides you and you wonder how
            long they have stood. In the distance you hear a sharp jackle and your hair
            stands on edge. Perhaps someone, or something, is also wandering among the
            dunes. You stand at ease and being to take in your surroundings...
            """)
            
        CloudMsg = ["As you continue along your journey,  you stop to gaze up upon the clouds.\nA curious thing catches your eye. In the distance you can see what you can only describe as a faint,\ndark object on the horizon. You blink, and it's gone! Hopefully it was nothing...",
                    "Having progessed further along towards your destination you stop to take a rest.\nBefore your eyes fully close you note that the object on the horizion you saw eariler has reappeared,\nbigger in size yet still quit some distance away. You note that it may be a strom, but quickly dirft to sleep.",
                    "Now that you have made considerable progress through the area you are suddenly\naware of a dark presence near you. You look up and realize that the dark object from before was\nindeed a storm, a big one too it appears. Hopefully, you will reach your destination before it hits you...",
                    "The storm is making quick  time, and you feel the air around you get colder.\nThe air tastes moist, and the sky is a deep, dark grey. You quickly push on towards the center of the area!",
                    "The storm is upon you! The edge of the storm is quickly gaining ground on you,\ntry as you might you are not able to out run it. The sky turns dark around you, and thick, heavy droplets\n rain down against your skin. Lighting crackles and momentairy lights your path.\nYou breifly see a figure standing before you. They seem to be the epicentor of the storm...",
                    "Death greets you...\n",
                    "The clouds begin to clear up!\n"]
        
        GameWorld = Biome(['Red Wood National Park','The Spooky Woods','Hidden Grove',"The Witch's Hut"],
                ['Mount Denali National Park','The Snowy Peaks','The Raging River','The Abandoned Cabin'],
                ['The Grand Canyon','The Oasis',"Mars' Dunes",'The Hidden Cave'],'G')
        GameWorld.PickArea(choice)
        self.turnCount += 1
        run = True
        while run == True:
            #while self.turnCount <= 5:
                if self.turnCount < 5:
                    GameWorld = Biome(['Red Wood National Park','The Spooky Woods','Hidden Grove',"The Witch's Hut"],
                        ['Mount Denali National Park','The Snowy Peaks','The Raging River','The Abandoned Cabin'],
                        ['The Grand Canyon','The Oasis',"Mars' Dunes",'The Hidden Cave'],'G')
                    GameWorld.PickAreaEvent(choice)
                    fobjects = ["bird's nest","some shrubs","a hollowed out log","a stone caked in moss","a vibrant patch of mushrooms","some wild bushes","some underbrush","a briar patch","waist high grass"]
                    dobjects = ['a skeleton','a broken cart','a shallow cave',"a tumble weed","a colorful cactus","a spikey cactus","a small dune","a patch of dead grass","an antelope skull","a large boulder"]
                    mobjects = ['a broken cart','a shallow cave','an abandoned mineshaft',"a jagged rock","a smooth stone","a puddle","crevace","a patch of weeds","a mound of gravel","a mossy stone"]
                    if choice in "forestsForests":
                      entry = input("\nTo your left you see "+random.choice(fobjects)+ ". To your right you see "+random.choice(fobjects)+". Which do you search?: ")
                    if choice in "desertsDeserts":
                      entry = input("\nTo your left you see "+random.choice(dobjects)+ ". To your right you see "+random.choice(dobjects)+". Which do you search?: ")
                    if choice in "mountainsMountains":
                      entry = input("\nTo your left you see "+random.choice(mobjects)+ ". To your right you see "+random.choice(mobjects)+". Which do you search?: ")
                    
                    entry = input("\nTo your left you see "+random.choice(fobjects)+ ". To your right you see "+random.choice(fobjects)+". Which do you search?: ")
                    print("\n")
                    controller.TriggerItem(Player)
                    input("Hit Enter to Move on...")
                    time.sleep(2)
                    clear()
                    print("\n\n",CloudMsg[self.turnCount - 1].strip("'"),"\n\n")
                    self.turnCount += 1
                    input("Hit Enter to Move on...")
                    
                elif self.turnCount == 5:
                    controller.endGame()
                    
                elif self.turnCount >= 10:
                    clear()
                    print(gameOver)
                    print(graveStone)
                    controller.endCredits()
                    input("Hit enter to leave the game....")
                    break
                    
                elif self.turnCount == 7:
                    clear()
                    time.sleep(3)
                    print(win)
                    controller.endCredits()
                    input("\nHit enter to leave the game....")
                    break

    def endGame():
        Professor_Shuman = Boss(20,3,"Professor Shuman")
        BattleMob = Professor_Shuman
        controller.TriggerBoss(BattleMob)
        input = ("Thanks for playing our game!")

    def endCredits():
        for i in creditPage:
            print(i,"\n")
            time.sleep(2)

#-------------Openning Credits-------------------------------
import time
import random
#import pygame



creditPage = [
"Written by Billy Duggleby and Brendon Lugo for IT209 at George Mason University, Spring 2019.",
"Ascii art wizard created by Morfina at www.asciiart.eu",
"Ascii art knight created by fsc at http://ascii.co.uk",
"Ascii art archer created by Erorppn Xrzavgm at http://ascii.co.uk",
"Ascii art wolf created by bug at https://www.asciiart.eu/animals/wolves",
"Ascii art dragon created by Joan at asciiart.website//joan/www.geocities.com",
"Ascii Dragon attack Art by Shanaka Dias",
"Ascii art Zombie by Nabis at https://www.asciiart.eu/mythology/skeletons",
"Ascii zombie attack at http://www.asciiworld.com/-Death-Co-.html",
"Gene Shuman ascii art created at https://www.text-image.com/convert/ascii.html",
"Ascii art snake attack by CJR at http://ascii.co.uk/art/snake",
"Ascii art tombstone by jgs at http://ascii.co.uk/art/rip",
"Clear function created by mohit_negi @ Geeksforgeeks.com",
"https://www.geeksforgeeks.org/clear-screen-python/",
"Ascii GAME OVER by unknown at http://textart4u.blogspot.com/2013/05/game-over-text-art.html",
"Ascii CONGRATS by hjw from http://ascii.co.uk/art/congrats"]
gameOver = '''\
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
'''
graveStone ='''
          
                               -|-
                                |
                            .-'~~~`-.
                          .'         `.
                          |  R  I  P  |
                          |           |
                          |           |
                        \\\\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'''
win = '''
   _____                            _         _       _   _                 _ 
  / ____|                          | |       | |     | | (_)               | |
 | |     ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___| |
 | |    / _ \\| '_ \\ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \\| '_ \\/ __| |
 | |___| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \\__ \\_|
  \\_____\\___/|_| |_|\\__, |_|  \\__,_|\\__|\\__,_|_|\\__,_|\\__|_|\\___/|_| |_|___(_)
                     __/ |                                                    
                    |___/   
                                        .--------.
                                      .: : :  :___`.
                                    .'!!:::::  \\\\_\\ `.
                               : . /%O!!::::::::\\\\_\\. \\
                              [""]/%%O!!:::::::::  : . \\
                              |  |%%OO!!::::::::::: : . |
                              |  |%%OO!!:::::::::::::  :|
                              |  |%%OO!!!::::::::::::: :|
                     :       .'--`.%%OO!!!:::::::::::: :|
                   : .:     /`.__.'\\%%OO!!!::::::::::::/
                  :    .   /        \\%OO!!!!::::::::::/
                 ,-'``'-. ;          ;%%OO!!!!!!:::::'
                 |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
                 | .   :| |_.','`.`._|  `%%%OO!%%'
                 | . :  | |--'    `--|    `%%%%'
                 |`-..-'| ||   | | | |     /__\\`-.
                 \\::::::/ ||)|/|)|)|\\|           /
        ----------`::::'--|._ ~**~ _.|----------( -----------------------
                    )(    |  `-..-'  |           \\    ______
                    )(    |          |,--.       ____/ /  /\\ ,-._.-'
                 ,-')('-. |          |\\`;/   .-()___  :  |`.!,-'`'/`-._
                (  '  `  )`-._    _.-'|;,|    `-,    \\_\\__\\`,-'>-.,-._
                 `-....-'     ````    `--'      `-._       (`- `-._`-.   hjw
'''
choose = '''
      * ***      *                                                                                                          
    *  ****  * **                                                                                                           
   *  *  ****  **                                                                                                           
  *  **   **   **                                                                                                           
 *  ***        **           ****       ****       ****                 **   ****         ****    **   ****     ***  ****    
**   **        **  ***     * ***  *   * ***  *   * **** *    ***        **    ***  *    * ***  *  **    ***  *  **** **** * 
**   **        ** * ***   *   ****   *   ****   **  ****    * ***       **     ****    *   ****   **     ****    **   ****  
**   **        ***   *** **    **   **    **   ****        *   ***      **      **    **    **    **      **     **         
**   **        **     ** **    **   **    **     ***      **    ***     **      **    **    **    **      **     **         
**   **        **     ** **    **   **    **       ***    ********      **      **    **    **    **      **     **         
 **  **        **     ** **    **   **    **         ***  *******       **      **    **    **    **      **     **         
  ** *      *  **     ** **    **   **    **    ****  **  **            **      **    **    **    **      **     **         
   ***     *   **     **  ******     ******    * **** *   ****    *      *********     ******      ******* **    ***        
    *******    **     **   ****       ****        ****     *******         **** ***     ****        *****   **    ***       
      ***       **    **                                    *****                ***                                        
                      *                                                   *****   ***                                       
                     *                                                  ********  **                                        
                    *                                                  *      ****                                          
                   *                                                                                                        
                                                                                                                            
                                                                                                                            
                   ***                           *                                                                                          
                 ** ***    *                   **            *                                                                              
                **   ***  ***                  **           **                                                                              
                **         *                   **           **                                                                              
                **                             **         ********           ***  ****                                                      
                ******   ***         ****      **  ***   ********     ***     **** **** *                                                   
                *****     ***       *  ***  *  ** * ***     **       * ***     **   ****                                                    
                **         **      *    ****   ***   ***    **      *   ***    **                                                           
                **         **     **     **    **     **    **     **    ***   **                                                           
                **         **     **     **    **     **    **     ********    **                                                           
                **         **     **     **    **     **    **     *******     **                                                           
                **         **     **     **    **     **    **     **          **                                                           
                **         **     **     **    **     **    **     ****    *   ***                                                          
                **         *** *   ********    **     **     **     *******     ***                                                         
                 **         ***      *** ***    **    **             *****                                                                  
                                          ***         *                                                                                     
                                     ****   ***       *                                                                                      
                                    *******  **       *                                                                                       
      	                           *     ****        * 
'''

title = '''
                                                                                                                             
     ***** *    **   ***              ***                                                                                    
  ******  *  *****    ***              ***                                                                                   
 **   *  *     *****   ***              **                                                                                   
*    *  **     * **      **             **                                                                                   
    *  ***     *         **             **                  ****                                                             
   **   **     *         **    ***      **       ****      * ***  * *** **** ****       ***                                  
   **   **     *         **   * ***     **      * ***  *  *   ****   *** **** ***  *   * ***                                 
   **   **     *         **  *   ***    **     *   ****  **    **     **  **** ****   *   ***                                
   **   **     *         ** **    ***   **    **         **    **     **   **   **   **    ***                               
   **   **     *         ** ********    **    **         **    **     **   **   **   ********                                
    **  **     *         ** *******     **    **         **    **     **   **   **   *******                                 
     ** *      *         *  **          **    **         **    **     **   **   **   **                                      
      ***      ***      *   ****    *   **    ***     *   ******      **   **   **   ****    *                               
       ******** ********     *******    *** *  *******     ****       ***  ***  ***   *******                                
         ****     ****        *****      ***    *****                  ***  ***  ***   *****                               
                                                                                             *                            
                                                                                             *                           
                                                                                            *                           
                                                                                                                          
                                                                                                                             
                                                                                                                             
        **             **                                                                                                    
     *****              **                                           *                                                       
    *  ***              **   **                                     **                                                       
       ***              **   **                                     **                                                       
      *  **             **    **    ***                           ******** **   ****     ***  ****              ***  ****    
      *  **         *** **     **    ***     ***    ***  ****    ********   **    ***  *  **** **** *    ***     **** **** * 
     *    **       *********   **     ***   * ***    **** **** *    **      **     ****    **   ****    * ***     **   ****  
     *    **      **   ****    **      **  *   ***    **   ****     **      **      **     **          *   ***    **         
    *      **     **    **     **      ** **    ***   **    **      **      **      **     **         **    ***   **         
    *********     **    **     **      ** ********    **    **      **      **      **     **         ********    **         
   *        **    **    **     **      ** *******     **    **      **      **      **     **         *******     **         
   *        **    **    **     **      *  **          **    **      **      **      **     **         **          **         
  *****      **   **    **      *******   ****    *   **    **      **       ******* **    ***        ****    *   ***        
 *   ****    ** *  *****         *****     *******    ***   ***      **       *****   **    ***        *******     ***       
*     **      **    ***                     *****      ***   ***                                        *****                
*                                                                                                                            
 **
'''

zombieImg = '''
                              _.--""-._
  .                         ."         ".
 / \\    ,^.         /(     Y             |      )\\
/   `---. |--'\\    (  \\__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \\  .-' | |  `              l._       _.'
  \\/    | |                   l`^^'^^'j
        | |                _   \\_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \\'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  \\
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. \\
     '._' / \\         _/(   `/   )- ---' ;  /__.J   L.__.\\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\\  __  \\  \\  I   1   / /
        `-'                /   `-\\-(-'   \\ \\  `.|   | ,' /
                           \\__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'
                             )(  l\\ o ('..-.
                       _..--' _'-' '--'.-. |
                __,,-'' _,,-''            \\ \\
               f'. _,,-'                   \\ \\
              ()--  |                       \\ \\
                \.  |                       /  \\
                  \\ \\                      |._  |
                   \\ \\                     |  ()|
                    \\ \\                     \\  /
                     ) `-.                   | |
                    // .__)                  | |
                 _.//7'                      | |
               '---'                         j_| `
                                            (| |
                                             |  \\
                                             |lllj
                                             |||||
'''
zombieAtt = '''
          _,.-----.,_
       ,-~           ~-.
      ,^___           ___^.
    /~"   ~"   .   "~   "~\\
   Y  ,--._    I    _.--.  Y
    | Y     ~-. | ,-~     Y |
    | |        }:{        | |
    j l       / | \\       ! l
 .-~  (__,.--" .^. "--.,__)  ~-.
(           / / | \\ \\           )
 \\.____,   ~  \\/"\\/  ~   .____,/
  ^.____                 ____.^
     | |T ~\\  !   !  /~ T| |
     | |l   _ _ _ _ _   !| |
     | l \\/V V V V V V\\/ j |
     l  \\ \\|_|_|_|_|_|/ /  !
      \  \\[T T T T T TI/  /
       \  `^-^-^-^-^-^'  /
        \               /
         \.           ,/
           "^-.___,-^"

'''
wolfImg = '''
                              __
                            .d$$b
                          .' TO$;\\
                         /  : TP._;
                        / _.;  :Tb|
                       /   /   ;j$j
                   _.-"       d$$$$
                 .' ..       d$$$$;
                /  /P'      d$$$$P. |\\
               /   "      .d$$$P' |\\^"l
             .'           `T$P^"""""  :
         ._.'      _.'                ;
      `-.-".-'-' ._.       _.-"    .-"
    `.-" _____  ._              .-"
   -(.g$$$$$$$b.              .'
     ""^^T$$$P^)            .(:
       _/  -"  /.'         /:/;
    ._.'-'`-'  ")/         /;/;
 `-.-"..--""   " /         /  ;
.-" ..--""        -'          :
..--""--.-"         (\\      .-(\\
  ..--""              `-\(\\/;`
    _.                      :
                            ;`-
                           :\\
                           ;

'''
wolfAtt = '''
             _     ___
            #_~`--'__ `===-,
            `.`.     `#.,//
            ,_\\_\\     ## #\\
            `__.__    `####\\
                 ~~\\ ,###'~
                    \\##'
'''
knightImg = '''
                          ,dM
                         dMMP
                        dMMM'
                        \\MM/
                        dMMm.
                       dMMP'_\\---.
                      _| _  p ;88;`.
                    ,db; p >  ;8P|  `.
                   (``T8b,__,'dP |   |
                   |   `Y8b..dP  ;_  |
                   |    |`T88P_ /  `\;
                   :_.-~|d8P'`Y/    /
                    \\_   TP    ;   7`\\
         ,,__        >   `._  /'  /   `\\_
         `._ """"~~~~------|`\\;' ;     ,'
            """~~~-----~~~'\\__[|;' _.-'  `\\
                    ;--..._     .-'-._     ;
                   /      /`~~"'   ,'`\\_ ,/
                  ;_    /'        /    ,/
                  | `~-l         ;    /
                  `\\    ;       /\\.._|
                    \\    \\      \\     \\
                    /`---';      `----'
                   (     / 
                    `---'
'''
knightAtt = '''
           _____   _____
          /     \\ /     \\
     ,   |       '       |
     I __L________       L__
O====IE__________/     ./___>
     I      \\.       ./
     `        \\.   ./
                \\ /
                 '

'''
knightSp = '''
       @@@@@@           @@@@@@
      @@@@@@@@@@       @@@@@@@@@@
    @@@@@@@@@@@@@@   @@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@
              @@@@@@@@@@@
                @@@@@@@
                  @@@
                   @
'''

wizardImg ='''
                    / \\
                  .'* */
               __/_*_*(_
              / _______ \\
             _\\_)/___\\(_/_ 
            / _((\\0-0/))_ \\
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \\
           / _ \ - | - /_  \\
          (   ( .;""";. .)  )
         _\\"__ /(    )\\ __"/_
            \\/  \\'  ' /  \\/
             ( ' '...' ' )
              / /  |  \\ \\
             / .   .   . \\
            /   .     .   \\
           /   /   |   \\   \\
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._ 
 _.-'       |      BBb       '-.  '-. 
(___________\____.dBBBb.________)____)
'''
mageAtt = '''
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ;.--' ''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
'''
mageSp = '''
                             ____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \\___
- ------===;;;'====------------------===;;;===----- -  -
                  \\/  ~"~"~"~"~"~\\~"~)~"/
                  (_ (   \\  (     >    \\)
                   \\_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
'''

archerImg = '''
                                                       \\. 
                                                      /|.
                                                   /   |.
                                                 /     |.
                                               /       |.
                                             /         |.
                                          /            |.
        -\\                              /              |.
          \\\                          /                |.
           \\\                       /                  |.
            \\|                    /                    |\\
              \\#####\\           /                      ||
          ==###########>      /                        ||
           \\##==      \\     /                          ||
      ______ =       =|___/__                          ||
  ,--' ,----`-,__ ___/'  --,-`-========================##==========>
 \\               '        ##______ ____ ____,--,_____,=##,__
  `,    __==    ___,-,__,--'#'  ==='   `-'           | ##,-/
    `-,____,---'       \\####\\          |     ____,---\_##,/
        #_              |##   \\  __,--==,__,--'        ##
         #              ]===--==\\                      ||
         #,             ]         \\                    ||
          #_            |           \\                  ||
           ##_       __/'             \\                ||
            ####='     |                \\              |/
             ###       |                  \\            |.
             ##       _'                    \\          |.
            ###=======]                       \\        |.
           ///        |                         \\      |.
           //         |                           \\    |.
                                                    \\  |.
                                                      \\|.
                                                       /.
'''
archerAtt = '''
                     z$6*#""""*c     :@$$****$$$$L
                  .@$F          "N..$F         '*$$
                 /$F             '$P             '$$r
                d$"                                #$      '%C"""$
               4$F                                  $k    ud@$ JP
               M$                                   J$*Cz*#" Md"
               MR                              'dCum#$       "
               MR                               )    $
               4$                                   4$
                $L                                  MF
                '$                                 4$
                 ?B .z@r                           $
               .+(2d"" ?                          $~
    +$c  .z4Cn*"   "$.                           $
'#*M3$Eb*""         '$c                         $
   /$$RR              #b                      .R
   6*"                 ^$L                   JF
                         "$                 $
                           "b             u"
                             "N.        xF
                               '*c    zF
                                  "N@"

'''
archerSp = '''

           `@@_
            @@@L
      .d@L,]@@@@L,
-z__   ]@@@a@@@@@@_
 `@@@@zza@@@@@@@@@@L
  `]@@@@@@@@@@@@@@@@@_
    `@@@@@@@@@@@@@@@@@L
     `-@@@@@@@@@@@@@@@@'
       `@@@@@@@@@@@@@@[
        `@@@@@@@@@@@@@[
          ]@@@@@@@@@@@[
           "~~~~-@@@@@@,
                  "~-@@@_
                     ~@@@L
                      `@@@L_
                       `~@@@L
                         `@@@z,
                          `]@@@_
                            `@@@z
                             `]@@L_
                               ~@@@z
                                `@@@z,
                                 `]@@@L
                                   `@@@z
                                     ]@@L,
                                      ~@@@z
                                       "@@@z
                                        `-@@@_
                                          ~@@@_
                                           `@@@z
                                            `-@@@_
                                              ]@@@_
                                               "@@@z
                                                `]@@L,
                                                  `@@@L
                                                   `@@@z,
                                                    `-@@@_
                                                      `@@@L
                                                       `@@@L    ]e
                                                         ~@@b_  a@b
                                                          `@@@e]@@L
                                                    -zzzz___@@@U@@@,
                                                      "~-@@@@@@@@@@@
                                                         `~-@@@@@@@@L
                                                            "~-@@@@@@,
                                                               "~@@@@L
                                                                 `~@@@e
                                                                    ~@@_
                                                                      ~@
'''
dragon = '''
                                                    ___
                                                  .~))>>
                                                 .~)>>
                                               .~))))>>>
                                             .~))>>             ___
                                           .~))>>)))>>      .-~))>>  
                                         .~)))))>>       .-~))>>)>
                                       .~)))>>))))>>  .-~)>>)>
                   )                 .~))>>))))>>  .-~)))))>>)>
                ( )@@*)             //)>))))))  .-~))))>>)>
              ).@(@@               //))>>))) .-~))>>)))))>>)>
            (( @.@).              //))))) .-~)>>)))))>>)>
          ))  )@@*.@@ )          //)>))) //))))))>>))))>>)>
       ((  ((@@@.@@             |/))))) //)))))>>)))>>)>
      )) @@*. )@@ )   (\\_(\\-\\b  |))>)) //)))>>)))))))>>)>
    (( @@@(.@(@ .    _/`-`  ~|b |>))) //)>>)))))))>>)>
     )* @@@ )@*     (@) (@)  /\b|))) //))))))>>))))>>
   (( @. )@( @ .   _/       /  \b)) //))>>)))))>>>_._
    )@@ (@@*)@@.  (6,   6) / ^  \b)//))))))>>)))>>   ~~-.
 ( @jgs@@. @@@.*@_ ~^~^~, /\  ^  \b/)>>))))>>      _.     `,
  ((@@ @@@*.(@@ .   \^^^/' (  ^   \b)))>>        .'         `,
   ((@@).*@@ )@ )    `-'   ((   ^  ~)_          /             `,
     (@@. (@@ ).           (((   ^    `\\        |               `.
       (*.@*              / ((((        \\        \      .         `.
                         /   (((((  \\    \\    _.-~\     Y,          \\
                        /   / (((((( \\    \\.-~   _.`" _.-~`,        ;
                       /   /   `(((((()    )    (((((~      `,      ;
                     _/  _/      `"""/   /'                  ;     ;
                 _.-~_.-~           /  /'                _.-~   _.'
               ((((~~              / /'              _.-~ __.--~
                                  ((((          __.-~ _.-~
                                              <.~~~.~'
'''
profImg = '''
````````````````````````````````````````````````````````````````````````````````````````````````````
``````````````````````````````````````````hyyoo////::://///++ossy```````````````````````````````````
``````````````````````````````````````hyso++++//:::::::::::::/++++oshhh`````````````````````````````
```````````````````````````````````hys+////::-......--::///////+++oooyhhh```````````````````````````
`````````````````````````````````dyo+/::::-..`.````..----::://++++oossyhhhh`````````````````````````
```````````````````````````````hhs++////:........```..-------::::/+oossyyhhhh```````````````````````
```````````````````````````````hso////:-................---------:://+oooooyhhh`````````````````````
``````````````````````````````hyy+++//::----------........-------:::::///+++yhh`````````````````````
``````````````````````````````hhy+++++/::::------.........------------/:::://yhh````````````````````
``````````````````````````````hyooso+++//::------.........---------:--::---:/shhh```````````````````
``````````````````````````````yssyysoo++/:::------.........--------:---:----:shhh```````````````````
``````````````````````````````y+oyyyooo+/:::::---...`......--------------.---ohhh```````````````````
``````````````````````````````s/syyyso++/::::-:--..........------:::::---.--:ohhh```````````````````
``````````````````````````````s+syyyoo++/::------.........-------::::::--.--/shhh```````````````````
``````````````````````````````sosyyysoo+/::-------.--......-------:::::--..-/yhhh```````````````````
``````````````````````````````yssyyyoo++//:---------........-------::::--.--+yhhh```````````````````
``````````````````````````````hssyhyo+ooo++/:--------.--::///:/:--:::/:-.:::shhhh```````````````````
``````````````````````````````hhyhdhhhhhhhhyo++:::::/+oosyyso++++++++oooso/:+yhhh```````````````````
``````````````````````````````hdNmdhhhyhhmmmmdddssyhsssyyymhdyysodNNNNdh+--:s+hhhh``````````````````
``````````````````````````````myhhyyyhhssyysyhdd:--h+::///oso+oooyssso+/-:--//hhhh``````````````````
``````````````````````````````hyhdsoo+++////osds:-./y..-::----://o///////s--:+hhhh``````````````````
``````````````````````````````hhmdyo/:::////oyso:---//-.....--:/+::///+:-+/-:hhhh```````````````````
``````````````````````````````hhmmyso+////++oss+:--::-//:-----:---:///+:--:-shhh````````````````````
```````````````````````````````hhhyys+/:-::+sss/:--:--::-.....----:/:++:-.-+hhhh````````````````````
````````````````````````````````hyyhyo/::/+syhy+/::/oo/::/:...---////+/-.:shhhh`````````````````````
````````````````````````````````hhhhhso+ooooyhmdhyo+:::..-:///:-:/::/o+/ohhhh```````````````````````
`````````````````````````````````hhhhyss/:://+osso+-----....-/o+/:://osyhhh`````````````````````````
``````````````````````````````````hhyyyhsosoooososs+++:/::/:--://:://o/ohhh`````````````````````````
```````````````````````````````````hyyyhyhhddhhyyyssoossso+//-//////+o/ohhh`````````````````````````
````````````````````````````````````hyyhhsssso/::::----::--:-//++///o///dhhl````````````````````````
`````````````````````````````````````hyyhyssosso/++//::-----////://o+//:hNNq````````````````````````
``````````````````````````````````````hyyyyo+////:--------.-/:::+os+:+-//NNq````````````````````````
``````````````````````````````````````dmhyyo+++/:::::------://+sys/:/:/::/hhh```````````````````````
````````````````````````````````````hhmMNdhhsooo++++////:/+oyhho/://:/:::shhhhq`````````````````````
``````````````````````````````````mmmdNMMNmdhhhhhhhhhhhyhhddhs+///://::/ohhhhhhdq```````````````````
``````````````````````````````NNMMMNhdNNMMNmdhhhdmNmmmddhyyso++/://:///+hhhhhhhddddq````````````````
`````````````````````````NNMMMMMMMMhyhdmMMMNmdhhddhhhhyssooo+:/++//////hhhhhhhhhhdhdhddd````````````
`````````````````NNMMMMMMMMMMMMMMMmssyhhMMMNNmdhyyysssssso+:/oo+/::///yhhhhhhhhhhdhhhhhddddm````````
`````````````NNMNNNNNNNNNNNMMMMMMMsoossyMMMMNNNmdhssyyso//+ooo/:/://:ohhhhhhhhhhhdhhhhhhhddddd``````
``````````NNNNNNNNNNNNNNNNNNNMNNMmymNNmsmMMMNNNNNdhy+::/oooo+/::/:/:shhhhhhhhhhhhhhhhhhhhhhhddddd```
````````NNNNNNNNNNNNNNNNNNNNNNNNMmoyNMNshhmMNNmhyydNm//o+++//:::/:/+dhhhhhhhhhhhhhhhhhhhhhhhhhdddd``
``````NNNNNNNmmNmNmNNNNNNNNNNNNNNNy+dMNdhhsmNhyysydNNyo+++///:::/+/hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdd`
````NNNNNNNNmmmmmmmNmNNNNNNNNNNNNMNsommNNdhhhooooshmNs++o//:::/+//sdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
```NNNmNNNNmmmmmmmmmmNmmmNNNNNNNNMMmosdydNmdo+//++sdm+++/::::///:odhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
``NNNmmNNNNNNmmmmmmmmmmmmmNNNNNMMMMdhsyyshmyooooosydm++/::://::/:hdhhhhhhhhhhhdhhhdhhhhhhhhhhhhhhhhh
`NNNNmNNNNNNNmmmmmmmmmmmmmmmNNNNMMNyhhsoyyyooooo+++yd/-:::/:/::/oddhhhhhhhhhhhdhhhdhdhhhhhhhhhhhhhhh
'''
dragonAtt = '''
                                       \\/
                                       ^`'.
                                       ^   `'.
             (                         ^      `'.
           )  )        \\/              ^         `'.
         (   ) @       /^              ^            `'.
       )  )) @@  )    /  ^             ^               `'.
      ( ( ) )@@      /    ^            ^                  `'.
    ))  ( @@ @ )    /      ^           ^                     `'.
   ( ( @@@@@(@     /       |\\_/|,      ^                        `'.
  )  )@@@(@@@     /      _/~/~/~|C     ^                           `'.
((@@@(@@@@@(     /     _(@)~(@)~/\\C    ^                              `'.
  ))@@@(@@)@@   /     /~/~/~/~/`\\~`C   ^             __.__               `'.
   )@@@@(@@)@@@(     (o~/~o)^,) \\~ \\C  ^          .' -_'-'"...             `.
    ( (@@@)@@@(@@@@@@_~^~^~,-/\\~ \\~ \\C/^        /`-~^,-~-`_~-^`;_           `.
      @ )@@@(@@@@@@@   \\^^^/  (`^\\.~^ C^.,  /~^~^~^/_^-_`~-`~-~^\\- /`'-./`'-. ;
       (@ (@@@@(@@      `''  (( ~  .` .,~^~^-`-^~`/'^`-~ _`~-`_^-~\\/         ^^
           @jgs@             (((` ~ .-~-\\ ~`-_~`-/_-`~ `- ~-_- `~`;
          /                 /~((((` . ~-~\\` `  ~ |:`-_-~_~`  ~ _`-`;
         /                 /~-((((((`.\\-~-\\ ~`-`~^\/- ^_-~ ~` -_~-_`~`;
        /             /-~-/(((((((`\~-~\\~`^-`~`\\ -~`~/\\-^ -_~-_`~-`;
       /                 /~-~/  `((((((|-~-|((`.-~.`Y`_,~`/\\ `,- ~-_`~-`;
      /              ___/-~-/     `""""|~-~|"''    /~-^ .'    `:~`-_`~-~`;
     /         _____/  /~-~/           |-~-|      /-~-~.`      `:~^`-_`^-:
    /    _____/        ((((            ((((      (((((`           `:~^-_~-`;
    \\___/                                                          `:_^-~`;
                                                                    `:~-^`:
                                                                  ,`~-~`,`
                                                                 ,"`~.,'
                                                               ,"-`,"`
                                                             ,"_`,"
                                                            ,","`
                                                         ;~-~_~~;
                                                          '. ~.'
'''

ShumanPM = '''
            ____
      _,.-'`_ o `;__,
       _.-'` '---'  '
                    ____
                 .'`_ o `;__,
       .       .'.'` '---'  '
       .`-...-'.'
        `-...-'
                        _,.--.
    --..,_           .'`__ o  `;__,
       `'.'.       .'.'`  '---'`  ' 
          '.`-...-'.'
            `-...-'

    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
'''
ShumanLE = '''
 _                         
| |                        
| | __ _ ___  ___ _ __ ___ 
| |/ _` / __|/ _ \\ '__/ __|
| | (_| \\__ \\  __/ |  \\__ \\
|_|\\__,_|___/\\___|_|  |___/
'''
ShumanFB = '''
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'''
ShumanOip = '''

                        _    ,-,    _
                 ,--, /: :\\/': :`\\/: :\\
                |`;  ' `,'   `.;    `: |
                |    |     |  '  |     |.
                | :  |     | pb  |     ||
                | :. |  :  |  :  |  :  | \\
                 \\__/: :.. : :.. | :.. |  )
                      `---',\\___/,\\___/ /'
                           `==._ .. . /'
                                `-::-'
'''


control = controller(0,0,title,choose,0)
Player = control.PlayerClass()
control.startWorld()
input("\n\nHit enter to exit the game")
