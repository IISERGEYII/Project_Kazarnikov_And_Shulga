import sys

import pygame
from buttons import Button, Label

pygame.init()

width, height = 1500, 700
running = True
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('df')
d = []
protfield_button = Button(1, 'protfield_button', 100, 500, 280, 30, 'Купить защитное поле за 500 очков', 'img.png',
                          'img_1.png')
d.append(protfield_button)
reconstr_button = Button(1, 'reconstr_button', 100, 540, 280, 30, 'Купить реконструкцию за 600 очков', 'img.png',
                         'img_1.png')
d.append(reconstr_button)
doubledmg_button = Button(1, 'doubledmg_button', 100, 580, 280, 30, 'Купить двойной урон за 1200 очков', 'img.png',
                          'img_1.png')
d.append(doubledmg_button)
momentdmg_button = Button(1, 'momentdmg_button', 100, 620, 280, 30, 'Купить моментальный урон за 1200 очков', 'img.png',
                          'img_1.png')
d.append(momentdmg_button)
lightgame_button = Button(2, 'lightgame_button', 100, 220, 280, 100, 'Режим для новичков', 'img.png', 'img_1.png')
d.append(lightgame_button)
mediumgame_button = Button(2, 'mediumgame_button', 500, 220, 280, 100, 'Режим для опытных', 'img.png', 'img_1.png')
d.append(mediumgame_button)
hardgame_button = Button(2, 'hardgame_button', 900, 220, 280, 100, 'Лютый хардкор', 'img.png', 'img_1.png')
d.append(hardgame_button)
hack_spd_button = Button(3, 'hack_spd_button', 700, 500, 280, 30, 'Купить увеличение скорости взлома', 'img.png',
                         'img_1.png')
d.append(hack_spd_button)
noticecode_button = Button(3, 'noticecode_button', 700, 540, 280, 30, 'Купить незаметность шифровки', 'img.png',
                           'img_1.png')
d.append(noticecode_button)
virus_health_button = Button(3, 'hack_spd_button', 700, 580, 280, 30, 'Купить увеличение здоровья вируса', 'img.png',
                         'img_1.png')
virus_dmg_boost_button = Button(3, 'hack_spd_button', 700, 620, 280, 30, 'Купить увеличение урона вируса', 'img.png',
                         'img_1.png')
la_equip = Label(100, 440)
la_protfield = Label(400, 500)
la_reconstr = Label(400, 540)
la_doubledmg = Label(400, 580)
la_momentdmg = Label(400, 620)
la_amountequip = Label(400, 440)
la_points = Label(1300, 100)
la_improvement = Label(900, 440)
la_improve_level = Label(1100, 440)
la_hack_spd = Label(1300, 500)
la_notice_code = Label(1300, 540)
la_health_virus = Label(1300, 580)
la_dmg_virus = Label(1300, 620)
while running:
    screen.fill('white')
    for event in pygame.event.get():
        protfield_button.handle_event(event)
        reconstr_button.handle_event(event)
        doubledmg_button.handle_event(event)
        momentdmg_button.handle_event(event)
        hack_spd_button.handle_event(event)
        lightgame_button.handle_event(event)
        mediumgame_button.handle_event(event)
        hardgame_button.handle_event(event)
        hack_spd_button.handle_event(event)
        virus_health_button.handle_event(event)
        virus_dmg_boost_button.handle_event(event)
        noticecode_button.handle_event(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            if event.button == lightgame_button:
                lightgame_button.button_event(lightgame_button.ev, lightgame_button.namer)
                init_param = {'rows': 9, 'cols': 10, 'mode_coeff': 0.5, 'HP': 0}
                import the_playing_field
            elif event.button == hardgame_button:
                hardgame_button.button_event(hardgame_button.ev, hardgame_button.namer)
                init_param = {'rows': 9, 'cols': 10, 'mode_coeff': 1.5, 'HP': 0}
                import the_playing_field
            elif event.button == mediumgame_button:
                mediumgame_button.button_event(mediumgame_button.ev, mediumgame_button.namer)
                init_param = {'rows': 9, 'cols': 10, 'mode_coeff': 1, 'HP': 0}
                import the_playing_field
            elif event.button == protfield_button:
                protfield_button.button_event(protfield_button.ev, protfield_button.namer)

            elif event.button == reconstr_button:
                reconstr_button.button_event(reconstr_button.ev, reconstr_button.namer)
            elif event.button == doubledmg_button:
                doubledmg_button.button_event(doubledmg_button.ev, doubledmg_button.namer)
            elif event.button == momentdmg_button:
                lightgame_button.button_event(lightgame_button.ev, lightgame_button.namer)
            elif event.button == hack_spd_button:
                hack_spd_button.button_event(hack_spd_button.ev, hack_spd_button.namer)
            elif event.button == noticecode_button:
                noticecode_button.button_event(noticecode_button.ev, noticecode_button.namer)
            elif event.button == virus_health_button:
                virus_health_button.button_event(virus_health_button.ev, virus_health_button.namer)
            elif event.button == virus_dmg_boost_button:
                virus_dmg_boost_button.button_event(virus_dmg_boost_button.ev, virus_dmg_boost_button.namer)
    la_hack_spd.print_text_pygame(screen, f'{hack_spd_button.hack_spd}')
    la_notice_code.print_text_pygame(screen, f'{noticecode_button.notice_code}')
    la_health_virus.print_text_pygame(screen, f'{virus_health_button.health_virus}')
    la_dmg_virus.print_text_pygame(screen, f'{virus_dmg_boost_button.dmg_virus}')
    la_improve_level.print_text_pygame(screen, "уровень улучшений(макс.5)")
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
    noticecode_button.check_hover(pygame.mouse.get_pos())
    noticecode_button.draw_button(screen)
    virus_health_button.check_hover(pygame.mouse.get_pos())
    virus_health_button.draw_button(screen)
    virus_dmg_boost_button.check_hover(pygame.mouse.get_pos())
    virus_dmg_boost_button.draw_button(screen)
    pygame.display.flip()
pygame.quit()
sys.exit()
