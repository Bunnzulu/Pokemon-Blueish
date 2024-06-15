import pygame
pygame.init()

class StageHandler:
    def __init__(self):
        self.Stage = "Start"
        self.OverworldLocation = "Pallet Town"
        self.Index = 0
        self.Title_Font = pygame.font.Font('Fonts\Pokemon Hollow.ttf',100)
        self.SubTitle_Font = pygame.font.Font('Fonts\Pokemon Solid.ttf',50)
        self.Game_Font2 = pygame.font.Font('Fonts\Pokemon Solid.ttf',30)
        self.Game_Font3 = pygame.font.SysFont("arial",25,False,False)
        self.Title = self.Title_Font.render('Pokemon Blue........',True,"Black")
        self.Title2 = self.Title_Font.render('......ish Edition',True,"Black")
        self.Game_font = pygame.font.Font(None,30)
        self.Screen = pygame.display.get_surface()
        self.Start_Next = self.Game_font.render("Press any button to Start",True,"Black")
        self.Start_Next_rect = self.Start_Next.get_rect(center = (self.Screen.get_width()//2,self.Screen.get_height()//2))
        self.Title_rect = self.Title.get_rect(center = (self.Screen.get_width()//2,100))
        self.Title2_rect = self.Title2.get_rect(center = (self.Title_rect.centerx,200))
        self.Dr_OakfullSprite = pygame.image.load('Trainer_imgs\Dr.Oak.png').convert_alpha()
        self.Nidorino_SS = pygame.image.load(r'Pokemon_imgs\Nidorino_Front.png').convert_alpha()
        self.Playerfullsprite = pygame.image.load('Trainer_imgs\Player_SS.png').convert_alpha()
        self.Playerfullsprite_rect = self.Playerfullsprite.get_rect(center = (self.Screen.get_width()//2,self.Screen.get_height()//2 - 50))
        self.Dr_OakfullSprite_rect = self.Dr_OakfullSprite.get_rect(center = (self.Screen.get_width()//2,self.Screen.get_height()//2 - 50))
        self.Nidorino_SS_rect = self.Nidorino_SS.get_rect(center = (830,self.Screen.get_height()//2 - 50))
        self.Rivalfullsprite = pygame.image.load('Trainer_imgs\Rival_SS.png').convert_alpha()
        self.Rivalbattlestance = pygame.image.load('Trainer_imgs\Rival_BattleStance.png').convert_alpha()
        self.RivalChampion = pygame.image.load('Trainer_imgs\Champion.png').convert_alpha()
        self.Rivalfullsprite_rect = self.Rivalfullsprite.get_rect(center = (self.Screen.get_width()//2,self.Screen.get_height()//2 - 50))
        self.TextBox = pygame.Rect(0,500,self.Screen.get_width(),300)
        self.TextBox_outline = pygame.Rect(0,500,self.Screen.get_width(),300)
        self.Next_Text = self.Game_font.render("Shift to go on",True,"Black")
        self.Next_Text_rect = self.Next_Text.get_rect(bottomright = (self.TextBox.midright[0],self.TextBox.midright[1] + 50))
        self.Playerinput = ''
        self.Rivalinput = ''
        self.NameInputBox = pygame.Rect(200,100,100,30)
        self.Playerinput_surf = self.Game_font.render(self.Playerinput,True,"Black")
        self.Playerinput_rect = self.Playerinput_surf.get_rect(center = self.NameInputBox.center)
        self.SS1= False
        self.SS2 = False
        self.prePlayerName_input = False
        self.PlayerName_input = False
        self.PlayerNameConfirm = False
        self.preRivalName_input = False
        self.RivalName_input = False
        self.RivalNameConfirm = False
        self.SSSendOff = False
        self.OakCutscene1 = False
        self.OakCutscene2 = False
        self.OakCutscene3 = False
        self.OakCutscene4 = False
        self.OakCutscene5 = False
        self.PokemonPicked = False
        self.RPokemonPick = False
        self.PickinPoke = False
        self.SPNickname = ''
        self.preFirstRivalBattle = False
        self.RivalBattle = False
        self.StarterNickname = False
        self.PostRivalBattle = False
        self.PlayerPoke = ''
        self.RivalPoke = ''
        self.PokeMartCutscene = False
        self.PokeMartCutscene1 = True
        self.PokeMartCutscene2 = False
        self.HasPokeballs = False
        self.OakPokeBallCutscene1 = False
        self.OakPokeBallCutscene2 = False
        self.OakPokeBallCutscene3 = False
        self.OakPokeBallCutscene4 = False
        self.OakPokeBallCutscene5 = False
        self.OptionalRivalFightDone = False
        self.OptionalRivalFight = False
        self.OptionalRivalFightCutscene = True
        self.OptionalRivalFightAftermath = False
        self.CCRivalFightDone = False
        self.CCRivalFight = False
        self.CCRivalFightCutscene = True
        self.CCRivalFightAftermath = False
        self.NBRocketEncounter = False
        self.NBRocketCutscene = True
        self.NBRocketFight = False
        self.NBRocketAftermath = False
        self.BillPokemonEncounter = True
        self.HelpBillPokemon = False
        self.BillEncounter = False
        self.BillSSTicket = False
        self.BillSSTicketAftermath = False
        self.SSTicketGot = False
        self.CCRocketFightDone = False
        self.FishingCutscene = False
        self.FishFight = False
        self.GuardDrinkGiven = False
        self.PFCSpeech = False
        self.PFCp1 = True
        self.PFCp2 = False
        self.SSTicketCheck = False
        self.SSRivalBattleDone = False
        self.SSRivalFightCutscene = True
        self.SSRivalFightAftermath = False
        self.SSRivalFight = False
        self.SSCaptainDone = False
        self.SSCaptainCutscene = True
        self.SSCaptainHMGet = False
        self.PlayerDeathMessage = False
        self.HiddenItemPickedup = False
        self.HMFlashGet = False
        self.ItemFinderGet = False
        self.BikeEvent = False
        self.HaveBike = False
        self.GirlGotWater = False
        self.GirlGotPop = False
        self.GirlGotLemons = False
        self.GCRocketEncounter = False
        self.GCRocketCutscene = True
        self.GCRocketFight = False
        self.GCRocketAftermath = False
        self.RBaseGiovanniEncounter = False
        self.RBaseGiovanniCutscene = True
        self.RBaseGiovanniFight = False
        self.RBaseGiovanniAftermath = False
        self.PokeTowerRivalFightDone = False
        self.PokeTowerRivalFight = False
        self.PokeTowerRivalFightCutscene = True
        self.PokeTowerRivalFightAftermath = False
        self.PokeTowerGhostEncounter = True
        self.PokeTowerGhostReveal = False
        self.PokeTowerGhostFight = False
        self.PokeTowerGhostFightAftermath = False
        self.PokeTowerGhost = False
        self.Mr_FujiTalk1 = False
        self.Mr_FujiSaved = False
        self.CESnorlaxAwake = False
        self.VCSnorlaxAwake = False
        self.CESnorlaxFight = False
        self.VCSnorlaxFight = False
        self.Fighting_DojoFightDone = False
        self.Fighting_DojoFight = False
        self.Fighting_DojoFightCutscene = True
        self.Fighting_DojoFightAftermath = False
        self.Fighting_DojoPokePick = False
        self.Fighting_DojoPokemon = ""
        self.Fighting_DojoPokePickDone = False
        self.SilCoRivalBattleDone = False
        self.SilCoRivalFightCutscene = True
        self.SilCoRivalFightAftermath = False
        self.SilCoRivalFight = False
        self.SilCoGioDone = False
        self.SilCoGioCutscene = True
        self.SilCoGioFightAftermath = False
        self.SilCoGioFight = False
        self.SilCoLapras = False
        self.SilCoLaprasTalk = True
        self.SilCoLaprasAftermath = False
        self.CopyCat = False
        self.CopyCatTalk = True
        self.CopyCatAftermath = False
        self.ExpALLGet = False
        self.FossilDescion = True
        self.FossilRevival = False
        self.PokeMansionSwitchON = False
        self.BPLRivalFightDone = False
        self.BPLRivalFight = False
        self.BPLRivalFightCutscene = True
        self.BPLRivalFightAftermath = False
        self.Moltres = False
        self.MoltresFight = False
        self.ChampionFight = False
        self.ChampionFightCutsceneP1 = True
        self.ChampionFightCutsceneP2 = False
        self.ChampionFightAftermath = False
        self.AfterChampionP1 = False
        self.AfterChampionP2 = False
        self.AfterChampionP3 = False
        self.AfterChampionP4 = False
        self.FameHallTalkP1 = False
        self.FameHallTalkP2 = False
        self.FameHallDisplay = False
        self.FameHallDisplay2 = False
        self.EndScreenTitle = self.Title_Font.render('The End',True,"Black")
        self.EndScreenStaffTitle = self.SubTitle_Font.render('Staff',True,"Black")
        self.EndScreenStaffTitle_rect = self.EndScreenStaffTitle.get_rect(center = (400,228))
        self.EndScreenStaff = self.Game_Font3.render('Me',True,"Black")
        self.EndScreenStaff_rect = self.EndScreenStaff.get_rect(center = (self.EndScreenStaffTitle_rect.centerx,self.EndScreenStaffTitle_rect.centery + 30))
        self.Credits = self.SubTitle_Font.render('Inspired by',True,"Black")
        self.Credits_rect = self.Credits.get_rect(center = (400,305))
        self.Credited = self.Game_Font3.render('Pokemon Blue',True,"Black")
        self.Credited_rect = self.Credited.get_rect(center = (self.Credits_rect.centerx,self.Credits_rect.centery + 50))
        self.KeepPlayingTitle = self.SubTitle_Font.render("Hope you enjoyed the Game",True,"Black")
        self.KeepPlayingTitle_rect = self.KeepPlayingTitle.get_rect(center = (400,410))
        self.ClickNext = self.Game_Font3.render('Close the game to keep playing',True,"Black")
        self.ClickNext_rect = self.ClickNext.get_rect(center = (self.KeepPlayingTitle_rect.centerx,self.KeepPlayingTitle_rect.centery + 50))
        self.Zapdos = False
        self.ZapdosFight = False
        self.Articuno = False
        self.ArticunoFight = False
        self.Mewtwo = False
        self.MewtwoFight = False
        self.OakinLab = False
        self.OakFightCutscene = True
        self.OakFightAftermath = False
        self.OakFight = False
        self.CFightDone = False
        self.CFightCutscene = True
        self.CFightAftermath = False
        self.CFight = False

    def Events(self):
        match self.Stage:
            case "Start":
                self.Screen.fill("cornsilk1")
                self.Screen.blit(self.Title,self.Title_rect)
                self.Screen.blit(self.Title2,self.Title2_rect)
                self.Screen.blit(self.Start_Next,self.Start_Next_rect)
            
            case "Dr.Oak talk":
                self.Screen.fill("cornsilk1")
                if not self.SS1:
                    self.Screen.blit(self.Dr_OakfullSprite,self.Dr_OakfullSprite_rect)
                    self.Dialouge('Oak : Hello there!','Welcome to the world of POKEMON! My name is OAK!','People call me the POKEMON PROF!')
                elif not self.SS2:
                    self.Screen.blit(self.Dr_OakfullSprite,self.Dr_OakfullSprite_rect)
                    if self.Dr_OakfullSprite_rect.x >= 100:
                        self.Dr_OakfullSprite_rect.x -= 5
                    else:
                        self.Screen.blit(self.Nidorino_SS,self.Nidorino_SS_rect)
                        if self.Nidorino_SS_rect.x >= 400:
                            self.Nidorino_SS_rect.x -= 10
                    self.Dialouge('Oak : This world is inhabited by creatures called POKEMON!','For some people, POKEMON are pets. Others use them for fights.','Myself...I study POKEMON as a profession.')
                elif not self.prePlayerName_input:
                    self.Screen.blit(self.Playerfullsprite,self.Playerfullsprite_rect)
                    self.Dialouge('Oak: First, what is your name?')
                elif not self.PlayerName_input:
                    self.Playerinput_surf = self.Game_font.render(self.Playerinput,True,"Black")
                    self.Screen.blit(self.Playerfullsprite,self.Playerfullsprite_rect)
                    self.Screen.blit(self.Playerinput_surf,self.Playerinput_rect)
                    pygame.draw.rect(self.Screen,"Black",self.NameInputBox,5)  
                    self.Playerinput_rect = self.Playerinput_surf.get_rect(center = self.NameInputBox.center)
                elif not self.PlayerNameConfirm:
                    self.Screen.blit(self.Playerfullsprite,self.Playerfullsprite_rect)
                    self.Dialouge(f"Thats right your name is {self.Playerinput}")
                elif not self.preRivalName_input:
                    self.Screen.blit(self.Rivalfullsprite,self.Rivalfullsprite_rect)
                    self.Dialouge("Oak : This is my grandson. He's been your rival since you were a baby....","Erm, what is his name again?")
                elif not self.RivalName_input:
                    self.Playerinput_surf = self.Game_font.render(self.Rivalinput,True,"Black")
                    self.Screen.blit(self.Rivalfullsprite,self.Rivalfullsprite_rect)
                    self.Screen.blit(self.Playerinput_surf,self.Playerinput_rect)
                    pygame.draw.rect(self.Screen,"Black",self.NameInputBox,5)
                    self.Playerinput_rect = self.Playerinput_surf.get_rect(center = self.NameInputBox.center)
                elif not self.RivalNameConfirm:
                    self.Screen.blit(self.Rivalfullsprite,self.Rivalfullsprite_rect)
                    self.Dialouge(f"Oak: That's right! I remember now! His name is {self.Rivalinput}!")
                elif not self.SSSendOff:
                    self.Screen.blit(self.Playerfullsprite,self.Playerfullsprite_rect)
                    self.Dialouge(f"Oak : {self.Playerinput}! Your very own POKEMON legend is about to unfold!","A world of dreams and adventures with POKEMON awaits! Let's go!")
                elif self.SSSendOff:
                    self.Stage = "SPlayerRoom"
            
            case "Oak Lab":
                if self.StarterNickname:
                    self.Screen.fill("White")
                    self.Playerinput_surf = self.Game_font.render(self.SPNickname,True,"Black")
                    self.Screen.blit(self.Playerinput_surf,self.Playerinput_rect)
                    pygame.draw.rect(self.Screen,"Black",self.NameInputBox,5)  
                    self.Playerinput_rect = self.Playerinput_surf.get_rect(center = self.NameInputBox.center)
                
            case "Poke Mart":
                if not self.PokeMartCutscene:
                    if self.PokeMartCutscene1: self.Dialouge("Hey! You came from PALLET TOWN?","You know PROF.OAK, right?")
                    elif self.PokeMartCutscene2: self.Dialouge("Clerk:His order came in. Will you take it to him?",f"{self.Playerinput} got Oak's parcel","Clerk:Okay! Say hi to PROF.OAK for me!")

            case "The End":
                self.Screen.fill("cornsilk1")
                self.Screen.blit(self.EndScreenTitle,self.Title_rect)
                self.Screen.blit(self.EndScreenStaffTitle,self.EndScreenStaffTitle_rect)
                self.Screen.blit(self.EndScreenStaff,self.EndScreenStaff_rect)
                self.Screen.blit(self.Credits,self.Credits_rect)
                self.Screen.blit(self.Credited,self.Credited_rect)
                self.Screen.blit(self.KeepPlayingTitle,self.KeepPlayingTitle_rect)
                self.Screen.blit(self.ClickNext,self.ClickNext_rect)

    def Dialouge(self,Text1:str,Text2:str = "",Text3:str = "",Text4:str = "",Next = True):
        self.Text1 = self.Game_font.render(Text1,True,"Black")
        self.Text1_rect = self.Text1.get_rect(topleft = (self.TextBox.topleft[0] + 5,self.TextBox.topleft[1] + 10))
        self.Text2 = self.Game_font.render(Text2,True,"Black")
        self.Text2_rect = self.Text2.get_rect(topleft = self.Text1_rect.bottomleft)
        self.Text3 = self.Game_font.render(Text3,True,"Black")
        self.Text3_rect = self.Text3.get_rect(topleft = self.Text2_rect.bottomleft)
        self.Text4 = self.Game_font.render(Text4,True,"Black")
        self.Text4_rect = self.Text4.get_rect(topleft = self.Text3_rect.bottomleft)
        pygame.draw.rect(self.Screen,"cornsilk1",self.TextBox,border_radius=12)
        pygame.draw.rect(self.Screen,"Black",self.TextBox_outline,3,12)
        self.Screen.blit(self.Text1,self.Text1_rect)
        self.Screen.blit(self.Text2,self.Text2_rect)
        self.Screen.blit(self.Text3,self.Text3_rect)
        self.Screen.blit(self.Text4,self.Text4_rect)
        if Next:
            self.Screen.blit(self.Next_Text,self.Next_Text_rect)