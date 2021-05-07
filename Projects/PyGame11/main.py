import pygame,os

# setup display
pygame.init()
size = 900, 500
root = pygame.display.set_mode(size)
pygame.display.set_caption("11 Hangman")

color = 155, 89, 182

# load images
images = []
for i in range(7):
    image = pygame.image.load( str(i) + ".png" )
    images.append(pygame.transform.scale(image,(200,200)))
print(images)
FPS = 40 

def main():
    hangman = 0
    clock = pygame.time.Clock()
    root.fill(color)
    root.blit(images[hangman], (150,120))
    pygame.display.update()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
    pygame.quit()

if __name__ == "__main__":
    main()