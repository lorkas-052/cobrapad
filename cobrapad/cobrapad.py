import pygame
import sys





screenX = 0
screenY = 0

pencere = None
arka_plan_rengi = (30, 30, 30) 
saat = None  
cizim_listesi = [] 
kutular = []


renkler = {
    "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
    "white": (255, 255, 255), "black": (0, 0, 0), "yellow": (255, 255, 0),
    "light_red": (255, 102, 102), "dark_red": (139, 0, 0), "crimson": (220, 20, 60),
    "light_green": (144, 238, 144), "dark_green": (0, 100, 0), "lime": (0, 255, 0), "olive": (128, 128, 0),
    "light_blue": (173, 216, 230), "dark_blue": (0, 0, 139), "cyan": (0, 255, 255), "navy": (0, 0, 128), "sky_blue": (135, 206, 235),
    "pink": (255, 192, 203), "dark_pink": (231, 84, 128), "hot_pink": (255, 105, 180), "purple": (128, 0, 128), "magenta": (255, 0, 255), "violet": (238, 130, 238),
    "orange": (255, 165, 0), "gold": (255, 215, 0), "yellow_green": (154, 205, 50),
    "brown": (165, 42, 42), "gray": (128, 128, 128), "dark_gray": (169, 169, 169), "light_gray": (211, 211, 211), "silver": (192, 192, 192),
    "turquoise": (64, 224, 208), "coral": (255, 127, 80), "salmon": (250, 128, 114)
}

def open_screen():
    global pencere, saat, screenX, screenY
    
    ana_modul = sys.modules['__main__']
  
    try:
        screenX = int(getattr(ana_modul, 'screenX', 0))
        screenY = int(getattr(ana_modul, 'screenY', 0))
    except (ValueError, TypeError):
        raise TypeError("Cobrapad Error: 'screenX' and 'screenY' values must be integers (int) only!")
        
    x = screenX  
    y = screenY  
    
    if x <= 0 or y <= 0:
        raise ValueError("Cobrapad Error: Screen dimensions (screenX and screenY) must be greater than 0!")
    

    try:
        pygame.init()
        saat = pygame.time.Clock()  
        pencere = pygame.display.set_mode((x, y))
        pygame.display.set_caption("Cobrapad Game Engine")
    except Exception as e:
        raise RuntimeError(f"Cobrapad Error: An issue occurred while opening the game window. Details: {e}")
    
   

class Bridge:
    def __init__(self):        
        self.kutu_hazirmi = False 
        
    def create_the_box(self):  
        if self.kutu_hazirmi:
            raise RuntimeError("Cobrapad Error: The box is already initialized! You cannot initialize it more than once.")
        else:
            self.kutu_hazirmi = True 
            print("Cobrapad: Box initialized successfully.")


calisma = None
def study(isim="calisma"):
    yeni_kopru = Bridge()
    ana_modul = sys.modules['__main__']  
    setattr(ana_modul, isim, yeni_kopru)
    return yeni_kopru

class ScreenManager:
    def paint(self, renk_adi):
        global arka_plan_rengi, renkler
        temiz_renk = renk_adi.lower().strip().replace(" ", "_")
        if temiz_renk not in renkler:
             raise ValueError(f"Cobrapad Error: The color '{renk_adi}' is not defined in the color list!")
        arka_plan_rengi = renkler.get(temiz_renk, (255, 255, 255))

class KareNesnesi:
    def __init__(self, x, y, w, h, renk):
        self.tip = "kare"
        self.x, self.y, self.w, self.h, self.renk = x, y, w, h, renk
        self.visible = True 
        

class DaireNesnesi:
    def __init__(self, x, y, yaricap, renk):
        self.tip = "daire"
        self.x, self.y, self.yaricap, self.renk = x, y, yaricap, renk
        self.visible = True 
        
class YaziNesnesi:
    def __init__(self, yazi, x, y, w, renk, tip):
        self.yazi = str(yazi)
        self.x = x 
        self.y = y 
        self.w = w 
        self.renk = renk 
        self.tip = tip 
        self.visible = True 
        
        try:
            self.font_objesi = pygame.font.SysFont(tip, w)
        except Exception:
            self.font_objesi = pygame.font.Font(None, w)
class DrawManager:
    def Rect(self, x, y, w, h, renk, kopru=None):
        if kopru and not kopru.kutu_hazirmi:
            raise RuntimeError("Cobrapad Error: You must call .create_the_box() before using draw.Rect()!")
        temiz_renk = renk.lower().strip().replace(" ", "_")
        if temiz_renk not in renkler:
            raise ValueError(f"Cobrapad Error: The color '{renk}' is not defined in the color list!")
        rgb_renk = renkler[temiz_renk]
        nesne = KareNesnesi(x, y, w, h, rgb_renk)  
        cizim_listesi.append(nesne)
        return nesne

    def Circle(self, x, y, yaricap, renk, kopru=None):
        if kopru and not kopru.kutu_hazirmi:
            raise RuntimeError("Cobrapad Error: You must call .create_the_box() before using draw.Circle()!")
        temiz_renk = renk.lower().strip().replace(" ", "_")
        if temiz_renk not in renkler:
            raise ValueError(f"Cobrapad Error: The color '{renk}' is not defined in the color list!")
        rgb_renk = renkler[temiz_renk]
        nesne = DaireNesnesi(x, y, yaricap, rgb_renk)  
        cizim_listesi.append(nesne)
        return nesne

        
        
class DisplayManager:
    
    def text(self, yazi, x, y, w, renk, tip="Arial"):
        global renkler
        temiz_renk = renk.lower().strip().replace(" ", "_")
        if temiz_renk not in renkler:
            
            raise ValueError(f"Cobrapad Error: The color '{renk}' is not defined in the color list!")
        rgb_renk = renkler.get(temiz_renk, (255, 255, 255)) 
        nesne = YaziNesnesi(yazi, x, y, w, rgb_renk, tip)  
        kutular.append(nesne)
        return nesne
        
def hide(nesne):
    nesne.visible = False
    
def show(nesne):
    nesne.visible = True
def run():
    global pencere, arka_plan_rengi, saat, cizim_listesi, kutular
    
    if pencere is None:
        raise RuntimeError("Cobrapad Error: You must call open_screen() before run()!")
    
    while True:
        for olay in pygame.event.get():
            if olay.type == pygame.QUIT:
                try:
                    pygame.quit()
                    sys.exit()
                except SystemExit:
                    pass
                
        if pencere:
            pencere.fill(arka_plan_rengi)
            for nesne in cizim_listesi:
                if nesne.visible:
                    if nesne.tip == "kare":
                        pygame.draw.rect(pencere, nesne.renk, (nesne.x, nesne.y, nesne.w, nesne.h))
                    elif nesne.tip == "daire":
                        pygame.draw.circle(pencere, nesne.renk, (nesne.x, nesne.y), nesne.yaricap)
            for nesne2 in kutular:
                if nesne2.visible:
                    yazi_resmi = nesne2.font_objesi.render(nesne2.yazi, True, nesne2.renk)
                    pencere.blit(yazi_resmi, (nesne2.x, nesne2.y))

        pygame.display.flip()
        
        if saat: saat.tick(60)

screen = ScreenManager()
draw = DrawManager()
display = DisplayManager()

