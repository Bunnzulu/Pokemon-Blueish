import pygame
from pygame.math import Vector2
from Pokemon import Pokemon
pygame.init()

Item_Sell_prices = {"Poke Ball":100,"Antidote":50,"Parlyz Heal":100,"Burn Heal":125,"Potion":150,"Rare Candy":2400,"Escape Rope":275,"Awakening":100,"Map":0,"HP UP":4900,"Protein":4900,"Iron":4900,"Carbos":4900,"Calcium":4900,"Nugget":5000,"Super Potion":350,"Ice Heal":125,"Max Potion":1250,"Super Repel":250,"Revive":750,"TM08":2000,"TM34":1000,"TM12":500,"TM01":1500,"TM04":500,"TM11":1000,"TM45":1000,"TM19":1500,"TM28":1000,"TM44":1000,"TM24":1000,"TM23":2500,"TM15":2500,"TM50":1000,"TM32":500,"TM33":500,"TM02":1000,"TM07":1000,"TM37":1000,"TM05":1500,"TM09":1500,"TM17":1500,
"Full Restore":1500,"X Special":175,"X Attack":250,"X Defense":275,"X Speed":175,"X Accuracy":475,"Dire Hit":325,"Guard Spec":350,"Great Ball":300,"TM18":1000,"Poke Doll":500,"Fire Stone":1050,"Thunderstone":1050,"Water Stone":1050,"Leaf Stone":1050,"Fresh Water":100,"Soda Pop":150,"Lemonade":175,"TM13":2000,"TM48":2000,"TM49":2000,"TM21":2500,"TM10":2000,"Max Revive":2000,"Max Elixir":2250,"Ultra Ball":600,"Full Heal":300,"TM40":2000,"Max Repel":350,"TM03":1000,"TM26":2000,"TM31":1000,"TM46":2000,"TM41":1000,"TM39":1000,"TM35":2000,"TM14":2500,"TM22":2500,"TM38":2500,"TM27":2500,"TM43":2500,
"TM47":1500,"TM25":2500,"TM36":1000}
Key_Items = ("Map","Helix Fossil","Dome Fossil","S.S.TICKET","Old Rod","Itemfinder","Bike Voucher","HM01","HM02","HM03","HM04","HM05","Bike","Coin Case","Gold Teeth","Card Key","Good Rod","Super Rod","EXP All")


class Player(pygame.sprite.Sprite):
    def __init__(self,group):
        super().__init__(group)
        self.Scale = 1/7
        self.Idle_Down = pygame.image.load('Player_Sprites/Red_Idle_down.png').convert_alpha()
        self.Idle_Down = pygame.transform.rotozoom(self.Idle_Down,360,self.Scale)
        self.Idle_Up = pygame.image.load('Player_Sprites\Red_Idle_Up.png').convert_alpha()
        self.Idle_Up = pygame.transform.rotozoom(self.Idle_Up,360,self.Scale)
        self.Idle_Left = pygame.image.load('Player_Sprites\Red_Idle_Left.png').convert_alpha()
        self.Idle_Right = pygame.transform.flip(self.Idle_Left,True,False)

        self.Bike_Idle_Down = pygame.image.load('Player_Sprites\RedBikeDownIdle.png').convert_alpha()
        self.Bike_Idle_Down = pygame.transform.rotozoom(self.Bike_Idle_Down,360,self.Scale)
        self.Bike_Idle_Up = pygame.image.load('Player_Sprites\RedBikeUpIdle.png').convert_alpha()
        self.Bike_Idle_Up = pygame.transform.rotozoom(self.Bike_Idle_Up,360,self.Scale)
        self.Bike_Idle_Right = pygame.image.load('Player_Sprites\RedBikeRightIdle.png').convert_alpha()
        self.Bike_Idle_Right = pygame.transform.rotozoom(self.Bike_Idle_Right,360,self.Scale)
        self.Bike_Idle_Left = pygame.image.load('Player_Sprites\RedBikeLeftIdle.png').convert_alpha()
        self.Bike_Idle_Left = pygame.transform.rotozoom(self.Bike_Idle_Left,360,self.Scale)

        self.Swim_Idle_Down = pygame.image.load('Player_Sprites\RedSwimIdleDown.png').convert_alpha()
        self.Swim_Idle_Down = pygame.transform.rotozoom(self.Swim_Idle_Down,360,self.Scale)
        self.Swim_Idle_Up = pygame.image.load('Player_Sprites\RedSwimIdleUp.png').convert_alpha()
        self.Swim_Idle_Up = pygame.transform.rotozoom(self.Swim_Idle_Up,360,self.Scale)
        self.Swim_Idle_Right = pygame.image.load('Player_Sprites\RedSwimIdleRight.png').convert_alpha()
        self.Swim_Idle_Right = pygame.transform.rotozoom(self.Swim_Idle_Right,360,self.Scale)
        self.Swim_Idle_Left = pygame.image.load('Player_Sprites\RedSwimIdleLeft.png').convert_alpha()
        self.Swim_Idle_Left = pygame.transform.rotozoom(self.Swim_Idle_Left,360,self.Scale)
        
        self.Fishing_Down = pygame.image.load('Player_Sprites\RedFishingDown.png').convert_alpha()
        self.Fishing_Down = pygame.transform.rotozoom(self.Fishing_Down,360,self.Scale)
        self.Fishing_Up = pygame.image.load('Player_Sprites\RedFishingUp.png').convert_alpha()
        self.Fishing_Up = pygame.transform.rotozoom(self.Fishing_Up,360,self.Scale)
        self.Fishing_Right = pygame.image.load('Player_Sprites\RedFishingRight.png').convert_alpha()
        self.Fishing_Right = pygame.transform.rotozoom(self.Fishing_Right,360,self.Scale)
        self.Fishing_Left = pygame.image.load('Player_Sprites\RedFishingLeft.png').convert_alpha()
        self.Fishing_Left = pygame.transform.rotozoom(self.Fishing_Left,360,self.Scale)
        self.Fishing_pos =self.Fishing_Down

        self.Down1 = pygame.image.load('Player_Sprites\RedDown1.png').convert_alpha()
        self.Down2 = pygame.image.load('Player_Sprites\RedDown2.png').convert_alpha()
        self.DownIndex = 0
        self.Down_sprites = [self.Down1,self.Down2]
        self.Down_sprites = [pygame.transform.rotozoom(image,360,self.Scale) for image in self.Down_sprites]

        self.Bike_Down1 = pygame.image.load('Player_Sprites\RedBikeDown1.png').convert_alpha()
        self.Bike_Down2 = pygame.image.load('Player_Sprites\RedBikeDown2.png').convert_alpha()
        self.Bike_DownIndex = 0
        self.Bike_Down_sprites = [self.Bike_Down1,self.Bike_Down2]
        self.Bike_Down_sprites = [pygame.transform.rotozoom(image,360,self.Scale) for image in self.Bike_Down_sprites]

        self.Swim_Down1 = pygame.image.load('Player_Sprites\RedSwimDown1.png').convert_alpha()
        self.Swim_Down2 = pygame.image.load('Player_Sprites\RedSwimDown2.png').convert_alpha()
        self.Swim_DownIndex = 0
        self.Swim_Down_sprites = [self.Swim_Down1,self.Swim_Down2]
        self.Swim_Down_sprites = [pygame.transform.rotozoom(image,360,self.Scale) for image in self.Swim_Down_sprites]

        self.Up1 = pygame.image.load('Player_Sprites\RedUp1.png').convert_alpha()
        self.Up2  = pygame.image.load('Player_Sprites\RedUp2.png').convert_alpha()
        self.UpIndex = 0
        self.Up_sprites = [self.Up1,self.Up2]
        self.Up_sprites = [pygame.transform.rotozoom(image,360,self.Scale) for image in self.Up_sprites]

        self.Bike_Up1 = pygame.image.load('Player_Sprites\RedBikeUp1.png').convert_alpha()
        self.Bike_Up2  = pygame.image.load('Player_Sprites\RedBikeUp2.png').convert_alpha()
        self.Bike_UpIndex = 0
        self.Bike_Up_sprites = [self.Bike_Up1,self.Bike_Up2]
        self.Bike_Up_sprites = [pygame.transform.rotozoom(image,360,self.Scale) for image in self.Bike_Up_sprites]

        self.Swim_Up1 = pygame.image.load('Player_Sprites\RedSwimUp1.png').convert_alpha()
        self.Swim_Up2  = pygame.image.load('Player_Sprites\RedSwimUp2.png').convert_alpha()
        self.Swim_UpIndex = 0
        self.Swim_Up_sprites = [self.Swim_Up1,self.Swim_Up2]
        self.Swim_Up_sprites = [pygame.transform.rotozoom(image,360,self.Scale) for image in self.Swim_Up_sprites]

        self.Left1 = pygame.image.load('Player_Sprites\RedLeft1.png').convert_alpha()
        self.Left_sprites = [self.Idle_Left,self.Left1]
        self.Left_sprites = [pygame.transform.rotozoom(image,360,self.Scale) for image in self.Left_sprites]
        self.Idle_Left = self.Left_sprites[0]
        self.LeftIndex=0

        self.Bike_Left1 = pygame.image.load('Player_Sprites\RedBikeLeft1.png').convert_alpha()
        self.Bike_Left1 = pygame.transform.rotozoom(self.Bike_Left1,360,self.Scale)
        self.Bike_Left_sprites = [self.Bike_Idle_Left,self.Bike_Left1]
        self.Bike_LeftIndex=0

        self.Swim_Left1 = pygame.image.load('Player_Sprites\RedSwimLeft1.png').convert_alpha()
        self.Swim_Left1 = pygame.transform.rotozoom(self.Swim_Left1,360,self.Scale)
        self.Swim_Left_sprites = [self.Swim_Idle_Left,self.Swim_Left1]
        self.Swim_LeftIndex=0

        self.RightIndex = 0
        self.Right_Sprites = [pygame.transform.flip(image,True,False) for image in self.Left_sprites]
        self.Idle_Right = self.Right_Sprites[0]

        self.Bike_RightIndex = 0
        self.Bike_Right1 = pygame.image.load('Player_Sprites\RedBikeRight1.png').convert_alpha()
        self.Bike_Right1 = pygame.transform.rotozoom(self.Bike_Right1,360,self.Scale)
        self.Bike_Right_Sprites = [self.Bike_Idle_Right,self.Bike_Right1]
        self.Bike_Idle_Right = self.Bike_Right_Sprites[0]

        self.Swim_RightIndex = 0
        self.Swim_Right1 = pygame.image.load('Player_Sprites\RedSwimIdleRight.png').convert_alpha()
        self.Swim_Right1 = pygame.transform.rotozoom(self.Swim_Right1,360,self.Scale)
        self.Swim_Right_Sprites = [self.Swim_Idle_Right,self.Swim_Right1]
    
        self.image = self.Idle_Down
        self.rect = self.image.get_rect(center = (9*32,1524*32))
        self.Up,self.Down,self.Left,self.Right = False,False,False,False
        self.Moveable = True
        self.Bike = False
        self.Surf = False
        self.BikeLocations = ["OverWorld","Mt.Moon","Mt.Moon2","Mt.Moon3","Rock TunnelF1","Rock TunnelF2","R16GuardTower"]
        self.Fishing = False
        self.FishCaught = False
        self.Fishing_Rod = ""
        self.Menu = False
        self.Bag = []
        self.Pokemon = []
        self.PC_Items = [[["Potion",1]]]
        self.ItemFinderPing = False
        self.ItemFound = False
        self.ItemFinderUsed = False
        self.ItemFinderArea = pygame.Rect(self.rect.center,(3000,3000))

        self.Money = 3000
        self.Coins = 0
        self.Fly = False
        self.Badges = {"Boulder":False,"Cascade":False,"Thunder":False,"Rainbow":False,"Soul":False,"Marsh":False,"Volcano":False,"Earth":False}
        self.PCBoxes = [[]]
        self.PCBoxesIndex = 0
        self.PCItemsIndex = 0
        self.LoyaltyLevel = 10
        self.Search = False
        self.Direction = Vector2(0,0)
        self.ShowDex = False
        self.WalkSpeed = 2
        self.BikeSpeed = self.WalkSpeed * 2
    
    def Input(self):
        keys = pygame.key.get_pressed()
        if self.Moveable:
            self.ItemFinderArea = pygame.Rect(self.rect.center,(400,400))
            self.ItemFinderArea.center = self.rect.center
            if keys[pygame.K_DOWN]:
                if not self.Bike:self.Direction.y = self.WalkSpeed
                else:self.Direction.y = self.BikeSpeed
                self.Direction.x = 0
            elif keys[pygame.K_UP]:
                if not self.Bike:self.Direction.y = -(self.WalkSpeed)
                else:self.Direction.y = -(self.BikeSpeed)
                self.Direction.x = 0
            elif keys[pygame.K_RIGHT]:
                if not self.Bike:self.Direction.x = self.WalkSpeed
                else:self.Direction.x = self.BikeSpeed
                self.Direction.y = 0
            elif keys[pygame.K_LEFT]:
                if not self.Bike:self.Direction.x = -(self.WalkSpeed)
                else:self.Direction.x = -(self.BikeSpeed)
                self.Direction.y = 0
            elif keys[pygame.K_RETURN] and not self.IsWalking():
                self.Menu = True
                self.ShowDex = False
            elif keys[pygame.K_p]:
                self.ShowDex = True
                self.Menu = False
            else: self.Direction = Vector2(0,0)
        else: self.Direction = Vector2(0,0)

    def Animations(self):
        if not self.Bike and not self.Surf:
            if self.Direction.y >= 2:
                self.Down = True
                self.Right,self.Up,self.Left = [False,False,False]
                self.image = self.Down_sprites[int(self.DownIndex)]
                self.DownIndex += 0.2
                if self.DownIndex >= len(self.Down_sprites): self.DownIndex = 0
            elif self.Direction.y <= -2:
                self.Up = True
                self.Down,self.Right,self.Left = [False,False,False]
                self.image = self.Up_sprites[int(self.UpIndex)]
                self.UpIndex += 0.2
                if self.UpIndex >= len(self.Up_sprites): self.UpIndex = 0
            elif self.Direction.x >= 2:
                self.Right = True
                self.Down,self.Up,self.Left = [False,False,False]
                self.image = self.Right_Sprites[int(self.RightIndex)]
                self.RightIndex += 0.2
                if self.RightIndex >= len(self.Right_Sprites): self.RightIndex = 0
            elif self.Direction.x <= -2:
                self.Left = True
                self.Down,self.Up,self.Right = [False,False,False]
                self.image = self.Left_sprites[int(self.LeftIndex)]
                self.LeftIndex += 0.2
                if self.LeftIndex >= len(self.Left_sprites): self.LeftIndex = 0
            else:
                if self.Down:self.image = self.Idle_Down
                elif self.Up:self.image = self.Idle_Up
                elif self.Right:self.image = self.Idle_Right
                elif self.Left:self.image = self.Idle_Left
                self.DownIndex,self.UpIndex,self.RightIndex,self.LeftIndex = 0,0,0,0       
        elif self.Bike:
            if self.Direction.y >= 2:
                self.Down = True
                self.Right,self.Up,self.Left = [False,False,False]
                self.image = self.Bike_Down_sprites[int(self.Bike_DownIndex)]
                self.Bike_DownIndex += 0.2
                if self.Bike_DownIndex >= len(self.Bike_Down_sprites): self.Bike_DownIndex = 0
            elif self.Direction.y <= -2:
                self.Up = True
                self.Down,self.Right,self.Left = [False,False,False]
                self.image = self.Bike_Up_sprites[int(self.Bike_UpIndex)]
                self.Bike_UpIndex += 0.2
                if self.Bike_UpIndex >= len(self.Bike_Up_sprites): self.Bike_UpIndex = 0
            elif self.Direction.x >= 2:
                self.Right = True
                self.Down,self.Up,self.Left = [False,False,False]
                self.image = self.Bike_Right_Sprites[int(self.Bike_RightIndex)]
                self.Bike_RightIndex += 0.2
                if self.Bike_RightIndex >= len(self.Bike_Right_Sprites): self.Bike_RightIndex = 0
            elif self.Direction.x <= -2:
                self.Left = True
                self.Down,self.Up,self.Right = [False,False,False]
                self.image = self.Bike_Left_sprites[int(self.Bike_LeftIndex)]
                self.Bike_LeftIndex += 0.2
                if self.Bike_LeftIndex >= len(self.Bike_Left_sprites): self.Bike_LeftIndex = 0
            else:
                if self.Down:self.image = self.Bike_Idle_Down
                elif self.Up:self.image = self.Bike_Idle_Up
                elif self.Right:self.image = self.Bike_Idle_Right
                elif self.Left:self.image = self.Bike_Idle_Left
                self.Bike_DownIndex,self.Bike_UpIndex,self.Bike_RightIndex,self.Bike_LeftIndex = 0,0,0,0
        else:
            if self.Direction.y >= 2:
                self.Down = True
                self.Right,self.Up,self.Left = [False,False,False]
                self.image = self.Swim_Down_sprites[int(self.Swim_DownIndex)]
                self.Swim_DownIndex += 0.2
                if int(self.Swim_DownIndex) >= len(self.Swim_Down_sprites): self.Swim_DownIndex = 0
            elif self.Direction.y <= -2:
                self.Up = True
                self.Down,self.Right,self.Left = [False,False,False]
                self.image = self.Swim_Up_sprites[int(self.Swim_UpIndex)]
                self.Swim_UpIndex += 0.2
                if int(self.Swim_UpIndex) >= len(self.Swim_Up_sprites): self.Swim_UpIndex = 0
            elif self.Direction.x >= 2:
                self.Right = True
                self.Down,self.Up,self.Left = [False,False,False]
                self.image = self.Swim_Right_Sprites[int(self.Swim_RightIndex)]
                self.Swim_RightIndex += 0.2
                if self.Swim_RightIndex >= len(self.Swim_Right_Sprites): self.Swim_RightIndex = 0
            elif self.Direction.x <= -2:
                self.Left = True
                self.Down,self.Up,self.Right = [False,False,False]
                self.image = self.Swim_Left_sprites[int(self.Swim_LeftIndex)]
                self.Swim_LeftIndex += 0.2
                if self.Swim_LeftIndex >= len(self.Swim_Left_sprites): self.Swim_LeftIndex = 0
            else:
                if self.Down:self.image = self.Swim_Idle_Down
                elif self.Up:self.image = self.Swim_Idle_Up
                elif self.Right:self.image = self.Swim_Idle_Right
                elif self.Left:self.image = self.Swim_Idle_Left
                self.Swim_DownIndex,self.Swim_UpIndex,self.Swim_RightIndex,self.Swim_LeftIndex = 0,0,0,0

    def SetLoyaltyLevel(self):
        if self.Get_BadgeInfo() == 1:self.LoyaltyLevel = 20
        if self.Get_BadgeInfo("Cascade",True):self.LoyaltyLevel = 30
        if self.Get_BadgeInfo("Rainbow",True):self.LoyaltyLevel = 50
        if self.Get_BadgeInfo("Marsh",True):self.LoyaltyLevel = 70
        if self.Get_BadgeInfo("Earth",True):self.LoyaltyLevel = 100

    def Horizontal_Collison(self,Tiles:list[pygame.Rect]):
        for rect in Tiles:
            if rect.colliderect(self.rect):
                if not self.Bike:
                    if self.Direction.x < 0 and self.rect.right -(self.WalkSpeed)!= rect.left and self.rect.bottom - (self.WalkSpeed)!=  rect.top and self.rect.top + (self.WalkSpeed)!= rect.bottom:
                        self.rect.left = rect.right
                    if self.Direction.x > 0 and self.rect.left +(self.WalkSpeed)!= rect.right and self.rect.bottom - (self.WalkSpeed)!=  rect.top and self.rect.top + (self.WalkSpeed)!= rect.bottom:
                        self.rect.right = rect.left
                else:
                    if self.Direction.x < 0 and self.rect.right -(self.BikeSpeed)!= rect.left and self.rect.bottom - (self.BikeSpeed)!=  rect.top and self.rect.top + (self.BikeSpeed)!= rect.bottom:
                        self.rect.left = rect.right
                    if self.Direction.x > 0 and self.rect.left +(self.BikeSpeed)!= rect.right and self.rect.bottom - (self.BikeSpeed)!=  rect.top and self.rect.top + (self.BikeSpeed)!= rect.bottom:
                        self.rect.right = rect.left
    
    def IsWalking(self) -> bool:
        return self.Direction != Vector2(0,0)
    
    def Add_Bag(self,ItemName:str,ItemAmount:int):
        In_bag = False
        overflow = ItemAmount
        overflowed = False
        if len(self.Bag) >= 20: self.Add_PC_Items(ItemName,ItemAmount)
        elif len(self.Bag) < 20:
            for Items in self.Bag:
                if Items[0] == ItemName and Items[1] < 99:
                    Items[1] += ItemAmount
                    if Items[1] > 99:
                        overflow = Items[1] - 99
                        Items[1] = 99
                        overflowed = True
                    In_bag = True
            if (not In_bag or overflowed): self.Bag.append([ItemName,overflow])

    def Purchase(self,ItemName:str,ItemAmount:int,Itemcost:int):
        if self.Money >= Itemcost * ItemAmount:
            self.Money -= Itemcost * ItemAmount
            self.Add_Bag(ItemName,ItemAmount)
    
    def Purchase_from_PrizeBooth(self,ItemName,Itemcost:int,Type:str):
        if self.Coins >= Itemcost:
            self.Coins -= Itemcost
            if Type == "Item":self.Add_Bag(ItemName,1)
            else:self.Add_Pokemon(ItemName)
    
    def Sell(self,ItemName:str,ItemAmount:int):
        self.Money += Item_Sell_prices[ItemName] * ItemAmount
        self.Remove_Bag(ItemName,ItemAmount,False)

    def Get_PriceForBag(self):
        items = [[itemname[0],Item_Sell_prices.setdefault(itemname[0],0),itemname[1]] for itemname in self.Bag]
        return items

    def Get_BadgeInfo(self,Badge:str = "",Name:bool = False):
        N = 0
        if Name: return self.Badges[Badge]
        else:
            for i in self.Badges.items():
                if i[1]: N += 1
            return N

    def GetRemainingPokemon(self):
        N = 0
        for poke in self.Pokemon:
            if poke.HP > 0:
                N += 1
        return N

    def PokemonHasMove(self,Move):
        for poke in self.Pokemon:
            if Move in poke.Moves: return True
        return False

    def GetPokemon(self,Pokemon:str):
        for poke in self.Pokemon:
            if poke.Name == Pokemon:return True
        return False

    def TradingPokemon(self,HisPokemon,YourPokemon,NickName):
        UP = Pokemon
        OP = Pokemon
        for N,i in enumerate(self.Pokemon):
            if i.Name == YourPokemon:
                UP = i
                self.Pokemon.pop(N)
                break
        OP = Pokemon(HisPokemon,UP.Level,["Tackle"],"Trainer",NickName)
        OP.Moves = OP.Last4Moves(Level=UP.Level)
        OP.Move_Update()
        self.Pokemon.append(OP)

    def Remove_Bag(self,ItemName:str,ItemAmount:int,Into_PC:bool=False):
        self.Bag_Updates()
        if len(self.Bag):
            for i,Items in enumerate(self.Bag):
                if Items[0] == ItemName and Items[1] >= ItemAmount:
                    self.Bag[i][1] -= ItemAmount
                    if self.Bag[i][1] <= 0: self.Bag.remove(self.Bag[i])
                    if Into_PC:
                        self.Add_PC_Items(ItemName,ItemAmount)
        self.Bag_Updates()

    def Group_Collison(self,Rects):
        for rect in Rects:
            if self.rect.colliderect(rect): return True
        return False

    def Add_Pokemon(self,Pokemon):
        if len(self.Pokemon) < 6:
            self.Pokemon.append(Pokemon)
        else:
            self.Add_PCPokemon(Pokemon)

    def Add_PCPokemon(self,Pokemon):
        for count,i in enumerate(self.PCBoxes): 
            if len(i) < 20:
                self.PCBoxes[count].append(Pokemon)
            else:
                if count + 1 == len(self.PC_Items):
                    self.PCBoxes.append([Pokemon])

    def Check_Moves(self,Move:str):
        for poke in self.Pokemon:
            if Move in poke.Moves:return True
        return False

    def Check_Statuses(self,Status:str):
        for poke in self.Pokemon:
            if poke.Status == Status:return True
        return False

    def Add_PC_Items(self,ItemName:str,ItemAmount:int):
        itemmatch = False
        overflow = 0
        for count,i in enumerate(self.PC_Items):
            if len(i) > 0:
                for Items in i:
                    if Items[0] == ItemName and Items[1] < 99:
                        Items[1] += ItemAmount
                        if Items[1] > 99:
                            overflow = Items[1] - 99
                            Items[1] = 99
                            itemmatch = True
                            break
                if len(i) < 20:
                    if itemmatch:self.PC_Items[count].append([ItemName,overflow])
                    else:self.PC_Items[count].append([ItemName,ItemAmount])
                else:
                    if count + 1 == len(self.PC_Items):
                        if itemmatch:self.PC_Items.append([[ItemName,overflow]])
                        else:self.PC_Items.append([[ItemName,ItemAmount]])
            else:
                self.PC_Items[count].append([ItemName,ItemAmount])

    def PC_Items_Update(self):
        pc_Items = []
        Slot = []
        for i in self.PC_Items:
            for item in i:
                if item[1] > 0:Slot.append(item)
            pc_Items.append(Slot)
        self.PC_Items = pc_Items
    
    def Bag_Updates(self):
        Bag_items = [item for item in self.Bag if item[1] > 0]
        self.Bag = Bag_items

    def Remove_PC_Item(self,ItemName:str,ItemAmount:int,Into_Bag:bool):
        self.PC_Items_Update()
        if len(self.PC_Items):
            for i,Items in enumerate(self.PC_Items):
                if Items[i][0] == ItemName and Items[i][1] >= ItemAmount:
                    Items[i][1] -= ItemAmount
                    if Into_Bag:
                        self.Add_Bag(ItemName,ItemAmount)
            self.PC_Items_Update()

    def Full_Team_Heal(self):
        for i in range(len(self.Pokemon)):
            self.Pokemon[i].Heal(self.Pokemon[i].MAXHP -self.Pokemon[i].HP,True,True)

    def Vertical_Collison(self, Rects:list[pygame.Rect]):
        for rect in Rects:
            if rect.colliderect(self.rect):
                if not self.Bike:
                    if self.Direction.y < 0 and self.rect.bottom - (self.WalkSpeed)!=  rect.top and self.rect.right -(self.WalkSpeed)!= rect.left and self.rect.left +(self.WalkSpeed)!= rect.right:
                        self.rect.top = rect.bottom
                    if self.Direction.y > 0 and self.rect.top + (self.WalkSpeed)!= rect.bottom and self.rect.right -(self.WalkSpeed)!= rect.left and self.rect.left +(self.WalkSpeed)!= rect.right:
                        self.rect.bottom = rect.top
                else:
                    if self.Direction.y < 0 and self.rect.bottom - (self.BikeSpeed)!=  rect.top and self.rect.right -(self.BikeSpeed)!= rect.left and self.rect.left +(self.BikeSpeed)!= rect.right:
                        self.rect.top = rect.bottom
                    if self.Direction.y > 0 and self.rect.top + (self.BikeSpeed)!= rect.bottom and self.rect.right -(self.BikeSpeed)!= rect.left and self.rect.left +(self.BikeSpeed)!= rect.right:
                        self.rect.bottom = rect.top
    
    def update(self,Tiles):
        self.Input()
        self.Animations()
        self.Vertical_Collison(Tiles)
        self.Horizontal_Collison(Tiles)
        self.BikeSpeed = self.WalkSpeed * 2
        self.rect.x += self.Direction.x
        self.rect.y += self.Direction.y
