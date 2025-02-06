import pygame
import os
import random
from board_pygame import *

pygame.font.init()
FPS = 60

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
                    terminate()
                elif event.type == pygame.KEYUP:
                    return
            self.render_screen(sc)
            pygame.display.flip()
            clock.tick(FPS)



clock = pygame.time.Clock()
init_param = {"rows": 9, "cols": 10, "mode_coeff": 0.5, "HP": 0}
field = The_playing_field(10, 9, init_param)
screen = pygame.display.set_mode((1100, 1000))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
        if event.type == field.alarm_time_move_event:
            field.move_progres_alarm_timer()

    screen.fill((255, 255, 255))
    field.render(screen)
    pygame.display.flip()
    clock.tick(FPS)
