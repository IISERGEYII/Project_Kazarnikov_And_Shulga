import sys

import pygame

from buttons import Button, Label

pygame.init()

width, height = 1500, 700
running = True
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('df')
a = dict()
d = []
protfield_button = Button(1, 'protfield_button', 100, 500, 280, 30, 'Купить защитное поле за 500 очков', 'img.png',
                          'img_1.png')
a[str(protfield_button)] = [protfield_button.x, protfield_button.y, protfield_button.width, protfield_button.height]
d.append(protfield_button)
reconstr_button = Button(1, 'reconstr_button', 100, 540, 280, 30, 'Купить реконструкцию за 600 очков', 'img.png',
                         'img_1.png')
a[str(reconstr_button)] = [reconstr_button.x, reconstr_button.y, reconstr_button.width, reconstr_button.height]
d.append(reconstr_button)
doubledmg_button = Button(1, 'doubledmg_button', 100, 580, 280, 30, 'Купить двойной урон за 1200 очков', 'img.png',
                          'img_1.png')
a[str(doubledmg_button)] = [doubledmg_button.x, doubledmg_button.y, doubledmg_button.width, doubledmg_button.height]
d.append(doubledmg_button)
momentdmg_button = Button(1, 'momentdmg_button', 100, 620, 280, 30, 'Купить моментальный урон за 1200 очков', 'img.png',
                          'img_1.png')
a[str(momentdmg_button)] = [momentdmg_button.x, momentdmg_button.y, momentdmg_button.width, momentdmg_button.height]
d.append(momentdmg_button)
lightgame_button = Button(2, 'lightgame_button', 100, 220, 280, 100, 'Режим для новичков', 'img.png', 'img_1.png')
a[str(lightgame_button)] = [lightgame_button.x, lightgame_button.y, lightgame_button.width, lightgame_button.height]
d.append(lightgame_button)
mediumgame_button = Button(2, 'mediumgame_button', 500, 220, 280, 100, 'Режим для опытных', 'img.png', 'img_1.png')
a[str(mediumgame_button)] = [mediumgame_button.x, mediumgame_button.y, mediumgame_button.width, mediumgame_button.height]
d.append(mediumgame_button)
hardgame_button = Button(2, 'hardgame_button', 900, 220, 280, 100, 'Лютый хардкор', 'img.png', 'img_1.png')
a[str(hardgame_button)] = [hardgame_button.x, hardgame_button.y, hardgame_button.width, hardgame_button.height]
d.append(hardgame_button)
hack_spd_button = Button(3, 'hack_spd_button', 900, 500, 280, 30, 'Купить увеличение скорости взлома', 'img.png',
                         'img_1.png')
a[str(hack_spd_button)] = [hack_spd_button.x, hack_spd_button.y, hack_spd_button.width, hack_spd_button.height]
d.append(hack_spd_button)
noticecode_button = Button(3, 'noticecode_button', 900, 500, 280, 30, 'Купить незаметность шифровки', 'img.png',
                           'img_1.png')
a[str(noticecode_button)] = [noticecode_button.x, noticecode_button.y, noticecode_button.width, noticecode_button.height]
d.append(noticecode_button)
'''hack_spd_button = Button(3, 'hack_spd_button', 900, 500, 280, 30, 'Купить увеличение здоровья вируса', 'img.png',
                         'img_1.png')
a[hardgame_button] = [hardgame_button.x, hardgame_button.y, hardgame_button.width, hardgame_button.height]
hack_spd_button = Button(3, 'hack_spd_button', 900, 500, 280, 30, 'Купить увеличение урона вируса', 'img.png',
                         'img_1.png')
a[hardgame_button] = [hardgame_button.x, hardgame_button.y, hardgame_button.width, hardgame_button.height]'''
la_equip = Label(100, 440)
la_protfield = Label(400, 500)
la_reconstr = Label(400, 540)
la_doubledmg = Label(400, 580)
la_momentdmg = Label(400, 620)
la_amountequip = Label(400, 440)
la_points = Label(1300, 100)
la_improvement = Label(900, 440)
while running:
    screen.fill('white')
    for event in pygame.event.get():
        protfield_button.handle_event(event)
        reconstr_button.handle_event(event)
        doubledmg_button.handle_event(event)
        momentdmg_button.handle_event(event)
        hack_spd_button.handle_event(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            pass
            if event.Button.init_param != 0:
                init_param = event.button.init_param
    la_improvement.print_text_pygame(screen, f'улучшения')
    la_points.print_text_pygame(screen, f'{protfield_button.u}')
    la_protfield.print_text_pygame(screen, f'{protfield_button.protfield}')
    la_reconstr.print_text_pygame(screen, f'{reconstr_button.reconstr}')
    la_doubledmg.print_text_pygame(screen, f'{doubledmg_button.doubledmg}')
    la_momentdmg.print_text_pygame(screen, f'{momentdmg_button.momentdmg}')
    la_amountequip.print_text_pygame(screen, 'кол-во снаряжения')
    la_equip.print_text_pygame(screen, 'снаряжение')
    lightgame_button.check_hover(pygame.mouse.get_pos())
    lightgame_button.draw_button(screen)
    mediumgame_button.check_hover(pygame.mouse.get_pos())
    mediumgame_button.draw_button(screen)
    hardgame_button.check_hover(pygame.mouse.get_pos())
    hardgame_button.draw_button(screen)
    protfield_button.check_hover(pygame.mouse.get_pos())
    protfield_button.draw_button(screen)
    reconstr_button.check_hover(pygame.mouse.get_pos())
    reconstr_button.draw_button(screen)
    doubledmg_button.check_hover(pygame.mouse.get_pos())
    doubledmg_button.draw_button(screen)
    momentdmg_button.check_hover(pygame.mouse.get_pos())
    momentdmg_button.draw_button(screen)
    hack_spd_button.check_hover(pygame.mouse.get_pos())
    hack_spd_button.draw_button(screen)
    pygame.display.flip()
pygame.quit()
sys.exit()
