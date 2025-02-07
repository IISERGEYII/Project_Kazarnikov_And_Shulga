import pygame




class Button:
    def __init__(self, ev, name, x, y, width, height, text, image_path, hover_im_path=None, size=20):
        self.x = x
        self.u = 0
        self.namer = name
        self.y = y
        self.size = size
        self.width = width
        self.ev = ev
        self.height = height
        self.text = text
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        self.protfield = 0
        self.reconstr = 0
        self.doubledmg = 0
        self.momentdmg = 0
        self.init_param = 0
        self.hack_spd = 1
        self.notice_code = 1
        self.health_virus = 1
        self.dmg_virus = 1

        if hover_im_path:
            self.hover_image = pygame.image.load(hover_im_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_hovered = False

    def draw_button(self, screen):
        if self.is_hovered:
            current_img = self.hover_image
        else:
            current_img = self.image
        screen.blit(current_img, self.rect.topleft)
        font = pygame.font.Font(None, self.size)
        text_surf = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))

    def button_event(self, num: int, nam: str):
        if num == 1:
            if nam == 'momentdmg_button' and self.u >= 1200:
                self.momentdmg += 1
                self.u -= 1200
            elif nam == 'protfield_button' and self.u >= 500:
                self.protfield += 1
                self.u -= 500
            elif nam == 'reconstr_button' and self.u >= 600:
                self.reconstr += 1
                self.u -= 500
            elif nam == 'doubledmg_button' and self.u >= 1200:
                self.doubledmg += 1
                self.u -= 1200
        elif num == 2:
            if nam == 'lightgame_button':
                self.init_param = {'rows': 9, 'cols': 10, 'mode_coeff': 0.5, 'HP': 0}
            elif nam == 'mediumgame_button':
                self.init_param = {'rows': 9, 'cols': 10, 'mode_coeff': 1, 'HP': 0}
            elif nam == 'hardgame_button':
                self.init_param = {'rows': 9, 'cols': 10, 'mode_coeff': 1.5, 'HP': 0}
        elif num == 3:
            if nam == 'hack_spd_button' and self.u >= 1000 and self.hack_spd <= 5:
                self.hack_spd += 1
                self.u -= 1000
            elif nam == 'noticecode_button' and self.u >= 1000 and self.notice_code <= 5:
                self.notice_code += 1
                self.u -= 1000
            elif nam == 'virus_health_button' and self.u >= 1000 and self.health_virus <= 5:
                self.health_virus += 1
                self.u -= 1000
            elif nam == 'virus_dmg_boost_button' and self.u >= 1000 and self.dmg_virus <= 5:
                self.dmg_virus += 1
                self.u -= 1000


class Label:
    def __init__(self, x, y, size=30, type=None):
        self.x = x
        self.y = y
        self.font_type = pygame.font.Font(type, size)

    def print_text_pygame(self, screen, text):
        self.text = self.font_type.render(text, True, (0, 0, 0))
        screen.blit(self.text, (self.x, self.y))
