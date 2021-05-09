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

"""

Albert Calasanz Implementation

License:
-------------------------------------------------------------------------------
The MIT License (MIT)
Copyright 2017-2021 Albert Calasanz @acsstudios

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
import pygame,time,random
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('Example - Simple', (600, 400))
global mode
FPS = 60
global level
level = 1


modes = ['divisio','suma','multipliacio']
def set_mode(selected: Tuple, value: Any) -> None:
    global mode
    mode = selected[0][0]
    print(mode)

def start_the_game() -> None:
    global level,count,mode
    count = 0
    # Set up the drawing window
    screen = pygame.display.set_mode([600, 400])
    # Run until the user asks to quit
    running = True
    clock = pygame.time.Clock()
    try:
        level = int(level.get_value()[0])
        mode = mode.get_value()[0][0]
    except:
        pass
    print(level)
    if mode == "divisio":
        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill([128, 0, 128])
            num = random.randrange(1,level*2+5)
            divisor = random.randrange(1,level*2+5)
            x = num*divisor
            global font2
            if count <= max(range(level*2)):
                # LABEL 1
                string = f"Pregunta {count+1} de {max(range(level*2))+1}:"
                font = pygame_menu.font.get_font(pygame_menu.font.FONT_NEVIS, 20)
                blit = font.render(string, True, (200, 200, 200))
                blit_size = blit.get_size()
                screen.blit(blit, (int(600 / 2 - blit_size[0] / 2),
                                            int(400 / 2 - blit_size[1] / 2-100)))
                # LABEL 2
                string2 = f"{x}/{num} = "
                font2 = pygame_menu.font.get_font(pygame_menu.font.FONT_NEVIS, 50)
                blit2 = font2.render(string2, True, (200, 200, 200))
                screen.blit(blit2, (int(600 / 2 - blit_size[0] / 2),
                                            int(400 / 2 - blit_size[1] / 2- 40)))
            else:
                screen.fill((35,160,27))
                string2 = "Well Done!"
                font2 = pygame_menu.font.get_font(pygame_menu.font.FONT_NEVIS, 50)
                blit2 = font2.render(string2, True, (200, 200, 200))
                screen.blit(blit2, (int(600 / 2 - blit_size[0] / 2 - 100),
                                            int(400 / 2 - blit_size[1] / 2- 40)))
                string2 = f"{level} passed."
                font2 = pygame_menu.font.get_font(pygame_menu.font.FONT_NEVIS, 50)
                blit2 = font2.render(string2, True, (200, 200, 200))
                screen.blit(blit2, (int(600 / 2 - blit_size[0] / 2 - 100),
                                            int(400 / 2 - blit_size[1] / 2)))
            # Flip the display
            pygame.display.flip()
            clock.tick(FPS)
            time.sleep(1.5)
            if count <= max(range(level*2)):
                # Result
                string = str(divisor)
                blit=font2.render(string,True,(0,206,201))
                screen.blit(blit, (int(600 / 2 + blit_size[0] / 2+ 50),
                                                int(400 / 2 - blit_size[1] / 2- 40)))
                pygame.display.flip()
                time.sleep(0.8)
            count += 1

menu = pygame_menu.Menu(
    height=400,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Brain Age v1 by Albert CS                ',
    width=600
)

#5.Es crida un method en modes
mode = modes[0]
metodes = [(method,i+1) for i,method in enumerate(modes)]


user_name = menu.add.text_input('Name: ', default='Albert C', maxchar=10)
level = menu.add.dropselect('Level: ',[str(i) for i in range(1,10)],default=0)
mode = menu.add.selector('Difficulty: ', metodes, onchange=set_mode)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)
