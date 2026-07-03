import pygame
import sys









screenX = 0
screenY = 0

pencere = None
arka_plan_rengi = (0,0,0) 
saat = None  
cizim_listesi = [] 
kutular = []
kutu_hazirmi2 = False 
resim_kutusu = []
resim_kutusu2 = []
resim_kutusu3 = []
kutularin_listesi = []
button_kutusu = []
animasyon_kutusu = []






renkler = {
    "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
    "white": (255, 255, 255), "black": (0, 0, 0), "yellow": (255, 255, 0),
    "light_red": (255, 102, 102), "dark_red": (139, 0, 0), "crimson": (220, 20, 60),
    "light_green": (144, 238, 144), "dark_green": (0, 100, 0), "lime": (0, 255, 0), "olive": (128, 128, 0),
    "light_blue": (173, 216, 230), "dark_blue": (0, 0, 139), "cyan": (0, 255, 255), "navy": (0, 0, 128), "sky_blue": (135, 206, 235),
    "pink": (255, 192, 203), "dark_pink": (231, 84, 128), "hot_pink": (255, 105, 180), "purple": (128, 0, 128), "magenta": (255, 0, 255), "violet": (238, 130, 238),
    "orange": (255, 165, 0), "gold": (255, 215, 0), "yellow_green": (154, 205, 50),
    "brown": (165, 42, 42), "gray": (128, 128, 128), "dark_gray": (169, 169, 169), "light_gray": (211, 211, 211), "silver": (192, 192, 192),
    "turquoise": (64, 224, 208), "coral": (255, 127, 80), "salmon": (250, 128, 114),
    
    
    "teal": (0, 128, 128), "indigo": (75, 0, 130), "khaki": (240, 230, 140),
    "lavender": (230, 230, 250), "maroon": (128, 0, 0), "peach": (255, 218, 185),
    "mint": (189, 252, 201), "azure": (240, 255, 255), "chocolate": (210, 105, 30),
    "ivory": (255, 255, 240), "wheat": (245, 222, 179), "plum": (221, 160, 221),
    "charcoal": (54, 54, 54), "beige": (245, 245, 220), "tan": (210, 180, 140)
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
    def setup(self):
        global kutu_hazirmi2 
        kutu_hazirmi2 = True 



def study(isim="calisma"):
    yeni_kopru = Bridge()
    ana_modul = sys.modules['__main__']  
    setattr(ana_modul, isim, yeni_kopru)
    return yeni_kopru

class ScreenManager:
    def paint(self, renk_adi):
        global arka_plan_rengi, renkler
        temiz_renk = renk_adi.lower().strip().replace(" ", "_")
        if kutu_hazirmi2 == False:
        	raise ValueError("Cobrapad Error: You must call setup() before using screen.paint()!")
        else:
        	pass 
        if temiz_renk not in renkler:
             raise ValueError(f"Cobrapad Error: The color '{renk_adi}' is not defined in the color list!")
        arka_plan_rengi = renkler.get(temiz_renk, (255, 255, 255))

class KareNesnesi:
    def __init__(self, x, y, w, h, renk):
        self.tip = "kare"
        self.x, self.y, self.w, self.h, self.renk = x, y, w, h, renk
        self.visible = True
        self._moves_y = 0
        self._moves_x = 0
        self._moves_speed = 0
        self._moves_aktif = False

    def moves(self, y=0, x=0, speed=1):
        self._movesby_aktif = False 
        self._moves_y = y
        self._moves_x = x
        self._moves_speed = speed
        self._moves_aktif = True

    def movesBy(self, y=0, x=0, speed=1):
        self._moves_aktif = False
        self._movesby_hedef_x = self.x + x
        self._movesby_hedef_y = self.y + y
        mesafe = (x**2 + y**2) ** 0.5
        if mesafe == 0:
            self._movesby_speed_x = 0
            self._movesby_speed_y = 0
        else:
            self._movesby_speed_x = speed * (x / mesafe)
            self._movesby_speed_y = speed * (y / mesafe)
            self._movesby_aktif = True
    


class DaireNesnesi:
    def __init__(self, x, y, yaricap, renk):
        self.tip = "daire"
        self.x, self.y, self.yaricap, self.renk = x, y, yaricap, renk
        self.visible = True
        self._moves_y = 0
        self._moves_x = 0
        self._moves_speed = 0
        self._moves_aktif = False

    def moves(self, y=0, x=0, speed=1):
        self._movesby_aktif = False
        self._moves_y = y
        self._moves_x = x
        self._moves_speed = speed
        self._moves_aktif = True

    def movesBy(self, y=0, x=0, speed=1):
        self._moves_aktif = False
        self._movesby_hedef_x = self.x + x
        self._movesby_hedef_y = self.y + y
        mesafe = (x**2 + y**2) ** 0.5
        if mesafe == 0:
            self._movesby_speed_x = 0
            self._movesby_speed_y = 0
        else:
            self._movesby_speed_x = speed * (x / mesafe)
            self._movesby_speed_y = speed * (y / mesafe)
            self._movesby_aktif = True
    
      
        
        
class YaziNesnesi:
    def __init__(self, yazi, x, y, w, renk, tip):
        self.tip = "yazi"
        self._yazi = str(yazi)
        self.x = x 
        self.y = y 
        self.w = w 
        self.renk = renk 
        self.visible = True 
        
        try:
            self.font_objesi = pygame.font.SysFont(tip, w)
        except Exception:
            self.font_objesi = pygame.font.Font(None, w)
            
        self.surface = self.font_objesi.render(self._yazi, True, self.renk)
       

    @property
    def yazi(self):
        return self._yazi

    @yazi.setter
    def yazi(self, yeni_yazi):
        if self._yazi != str(yeni_yazi):
            self._yazi = str(yeni_yazi)
            self.surface = self.font_objesi.render(self._yazi, True, self.renk)
    def moves(self, y=0, x=0, speed=1):
        self._movesby_aktif = False
        self._moves_y = y
        self._moves_x = x
        self._moves_speed = speed
        self._moves_aktif = True 

    def movesBy(self, y=0, x=0, speed=1):
        self._moves_aktif = False
        self._movesby_hedef_x = self.x + x
        self._movesby_hedef_y = self.y + y
        mesafe = (x**2 + y**2) ** 0.5
        if mesafe == 0:
            self._movesby_speed_x = 0
            self._movesby_speed_y = 0
        else:
            self._movesby_speed_x = speed * (x / mesafe)
            self._movesby_speed_y = speed * (y / mesafe)
            self._movesby_aktif = True
class OvalNesnesi:
    def __init__(self, x, y, w, h, renk):
        self.tip = "oval"
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.renk = renk
        self.visible = True
        self._moves_y = 0
        self._moves_x = 0
        self._moves_speed = 0
        self._moves_aktif = False

    def moves(self, y=0, x=0, speed=1):
        self._movesby_aktif = False
        self._moves_y = y
        self._moves_x = x
        self._moves_speed = speed
        self._moves_aktif = True 

    def movesBy(self, y=0, x=0, speed=1):
        self._moves_aktif = False
        self._movesby_hedef_x = self.x + x
        self._movesby_hedef_y = self.y + y
        mesafe = (x**2 + y**2) ** 0.5
        if mesafe == 0:
            self._movesby_speed_x = 0
            self._movesby_speed_y = 0
        else:
            self._movesby_speed_x = speed * (x / mesafe)
            self._movesby_speed_y = speed * (y / mesafe)
            self._movesby_aktif = True

class PolygonNesnesi:
    def __init__(self, noktalar, kalinrik, renk):
        self.tip = "polygon"
        self.noktalar = noktalar
        self.renk = renk
        self.kalinrik = kalinrik
        self.visible = True
        
        
class ResimNesnesi:
    def __init__(self, ekran_resim):
        self.ekran_resim = ekran_resim
        orijinal_surface = pygame.image.load(ekran_resim).convert()
        self.surface = pygame.transform.scale(orijinal_surface, (screenX, screenY))
        self.visible = True

       
        

class Resim2Nesnesi:
    def __init__(self, resim):
        self.surface = pygame.image.load(resim).convert_alpha()
        self.x = 0
        self.y = 0
        self.visible = True
        self._moves_y = 0
        self._moves_x = 0
        self._moves_speed = 0
        self._moves_aktif = False

    def moves(self, y=0, x=0, speed=1):
        self._movesby_aktif = False
        self._moves_y = y
        self._moves_x = x
        self._moves_speed = speed
        self._moves_aktif = True

    def movesBy(self, y=0, x=0, speed=1):
        self._moves_aktif = False
        self._movesby_hedef_x = self.x + x
        self._movesby_hedef_y = self.y + y
        mesafe = (x**2 + y**2) ** 0.5
        if mesafe == 0:
            self._movesby_speed_x = 0
            self._movesby_speed_y = 0
        else:
            self._movesby_speed_x = speed * (x / mesafe)
            self._movesby_speed_y = speed * (y / mesafe)
            self._movesby_aktif = True

            	
            	
            	
            
class DrawManager:
    def Rect(self, x, y, w, h, renk):
        temiz_renk = renk.lower().strip().replace(" ", "_")
        if kutu_hazirmi2 == False:
        	raise ValueError("Cobrapad Error: You must call setup() before using draw.Rect()")
        else:
        	pass 
        	
        if temiz_renk not in renkler:
            raise ValueError(f"Cobrapad Error: The color '{renk}' is not defined in the color list!")
        rgb_renk = renkler[temiz_renk]
        nesne = KareNesnesi(x, y, w, h, rgb_renk)  
        cizim_listesi.append(nesne)
        return nesne
        
    def Oval(self, x, y, w, h, renk):
        temiz_renk = renk.lower().strip().replace(" ", "_")
        if kutu_hazirmi2 == False:
        	raise ValueError("Cobrapad Error: You must call setup() before using draw.Oval()")
        else:
        	pass 
        if temiz_renk not in renkler:
            raise ValueError(f"Cobrapad Error: The color '{renk}' is not defined in the color list!")
        
        rgb_renk = renkler[temiz_renk]
        nesne = OvalNesnesi(x, y, w, h, rgb_renk)  
        cizim_listesi.append(nesne)
        return nesne
        
    def Polygon(self, noktalar, kalinrik, renk):
        temiz_renk = renk.lower().strip().replace(" ", "_")
        if kutu_hazirmi2 == False:
        	raise ValueError("Cobrapad Error: You must call setup() before using draw.Polygon()")
        else:
        	pass 
        if temiz_renk not in renkler:
            raise ValueError(f"Cobrapad Error: The color '{renk}' is not defined in the color list!")
        
        rgb_renk = renkler[temiz_renk]
        nesne = PolygonNesnesi(noktalar, kalinrik, rgb_renk)  
        cizim_listesi.append(nesne)
        return nesne
    def place(self, nesne4, x, y, w, h):
        nesne4.x = x
        nesne4.y = y
        if not hasattr(nesne4, '_orijinal_surface'):
            nesne4._orijinal_surface = nesne4.surface.copy()
        nesne4.surface = pygame.transform.scale(nesne4._orijinal_surface, (w, h))
        if nesne4 not in resim_kutusu2:
            resim_kutusu2.append(nesne4)
        return nesne4
    	
    
    
    def Circle(self, x, y, yaricap, renk):
        temiz_renk = renk.lower().strip().replace(" ", "_")
        if kutu_hazirmi2 == False:
        	raise ValueError("Cobrapad Error: You must call setup() before using draw.Circle()")
        else:
        	pass 
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
        if kutu_hazirmi2 == False:
        	raise ValueError("Cobrapad Error: You must call setup() before using display.text()")
        else:
        	pass 
        if temiz_renk not in renkler:
            
            raise ValueError(f"Cobrapad Error: The color '{renk}' is not defined in the color list!")
        rgb_renk = renkler.get(temiz_renk, (255, 255, 255)) 
        nesne = YaziNesnesi(yazi, x, y, w, rgb_renk, tip)  
        kutular.append(nesne)
        return nesne
        
class AddManager:
    def background(self, ekran_resim):
        if kutu_hazirmi2 == False:
        	raise ValueError("Cobrapad Error: You must call setup() before using add.background()")
        else:
        	 pass
        if pencere is None:
            raise RuntimeError("Cobrapad Error: You must call open_screen() before add.background()!")
        nesne3 = ResimNesnesi(ekran_resim)
        resim_kutusu.append(nesne3)
        return nesne3
        
    def image(self, resim):
        if kutu_hazirmi2 == False:
        	raise ValueError("Cobrapad Error: You must call setup() before using add.image()")
        else:
        	pass
        if not pygame.get_init():
        	raise RuntimeError("Cobrapad Error: You must call open_screen() before add.image()!")
        nesne4 = Resim2Nesnesi(resim)
        return nesne4
        
        
def buttonCreate(nesne,onclick):
        if kutu_hazirmi2 == False:
        	raise ValueError("Cobrapad Error: You must call setup() before using buttonCreate()")
        nesne._onclick = onclick
        button_kutusu.append(nesne)
        return nesne 
        
 
def clearScreen():
    if kutu_hazirmi2 == False:
        raise ValueError("Cobrapad Error: You must call setup() before using clearScreen()")
    cizim_listesi.clear()
    kutular.clear()
    resim_kutusu.clear()
    resim_kutusu2.clear()
    button_kutusu.clear()
    kutularin_listesi.clear()

def collide(nesne1, nesne2):
    if kutu_hazirmi2 == False:
        raise ValueError("Cobrapad Error: You must call setup() before using collide()")
    
    def get_rect(nesne):
        if hasattr(nesne, 'surface'):
            return pygame.Rect(nesne.x, nesne.y, nesne.surface.get_width(), nesne.surface.get_height())
        elif nesne.tip == "daire":
            return pygame.Rect(nesne.x - nesne.yaricap, nesne.y - nesne.yaricap, nesne.yaricap*2, nesne.yaricap*2)
        elif nesne.tip == "polygon":
            xs = [n[0] for n in nesne.noktalar]
            ys = [n[1] for n in nesne.noktalar]
            return pygame.Rect(min(xs), min(ys), max(xs)-min(xs), max(ys)-min(ys))
        else:
            return pygame.Rect(nesne.x, nesne.y, nesne.w, nesne.h)
    
    return get_rect(nesne1).colliderect(get_rect(nesne2))
        	 	
        	 
        	 
        	        	 
        	
        
        
  
        
def hide(nesne):
    if kutu_hazirmi2 == False:
        raise ValueError("Cobrapad Error: You must call setup() before using hide()")
    nesne.visible = False

def show(nesne):
    if kutu_hazirmi2 == False:
        raise ValueError("Cobrapad Error: You must call setup() before using show()")
    nesne.visible = True
    

def stop(nesne, durduma_suresi, sonra):
    nesne._stop_baslangic = pygame.time.get_ticks()
    nesne._stop_sure = durduma_suresi * 1000
    nesne._stop_sonra = sonra
    kutularin_listesi.append(nesne)
    return kutularin_listesi
    

def _hareket_uygula(nesne):
    if hasattr(nesne, '_moves_aktif') and nesne._moves_aktif:
        nesne.x += nesne._moves_x * nesne._moves_speed
        nesne.y += nesne._moves_y * nesne._moves_speed

    if hasattr(nesne, '_movesby_aktif') and nesne._movesby_aktif:
        if abs(nesne.x - nesne._movesby_hedef_x) <= abs(nesne._movesby_speed_x):
            nesne.x = nesne._movesby_hedef_x
        else:
            nesne.x += nesne._movesby_speed_x

        if abs(nesne.y - nesne._movesby_hedef_y) <= abs(nesne._movesby_speed_y):
            nesne.y = nesne._movesby_hedef_y
        else:
            nesne.y += nesne._movesby_speed_y

        if nesne.x == nesne._movesby_hedef_x and nesne.y == nesne._movesby_hedef_y:
            nesne._movesby_aktif = False
    
def run(callback=None):
    global pencere, arka_plan_rengi, saat, cizim_listesi, kutular, kutu_hazirmi2

    if kutu_hazirmi2 == False:
        raise RuntimeError("Cobrapad Error: You must call the setup() method before running run()!")

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
            if olay.type == pygame.MOUSEBUTTONDOWN:
                ana_modul2 = sys.modules['__main__']
                fonksiyon = hasattr(ana_modul2, "__MOUSEBUTTONDOWN__")
                if fonksiyon:
                    fonksiyon2 = getattr(ana_modul2, "__MOUSEBUTTONDOWN__")
                    fonksiyon2(olay.pos)
                if olay.button == 1:
                    for nesne6 in button_kutusu:
                        if hasattr(nesne6, 'visible') and not nesne6.visible:
                            continue
                            
                        if hasattr(nesne6, 'tip'):
                            if nesne6.tip == "kare" or nesne6.tip == "oval":
                                rect = pygame.Rect(nesne6.x, nesne6.y, nesne6.w, nesne6.h)
                                if rect.collidepoint(olay.pos):
                                    nesne6._onclick()
                            elif nesne6.tip == "daire":
                                dx = olay.pos[0] - nesne6.x
                                dy = olay.pos[1] - nesne6.y
                                if (dx ** 2 + dy ** 2) <= nesne6.yaricap ** 2:
                                    nesne6._onclick()
                            elif nesne6.tip == "yazi":
                                rect = pygame.Rect(nesne6.x, nesne6.y, nesne6.surface.get_width(), nesne6.surface.get_height())
                                if rect.collidepoint(olay.pos):
                                    nesne6._onclick()
                        else:
                            rect = pygame.Rect(nesne6.x, nesne6.y, nesne6.surface.get_width(), nesne6.surface.get_height())
                            if rect.collidepoint(olay.pos):
                                nesne6._onclick()

        if callback:
            callback()

        if pencere:
            pencere.fill(arka_plan_rengi)

            for nesne3 in resim_kutusu:
                if nesne3.visible:
                    pencere.blit(nesne3.surface, (0, 0))

            for nesne in cizim_listesi:
                if nesne.visible:
                    if nesne.tip == "kare":
                        pygame.draw.rect(pencere, nesne.renk, (nesne.x, nesne.y, nesne.w, nesne.h))
                    elif nesne.tip == "daire":
                        pygame.draw.circle(pencere, nesne.renk, (nesne.x, nesne.y), nesne.yaricap)
                    elif nesne.tip == "oval":
                        pygame.draw.ellipse(pencere, nesne.renk, (nesne.x, nesne.y, nesne.w, nesne.h))
                    elif nesne.tip == "polygon":
                        pygame.draw.polygon(pencere, nesne.renk, nesne.noktalar, nesne.kalinrik)

                    _hareket_uygula(nesne)

            for karakter in resim_kutusu2:
                if karakter.visible:
                    pencere.blit(karakter.surface, (karakter.x, karakter.y))
                    _hareket_uygula(karakter)

            for nesne2 in kutular:
                if nesne2.visible:
                    pencere.blit(nesne2.surface, (nesne2.x, nesne2.y))
                    _hareket_uygula(nesne2)

            for nesne5 in list(kutularin_listesi):
                if hasattr(nesne5, '_stop_baslangic'):
                    if pygame.time.get_ticks() - nesne5._stop_baslangic >= nesne5._stop_sure:
                        nesne5._stop_sonra()
                        del nesne5._stop_baslangic
                        kutularin_listesi.remove(nesne5)

        pygame.display.flip()

        if saat:
            saat.tick(60)


screen = ScreenManager()
draw = DrawManager()
display = DisplayManager()
add = AddManager()



