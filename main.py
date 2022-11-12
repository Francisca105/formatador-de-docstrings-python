from base import *
import pygame

pygame.init()

display = pygame.display.set_mode([480, 45])
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

pygame.display.set_caption("Formatador de texto")

text = 'Cola o teu texto nesta janela'
Loop = True


while Loop:
    display.fill([240, 240, 234])
    pygame.scrap.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == ((pygame.K_LCTRL or pygame.K_RCTRL) and pygame.K_v):
                pygame.scrap.put(pygame.SCRAP_TEXT, 
                bytes(
                    "\n".join(
                        justifica_texto(
                            str(bytes.decode(pygame.scrap.get(pygame.SCRAP_TEXT), encoding="latin"))
                            .replace(u'\x00', ''), 79))
                        , encoding="latin")
                        )

                text = "O texto formatado foi agora copiado"
                        

    text_surface = font.render(text, True, [0, 0, 0])
    display.blit(text_surface, [5,5])
    pygame.display.update()