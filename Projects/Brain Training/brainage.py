"""
pygame-menu
https://github.com/ppizarror/pygame-menu

EXAMPLE - SIMPLE
Super simple example of pygame-menu usage, featuring a selector and a button.

License:
-------------------------------------------------------------------------------
The MIT License (MIT)
Copyright 2017-2021 Pablo Pizarro R. @ppizarror

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-------------------------------------------------------------------------------
"""
import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('Example - Simple', (600, 400))
FPS = 60
global level
level = 1
def start_the_game() -> None:
    global level
    # Set up the drawing window
    screen = pygame.display.set_mode([600, 400])
    # Run until the user asks to quit
    running = True
    clock = pygame.time.Clock()
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill([128, 0, 128])
        string = "Hello"
        font = pygame_menu.font.get_font(pygame_menu.font.FONT_NEVIS, 100)
        blit = font.render(string, True, (255, 255, 255))
        blit_size = blit.get_size()
        screen.blit(blit, (int(600 / 2 - blit_size[0] / 2),
                                    int(400 / 2 - blit_size[1] / 2)))

        # Flip the display
        pygame.display.flip()
        clock.tick(FPS)

menu = pygame_menu.Menu(
    height=400,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Brain Age v1 by Albert CS                ',
    width=600
)

user_name = menu.add.text_input('Name: ', default='Albert C', maxchar=10)
level = menu.add.dropselect('Level: ',[str(i) for i in range(10)])
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)
