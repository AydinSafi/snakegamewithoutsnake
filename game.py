import pygame
import sys
import random

#settings
genislik = 600
yukseklik = 400


#game settings
FPS = 10
BLOCK_SIZE = 20
yem_size = 20
BASLANGIC_HIZI = 10
PUAN_ARALIGI = 5
skor = 0
seviye = 1

#colors
SIYAH = (0,0,0)
KOYU_GRI = ( 20, 20, 20)



pygame.init()
skor_font = pygame.font.Font(None, 36)
ekran = pygame.display.set_mode((genislik,yukseklik))
pygame.display.set_caption("Where the hell is that snake!!")
saat = pygame.time.Clock()

yilan = [[genislik // 2, yukseklik // 2]]
yon = (0, 0)

yem_location_x = (random.randint(0, (genislik - yem_size)//BLOCK_SIZE)* BLOCK_SIZE)
yem_location_y = (random.randint(0, (yukseklik - yem_size)//BLOCK_SIZE)* BLOCK_SIZE)
yem = (yem_location_x, yem_location_y)

#OYUN DONGUSU
running = True
while running:
    for event in pygame.event.get():
        # a way to quit game
        if event.type == pygame.QUIT:
            running = False
        # getting inputs from the player
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and yon!=(0, 1):
                yon = (0, -1)
            elif event.key == pygame.K_DOWN and yon!=(0, -1):
                yon = (0, 1)
            elif event.key == pygame.K_LEFT and yon!=(1, 0):
                yon = (-1, 0)
            elif event.key == pygame.K_RIGHT and yon!=(-1, 0):
                yon = (1, 0)
    if yilan:
        yeni_bas = (yilan[0][0] + yon[0] * BLOCK_SIZE, yilan[0][1] + yon[1] * BLOCK_SIZE)
        if yeni_bas[0] < 0 or yeni_bas[0] >= genislik or yeni_bas[1] >= yukseklik or yeni_bas[1] < 0 or yeni_bas in yilan[1:]:
            #deads
            running = False
        else:
            
            if yeni_bas == yem:
                yilan.insert(0, yeni_bas)
                skor += 1 # getting score up
                if skor % PUAN_ARALIGI == 0:
                    seviye += 1
                    FPS += 1
                # spawning our food at random place again
                yem_location_x = (random.randint(0, (genislik - yem_size//1)))
                yem_location_y = (random.randint(0, (yukseklik - yem_size//1)))
                yem = (yem_location_x, yem_location_y)
            else:
                yilan.pop()
        ekran.fill(SIYAH)
    
    for x in range(0, genislik, BLOCK_SIZE):
        for y in range(0, yukseklik, BLOCK_SIZE):
            # paint black and gray
            if ((x+y)// BLOCK_SIZE) % 2 == 0:
                pygame.draw.rect(ekran, KOYU_GRI, (x, y, BLOCK_SIZE, BLOCK_SIZE))
            else:
                pygame.draw.rect(ekran, SIYAH, (x, y, BLOCK_SIZE, BLOCK_SIZE))
                
    # printing the datas on the screen
    skor_yazi = skor_font.render("Skor: {}".format(skor), True, (255,255,255))
    seviye_yazi = skor_font.render("Seviye: {}".format(seviye), True, (255,255,255))
    ekran.blit(skor_yazi, (10,10))
    ekran.blit(seviye_yazi, (genislik-150,10))

    for parca in yilan:
        pygame.draw.rect(ekran, (0,255,0), (parca[0], parca[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.draw.rect(ekran, (255, 0, 0), (yem[0], yem[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()
    saat.tick(FPS)

pygame.quit()
sys.exit()