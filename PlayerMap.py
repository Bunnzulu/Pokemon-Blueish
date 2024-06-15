import pygame,sys,random
import Pokemon
pygame.init()

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

HoveredPlace = ''


class LandMarks:
    def __init__(self,x:int,y:int,w:int,h:int,Place:str):
        self.rect = pygame.Rect(x,y,w,h)
        self.Place = Place
    
    def Check_Hover(self):
        global HoveredPlace
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            HoveredPlace = self.Place

class Map:
    def __init__(self):
        self.SelectedPlace = HoveredPlace
        self.FlyLocations = []
        self.image = pygame.image.load("Trainer_imgs\Town_Map.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (0,0))
        self.PlaceTextBox = pygame.Rect(self.rect.bottomleft,(800,200))
        self.Font = pygame.font.Font(None,30)
        self.Pallet_Town = LandMarks(158,438,40,40,"Pallet Town")
        self.Viridain_City = LandMarks(158,318,40,40,"Viridian City")
        self.Pewter_City = LandMarks(158,118,40,40,"Pewter City")
        self.Route3 = LandMarks(199,115,120,45,"Route 3")
        self.Mtmoon = LandMarks(310,74,46,42,"Mt.Moon")
        self.CeruleanCity = LandMarks(478,77,39,39,"Cerulean City")
        self.Route10 = LandMarks(639,148,37,49,"Route 10")
        self.LavenderTown = LandMarks(638,194,39,39,"Lavender Town")
        self.SaffronCity = LandMarks(478,197,39,39,"Saffron City")
        self.CeladonCity = LandMarks(358,197,39,39,"Celadon City")
        self.VermilionCity = LandMarks(478,357,39,39,"Vermilion City")
        self.FuschiaCity = LandMarks(399,515,39,39,"Fuchsia City")
        self.CinnabarIsland = LandMarks(158,598,40,40,"Cinnabar Island")
        self.IndigoPlateau = LandMarks(78,78,40,40,"Indigo Plateau")
        
    def Draw(self):
        self.HoveredPlace_surf = self.Font.render(HoveredPlace,True,"Black")
        self.HoveredPlace_rect = self.HoveredPlace_surf.get_rect(center =(400,730))
        self.SelectedPlace = HoveredPlace
        screen.blit(self.image,self.rect)
        pygame.draw.rect(screen,"White",self.PlaceTextBox)
        pygame.display.get_surface().blit(self.HoveredPlace_surf,self.HoveredPlace_rect)
        self.Pallet_Town.Check_Hover()
        self.Viridain_City.Check_Hover()
        self.Pewter_City.Check_Hover()
        self.Mtmoon.Check_Hover()
        self.Route3.Check_Hover()
        self.CeruleanCity.Check_Hover()
        self.Route10.Check_Hover()
        self.LavenderTown.Check_Hover()
        self.SaffronCity.Check_Hover()
        self.CeladonCity.Check_Hover()
        self.VermilionCity.Check_Hover()
        self.FuschiaCity.Check_Hover()
        self.CinnabarIsland.Check_Hover()
        self.IndigoPlateau.Check_Hover()

