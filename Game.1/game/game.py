import pygame
import element

SZEROKOSC = 800
WYSOKOSC = 600

obraz_tła = pygame.image.load('background.png')
obraz_bazy_postaci = pygame.image.load('base.png')
pygame.init()

ekran = pygame.display.set_mode([SZEROKOSC, WYSOKOSC])
zegar = pygame.time.Clock()

nakrycie_glowy = element.NakrycieGlowy()
ubranie_element = element.UbranieElement()
oczy_element = element.OczyElement()
bron_element = element.BronElement()

pygame.font.init()
moja_czcionka = pygame.font.SysFont('Comic Sans M5', 30)

def wpiszTekst(ekran, tekst, pozycja):
    napis = moja_czcionka.render(tekst, False, (255, 255, 255))
    ekran.blit(napis, pozycja)

gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            gra_dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            if zdarzenie.key == pygame.K_q:
                nakrycie_glowy.wybierzNastepny()
            if zdarzenie.key == pygame.K_e:
                ubranie_element.wybierzNastepny()
            if zdarzenie.key == pygame.K_r:
                oczy_element.wybierzNastepny()
            if zdarzenie.key == pygame.K_t:
                bron_element.wybierzNastepny()
    ekran.blit(obraz_tła, (0, 0))
    ekran.blit(obraz_bazy_postaci, (270, 130))
    ekran.blit(nakrycie_glowy.wybranyObraz(), (270, 130))
    ekran.blit(ubranie_element.wybranyObraz(), (270, 130))
    ekran.blit(oczy_element.wybranyObraz(), (270, 130))
    ekran.blit(bron_element.wybranyObraz(), (270, 130))
    
    wpiszTekst(ekran, f"[Q] Glowa: {nakrycie_glowy.wybrany}", (100, 100))
    wpiszTekst(ekran, f"[e] Ubranie: {ubranie_element.wybrany}", (100, 140))
    wpiszTekst(ekran, f"[r] Oczy: {oczy_element.wybrany}", (100, 180))
    wpiszTekst(ekran, f"[t] bron: {bron_element.wybrany}", (100, 220))
    wpiszTekst(ekran, f"[S] Zapisz", (100, 260))
    
    if zapisywanie:
        moja_czcionka = pygame.font.SysFont('Comic Sans M5', 0)
        pygame.image.save(ekran, 'postac.png')
        zapisywanie = False
        moja_czcionka = pygame.font.SysFont('Comic Sans M5', 30)
    pygame.display.flip()
    
    zegar.tick(30)
            
pygame.quit()