import os
import sys

from board_pygame import *

FPS = 60
import pygame
from buttons import Button, Label


class The_playing_field:
    def __init__(self, width, height, params):
        self.width = width
        self.height = height
        self.board = Board(params)

        self.left = 10
        self.top = 10
        self.cell_size = 100
        self.all_sprites = pygame.sprite.Group()
        self.hack_timers_events = {}
        self.enc_timers_events = {}
        self.progress_hack_start = pygame.USEREVENT + 1
        self.progress_hack_current = pygame.USEREVENT + 1
        self.progress_hack_end = self.progress_hack_current + (params["rows"] * params["cols"])
        self.progress_enc_start = self.progress_hack_end + 1
        self.progress_enc_current = self.progress_hack_end + 1
        self.progress_enc_end = self.progress_enc_current + (params["rows"] * params["cols"])
        self.event_end_game = self.progress_enc_end + 1
        self.alarm_time_move_event = self.event_end_game + 1
        self.alarm_time_progres = 0
        self.alarm_time = False
        self.end_game_phrase = ""
        self.count = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        square = pygame.Rect(10, 10, self.cell_size - 1, self.cell_size - 10)
        script_field = pygame.Rect(310, 900, 175, 75)
        hacker_bar = pygame.Rect(12, 12, 20, 50)
        encrypted_bar = pygame.Rect(88, 12, 20, 50)
        informational_field = pygame.Rect(10, 900, 200, 75)
        end_timer_field = pygame.Rect(1020, 10, 75, 840)
        for i in range(self.height):
            for j in range(self.width):

                pygame.draw.rect(screen, "black", square.move(j * self.cell_size, i * self.cell_size - 10), width=1)
                pygame.draw.rect(screen, "green", hacker_bar.move(j * self.cell_size, i * self.cell_size - 10), width=1)
                pygame.draw.rect(screen, "green", encrypted_bar.move(j * self.cell_size, i * self.cell_size - 10),
                                 width=1)
                if self.board.nodeList[i][j].access is False:
                    image = self.load_image("notAccess.png")
                    image_rect = image.get_rect(
                        bottomright=((j + 1) * self.cell_size - 15, (i + 1) * self.cell_size - 40))
                    screen.blit(image, image_rect)

                elif self.board.nodeList[i][j].phase_node == 1:
                    if self.board.nodeList[i][j].main is True:
                        image = self.load_image("main_node_protect.png")
                    else:
                        image = self.load_image("node_protect.png")
                    if self.board.nodeList[i][j].isBlocked() is True:
                        image = self.load_image("blocked.png")
                    image_rect = image.get_rect(
                        bottomright=((j + 1) * self.cell_size - 15, (i + 1) * self.cell_size - 40))
                    screen.blit(image, image_rect)
                elif self.board.nodeList[i][j].phase_node == 1.5:
                    if self.board.nodeList[i][j].main is True:
                        image = self.load_image("main_node_protect.png")
                    else:
                        image = self.load_image("node_protect.png")
                    image_rect = image.get_rect(
                        bottomright=((j + 1) * self.cell_size - 15, (i + 1) * self.cell_size - 40))
                    screen.blit(image, image_rect)
                    progress_hack_bar = pygame.Rect(12, 12, 20, self.board.nodeList[i][j].hackProgress / 2)
                    pygame.draw.rect(screen, "green",
                                     progress_hack_bar.move(j * self.cell_size, i * self.cell_size - 10))
                elif self.board.nodeList[i][j].phase_node == 2:
                    if self.board.nodeList[i][j].main is True:
                        image = self.load_image("main_node_hacked.png")
                    else:
                        image = self.load_image("node_hacked.png")
                    image_rect = image.get_rect(
                        bottomright=((j + 1) * self.cell_size - 15, (i + 1) * self.cell_size - 40))
                    screen.blit(image, image_rect)
                    pygame.draw.rect(screen, "green", hacker_bar.move(j * self.cell_size, i * self.cell_size - 10))
                elif self.board.nodeList[i][j].phase_node == 2.5:
                    if self.board.nodeList[i][j].main is True:
                        image = self.load_image("main_node_hacked.png")
                    else:
                        image = self.load_image("node_hacked.png")
                    image_rect = image.get_rect(
                        bottomright=((j + 1) * self.cell_size - 15, (i + 1) * self.cell_size - 40))
                    screen.blit(image, image_rect)
                    progress_enc_bar = pygame.Rect(88, 12, 20, self.board.nodeList[i][j].encryptedProgress / 2)
                    pygame.draw.rect(screen, "green",
                                     progress_enc_bar.move(j * self.cell_size, i * self.cell_size - 10))
                    pygame.draw.rect(screen, "green", hacker_bar.move(j * self.cell_size, i * self.cell_size - 10))
                elif self.board.nodeList[i][j].phase_node == 3:
                    image = self.load_image("encrypted.png")
                    image_rect = image.get_rect(
                        bottomright=((j + 1) * self.cell_size - 15, (i + 1) * self.cell_size - 40))
                    screen.blit(image, image_rect)
                    pygame.draw.rect(screen, "green", hacker_bar.move(j * self.cell_size, i * self.cell_size - 10))
                    pygame.draw.rect(screen, "green",
                                     encrypted_bar.move(j * self.cell_size, i * self.cell_size - 10))
                elif self.board.nodeList[i][j].phase_node == 4:
                    if self.board.nodeList[i][j].av.type == 1:
                        image = self.load_image("kaspersky.png")
                    elif self.board.nodeList[i][j].av.type == 2:
                        image = self.load_image("bitdefender.png")
                    elif self.board.nodeList[i][j].av.type == 3:
                        image = self.load_image("norton.png")
                    elif self.board.nodeList[i][j].av.type == 4:
                        image = self.load_image("mcaffee.png")
                    image_rect = image.get_rect(
                        bottomright=((j + 1) * self.cell_size - 15, (i + 1) * self.cell_size - 40))
                    screen.blit(image, image_rect)
                    f1 = pygame.font.Font(None, 24)
                    text1 = f1.render(f'{self.board.nodeList[i][j].av.getHP()}', True,
                                      (0, 0, 0))
                    hp_surface = pygame.Surface((90, 15))
                    hp_surface.fill((255, 0, 0))
                    hp_surface.set_alpha(200)
                    progress_hack_bar = pygame.Rect(12, 12, 20, self.board.nodeList[i][j].hackProgress / 2)
                    hp_surface.set_alpha(250)
                    screen.blit(hp_surface, (15 + j * self.cell_size, 80 + i * self.cell_size - 10))
                    screen.blit(text1, (45 + j * self.cell_size, 80 + i * self.cell_size - 10))
                    pygame.draw.rect(screen, "green",
                                     progress_hack_bar.move(j * self.cell_size, i * self.cell_size - 10))
            for i in range(4):
                pygame.draw.rect(screen, "black", script_field.move(i * 200, 0), width=1)
            pygame.draw.rect(screen, "black", informational_field, width=1)
            HP_font = pygame.font.Font(None, 24)
            HP_text = HP_font.render(f'HP вируса:    {self.board.virus.getHP()}', True, (0, 0, 0))
            HP_surface = pygame.Surface((200, 37.5))
            HP_surface.fill((255, 0, 0))
            HP_surface.set_alpha(200)
            SHIELD_font = pygame.font.Font(None, 24)
            SHIELD_text = SHIELD_font.render(f'Щит вируса:    {self.board.virus.shield}', True, (0, 0, 0))
            SHIELD_surface = pygame.Surface((200, 37.5))
            SHIELD_surface.fill((0, 200, 255))
            SHIELD_surface.set_alpha(200)
            screen.blit(HP_surface, (10, 900))
            screen.blit(HP_text, (15, 905))
            screen.blit(SHIELD_surface, (10, 937.5))
            screen.blit(SHIELD_text, (15, 942.5))
            alarm_time_font = pygame.font.Font(None, 36)
            alarm_time_text = alarm_time_font.render(f'{60 - self.alarm_time_progres}', True, (0, 0, 0))
            pygame.draw.rect(screen, "black", end_timer_field, width=1)
            if self.alarm_time is True:
                progress_alarm_timer_bar = pygame.Rect(1020, 10, 75, 14 * self.alarm_time_progres)
                pygame.draw.rect(screen, "red", progress_alarm_timer_bar)
            screen.blit(alarm_time_text, (1030, 480))

    def phase_change(self, node):
        phase = node.phase_node
        if node.isBlocked():
            node.phase_node = phase
        elif node.access is False:
            node.phase_node = phase
        elif phase == 1:
            pygame.time.set_timer(self.progress_hack_current, 100)
            self.hack_timers_events[self.progress_hack_current] = node
            self.progress_hack_current += 1
            node.phase_node = 1.5
        elif phase == 2:
            pygame.time.set_timer(self.progress_enc_current, 100)
            self.enc_timers_events[self.progress_enc_current] = node
            self.progress_enc_current += 1
            node.phase_node = 2.5
        elif phase == 4:
            self.board.attackNode(node)
            if node.av.destroyed:
                self.return_phase_node(node)
            if self.board.virus.getHP() <= 0:
                pygame.time.set_timer(self.event_end_game, 10)
                self.end_game_phrase = "П  О  Р  А  Ж  Е  Н  И  Е  :  в  и  р  у  с   у  н  и  ч  т  о  ж  е  н"

    def move_progres_alarm_timer(self):
        self.alarm_time_progres += 1
        if self.alarm_time_progres >= 60:
            pygame.time.set_timer(self.event_end_game, 10)
            self.end_game_phrase = "П  О  Р  А  Ж  Е  Н  И  Е   :   в  а  с   о  т  к  л  ю  ч  и  л  и   о  т   с  и  с  т  е  м ы"

    def return_phase_node(self, node):
        if node.isEncrypted():
            node.setPhase(3)
        elif node.isHacked():
            node.setPhase(2)
        else:
            node.setPhase(1)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        i, j = (y - self.top) // self.cell_size, \
               (x - self.left) // self.cell_size
        return i, j

    def on_click(self, cell_coords):
        if cell_coords is not None:
            i, j = cell_coords
            self.phase_change(self.board.nodeList[i][j])

    def get_click(self, mouse_pos):
        x, y = mouse_pos
        if self.left <= x <= self.width * self.cell_size + self.left and \
                self.top <= y <= self.height * self.cell_size + self.top:
            cell_coord = self.get_cell(mouse_pos)
            self.on_click(cell_coord)
        else:
            self.on_click(None)

    def load_image(self, name):
        image = pygame.image.load(os.path.join("icons", name))
        return image

    def render_screen(self, sc):
        main_font = pygame.font.Font(None, 24)
        main_text = main_font.render(self.end_game_phrase, True, (0, 0, 0))
        image_1 = pygame.transform.scale(self.load_image("encrypted.png"), (100, 100))
        image_rect_1 = image_1.get_rect(
            bottomright=(100, 200))
        image_2 = pygame.transform.scale(self.load_image("alert.png"), (100, 100))
        image_rect_2 = image_2.get_rect(
            bottomright=(400, 200))
        image_3 = pygame.transform.scale(self.load_image("main_node_hacked.png"), (100, 100))
        image_rect_3 = image_3.get_rect(
            bottomright=(700, 200))
        sc.blit(image_1, image_rect_1)
        sc.blit(image_2, image_rect_2)
        sc.blit(image_3, image_rect_3)
        count_font = pygame.font.Font(None, 24)
        global coun
        coun = self.get_count()
        count_text = count_font.render(f"Суммарно очков: {self.get_count()}", True, (0, 0, 0))
        sc.blit(count_text, (10, 350))
        sc.blit(main_text, (10, 10))

    def get_count(self):
        return self.count

    def end_game_screen(self):
        sc = pygame.display.set_mode((800, 400))
        sc.fill((255, 255, 255))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    play_menu()
                elif event.type == pygame.KEYUP:
                    return
            self.render_screen(sc)
            pygame.display.flip()
            clock.tick(FPS)


def play_game(params):
    screen = pygame.display.set_mode((1100, 1000))
    running = True
    field = The_playing_field(10, 9, params)
    coun = field.get_count()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen = pygame.display.set_mode((1500, 700))
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                field.get_click(event.pos)
                field.render(screen)
            if event.type in range(field.progress_hack_start, field.progress_hack_end):
                node = field.hack_timers_events.get(event.type)
                node.moveHackProgress()
                if node.hacked:
                    field.count += 50
                    node.phase_node = 2
                    pygame.time.set_timer(event.type, 0)
                    accessibleNodes = field.board.accessibleNodes(node)
                    for access_node in accessibleNodes:
                        access_node.setAccess()
                elif node.avActive():
                    pygame.time.set_timer(event.type, 0)
                    node.phase_node = 4
                    accessibleNodes = field.board.accessibleNodes(node)
                    for node_block in accessibleNodes:
                        if node_block.avActive() is False:
                            node.blockedList.append(node_block)
                            node_block.setBlock(True, node.getAV())
                    field.board.virus.setAP(field.board.virus.getAP() - node.getAV().effect)
                    field.board.activeAV.append(node.getAV())
                    if node.getAV().type == 3:
                        field.board.activeRepairs.append(node.getAV())
            if event.type in range(field.progress_enc_start, field.progress_enc_end):
                node = field.enc_timers_events.get(event.type)
                node.moveEncProgress()
                if node.encrypted:
                    node.phase_node = 3
                    pygame.time.set_timer(event.type, 0)
                    if node.isMain():
                        field.count += 5000
                        pygame.time.set_timer(field.event_end_game, 10)
                        field.end_game_phrase = "П  О  Б  Е  Д  А  :  г  л  а  в  н  а  я   н  о  д  а   в  з  л  о  м  а  н  а"

                    field.count += 500
                    if field.alarm_time is False and node.start_alarm is True:
                        field.alarm_time = True
                        pygame.time.set_timer(field.alarm_time_move_event, 1000)
            if event.type == field.event_end_game:
                field.end_game_screen()
                running = False
                play_menu()
            if event.type == field.alarm_time_move_event:
                field.move_progres_alarm_timer()

        screen.fill((255, 255, 255))
        field.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    play_menu()


clock = pygame.time.Clock()

coun = 0


def play_menu():
    pygame.init()
    pygame.font.init()
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
    momentdmg_button = Button(1, 'momentdmg_button', 100, 620, 280, 30, 'Купить моментальный урон за 1200 очков',
                              'img.png',
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
    virus_health_button = Button(3, 'hack_spd_button', 700, 580, 280, 30, 'Купить увеличение здоровья вируса',
                                 'img.png',
                                 'img_1.png')
    virus_dmg_boost_button = Button(3, 'hack_spd_button', 700, 620, 280, 30, 'Купить увеличение урона вируса',
                                    'img.png',
                                    'img_1.png')
    la_equip = Label(100, 440)
    la_protfield = Label(400, 500)
    la_reconstr = Label(400, 540)
    la_doubledmg = Label(400, 580)
    la_momentdmg = Label(400, 620)
    la_amountequip = Label(400, 440)
    la_points = Label(600, 100)
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
                    play_game({'rows': 9, 'cols': 10, 'mode_coeff': 0.5, 'HP': 0})
                elif event.button == hardgame_button:
                    hardgame_button.button_event(hardgame_button.ev, hardgame_button.namer)
                    play_game({'rows': 9, 'cols': 10, 'mode_coeff': 1.5, 'HP': 0})
                elif event.button == mediumgame_button:
                    mediumgame_button.button_event(mediumgame_button.ev, mediumgame_button.namer)
                    play_game({'rows': 9, 'cols': 10, 'mode_coeff': 1.0, 'HP': 0})
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
        if coun == 0:
            la_points.print_text_pygame(screen, f'{0}')
        else:
            la_points.print_text_pygame(screen, f'{coun} очков')
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


play_menu()
