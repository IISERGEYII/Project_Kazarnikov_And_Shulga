import pygame
import os

from board_pygame import Board, Node


class The_playing_field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 100
        self.all_sprites = pygame.sprite.Group()

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        rect = pygame.Rect(self.left, self.top, self.cell_size, self.cell_size, width=1)
        for i in range(self.height):
            for j in range(self.width):

                pygame.draw.rect(screen, "black", rect.move(j * self.cell_size, i * self.cell_size), width=1)
                if self.board[i][j] == 0:
                    image = self.load_image("node_protect.png")
                    image_rect = image.get_rect(bottomright=((j + 1) * self.cell_size, (i + 1) * self.cell_size))
                    screen.blit(image, image_rect)
                else:
                    image = self.load_image("node_hacked.png")
                    image_rect = image.get_rect(bottomright=((j + 1) * self.cell_size, (i + 1) * self.cell_size))
                    screen.blit(image, image_rect)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        i, j = (y - self.top) // self.cell_size, \
               (x - self.left) // self.cell_size
        return i, j

    def on_click(self, cell_coords):
        if cell_coords is not None:
            i, j = cell_coords
            self.board[i][j] = (self.board[i][j] + 1) % 2

    def get_click(self, mouse_pos):
        x, y = mouse_pos
        if self.left <= x <= self.width * self.cell_size + self.left and \
                self.top <= y <= self.height * self.cell_size + self.top:
            cell_coord = self.get_cell(mouse_pos)
            self.on_click(cell_coord)
        else:
            self.on_click(None)

    def initIcons(self):
        icon_node_pr = pygame.image.save_extended("./res/icons/node_protect.png")
        self.icons[1] = icon_node_pr

        icon_node_hk = QIcon()
        icon_node_hk.addPixmap(QPixmap("./res/icons/node_hacked.png"))
        self.icons[2] = icon_node_hk

        icon_main_node_pr = QIcon()
        icon_main_node_pr.addPixmap(QPixmap("./res/icons/main_node_protect.png"))
        self.icons[3] = icon_main_node_pr

        icon_main_node_hk = QIcon()
        icon_main_node_hk.addPixmap(QPixmap("./res/icons/main_node_hacked.png"))
        self.icons[4] = icon_main_node_hk

        icon_block = QIcon()
        icon_block.addPixmap(QPixmap("./res/icons/blocked.png"))
        self.icons[5] = icon_block

        icon_encrypt = QIcon()
        icon_encrypt.addPixmap(QPixmap("./res/icons/encrypted.png"))
        self.icons[6] = icon_encrypt

        icon_kaspersky = QIcon()
        icon_kaspersky.addPixmap(QPixmap("./res/icons/kaspersky.png"))
        self.icons[7] = icon_kaspersky

        icon_bitdefender = QIcon()
        icon_bitdefender.addPixmap(QPixmap("./res/icons/bitdefender.png"))
        self.icons[8] = icon_bitdefender

        icon_norton = QIcon()
        icon_norton.addPixmap(QPixmap("./res/icons/norton.png"))
        self.icons[9] = icon_norton

        icon_mcafee = QIcon()
        icon_mcafee.addPixmap(QPixmap("./res/icons/mcaffee.png"))
        self.icons[10] = icon_mcafee

        icon_norton = QIcon()
        icon_norton.addPixmap(QPixmap("./res/icons/notAccess.png"))
        self.icons[11] = icon_norton

        icon_norton = QIcon()
        icon_norton.addPixmap(QPixmap("./res/icons/alert.png"))
        self.icons[12] = icon_norton

    def load_image(self, name):
        image = pygame.image.load(os.path.join("icons", name))
        return image


field = The_playing_field(10, 10)
screen = pygame.display.set_mode((1000, 1000))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            field.get_click(event.pos)

    screen.fill((255, 255, 255))
    field.render(screen)
    pygame.display.flip()
