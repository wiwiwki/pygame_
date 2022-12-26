import os
import pygame
import sys

# initializing the constructor
pygame.init()

# screen resolution
size = width, height = 990, 700

# opens up a window
screen = pygame.display.set_mode(size)

# white color
color = (105, 130, 120)

# light shade of the button
color_light = (105, 130, 120)

# dark shade of the button
color_dark = (5, 30, 20)

smallfont = pygame.font.SysFont('Tempus Sans ITC', 40)

# rendering a text written in
# this font
def main():
    text = smallfont.render('Sign in', True, color)
    text2 = smallfont.render('Create account', True, color)
    # text_res = smallfont.render('Hi! If u already have account into our game, lets log in!', True, color)
    multitext = "Hi! If you already have account into our game,\n                           let's log in!\n                     Else let's go sign up:)\n     Another info you can get with my email:\n                    nepisatt@gmail.com"
    run = True
    while run:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                run = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                pass

        screen.fill((15, 50, 40))
        all_sprites.draw(screen)
        mouse = pygame.mouse.get_pos()

        if width / 2 - 230 <= mouse[0] <= width / 2 + 220 and height / 2 + 100 <= mouse[1] <= height / 2 + 200:
            pygame.draw.rect(screen, color_light, [270, 450, 450, 100], 2, 4)
        else:
            pygame.draw.rect(screen, color_dark, [270, 450, 450, 100], 2, 4)

        if width / 2 - 230 <= mouse[0] <= width / 2 + 220 and height / 2 + 220 <= mouse[1] <= height / 2 + 320:
            pygame.draw.rect(screen, color_light, [270, 570, 450, 100], 2, 4)
        else:
            pygame.draw.rect(screen, color_dark, [270, 570, 450, 100], 2, 4)

        # superimposing the text onto our button
        screen.blit(text, (440, height / 1.5 + 5))
        screen.blit(text2, (380, 590))
        # screen.blit(text_res, (100, 100))

        # updates the frames of the game
        blitlines(screen, multitext, smallfont, color, 100, 100)
        pygame.display.update()

def load_image(name, colorkey=None):
    fullname = 'data/' + name
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def blitlines(surf, text, renderer, color, x, y):
    h = renderer.get_height()
    lines = text.split('\n')
    for i, ll in enumerate(lines):
        txt_surface = renderer.render(ll, True, color)
        surf.blit(txt_surface, (x, y + (i * h)))
    pygame.display.flip()

#загрузка скелета
class skeleton(pygame.sprite.Sprite):
    image = load_image("skelet8.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = skeleton.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    skeleton((-50, 370))
    main()