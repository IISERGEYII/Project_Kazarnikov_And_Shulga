import pygame
import os
import random

PROGRESS_HACK = pygame.USEREVENT + 1
PROGRESS_ENCRYPT = pygame.USEREVENT + 1

class Node:

    def __init__(self, row, col, mode_coeff, HP):
        self.row = row
        self.col = col
        self.hacked = False
        self.encrypted = False
        self.access = False
        self.hackProgress = 0
        self.encryptedProgress = 0
        self.isBlockedByList = []
        self.blockedList = []
        self.main = False
        self.phase_node = 1

    #        self.__initAV(mode_coeff, HP)

    #    def __initAV(self, mode_coeff, HP):
    #        random.seed()
    #        avType = random.randrange(1, 5)
    #        if avType == 1:
    #            self.av = AV_Kaspersky(mode_coeff, HP)
    #        elif avType == 2:
    #            self.av = AV_Bitdefender(mode_coeff, HP)
    #        elif avType == 3:
    #            self.av = AV_Norton(mode_coeff, HP)
    #        elif avType == 4:
    #            self.av = AV_Mcafee(mode_coeff, HP)

    def getAV(self):
        return self.av

    def getTypeAV(self):
        return self.av.type

    def isHacked(self):
        return self.hacked

    def isEncrypted(self):
        return self.encrypted

    def isBlocked(self):
        return bool(len(self.isBlockedByList))

    def isAccess(self):
        return self.access

    def isMain(self):
        return self.main

    def setBlock(self, blockFlag, av):
        if blockFlag is True:
            self.isBlockedByList.append(av)
        else:
            self.isBlockedByList.remove(av)

    def setAccess(self):
        self.access = True

    def setMain(self):
        self.main = True

    def setHacked(self):
        self.hacked = True

    #       self.av.hp = 0

    def setEncrypted(self):
        self.encrypted = True

    def avActive(self):
        return self.av.isActive()


class Board:
    def __init__(self, params):
        self.rows = params.get("rows")
        self.cols = params.get("cols")
        self.mode_coeff = params.get("mode_coeff")
        self.HP = params.get("HP")
        self.__initNodes()
        #        self.virus = Virus()
        self.alarmTimerActive = False
        self.list_picture_number = []
        self.activeAV = []
        self.activeRepairs = []

    def __initNodes(self):
        random.seed()
        self.nodeList = [[Node(i, j, self.mode_coeff, self.HP) for j in range(self.cols)] for i in range(self.rows)]

        startCol = 0
        selectSet = list(range(self.rows))

        while startCol < self.cols:
            startRow = random.choice(selectSet)
            startNode = self.getNodeByIndex(startRow, startCol)
            if startNode is None:
                selectSet.remove(startRow)
                if len(selectSet) == 0:
                    startCol += 1
                    selectSet = list(range(self.rows))
            else:
                break

        startNode.setAccess()
        startNode.setHacked()
        startNode.hackProgress = 100
        startNode.encryptedProgress = 100
        accessibleNodes = self.accessibleNodes(startNode)
        for node in accessibleNodes:
            node.setAccess()

        nodeNumbers = []
        for i in range(self.rows):

            for j in range(self.cols - 1, self.cols - 1 - i, -1):
                number = i * self.rows + j
                nodeNumbers.append(number)

        mainNodeNumber = random.choice(nodeNumbers)
        mainNode = self.nodeList[mainNodeNumber // self.rows][mainNodeNumber % self.cols]
        mainNode.setMain()

    def getNodeByIndex(self, row, col):
        return self.nodeList[row][col]

    def accessibleNodes(self, node, radius=1):
        accessibleNodes = []

        for i in range(1, radius + 1):

            if node.row + i < self.rows:
                near_node = self.getNodeByIndex(node.row + i, node.col)
                accessibleNodes.append(near_node)

            if node.row - i >= 0:
                near_node = self.getNodeByIndex(node.row - i, node.col)
                accessibleNodes.append(near_node)

            if node.col + i < self.cols:
                near_node = self.getNodeByIndex(node.row, node.col + i)
                accessibleNodes.append(near_node)

            if node.col - i >= 0:
                near_node = self.getNodeByIndex(node.row, node.col - i)
                accessibleNodes.append(near_node)

        return accessibleNodes

    def attackNode(self, attackNode):
        self.virus.attackNode(attackNode, self)

    def endGame(self):
        pass

    def setAlarmTimerActive(self):
        self.alarmTimerActive = True

    def getScores(self):
        scores = 0
        for nodes in self.nodeList:
            for node in nodes:
                if node.isEncrypted():
                    if node.isMain():
                        scores += 3000
                    else:
                        scores += 50
        return scores


class The_playing_field:
    def __init__(self, width, height, params):
        self.width = width
        self.height = height
        self.board = Board(params)
        self.left = 10
        self.top = 10
        self.cell_size = 100
        self.all_sprites = pygame.sprite.Group()

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        square = pygame.Rect(10, 10, self.cell_size, self.cell_size)
        hacker_bar = pygame.Rect(12, 12, 20, 50)
        encrypted_bar = pygame.Rect(88, 12, 20, 50)
        hp_bar = pygame.Rect(15, 98, 90, 10)
        for i in range(self.height):
            for j in range(self.width):

                pygame.draw.rect(screen, "black", square.move(j * self.cell_size, i * self.cell_size), width=1)
                pygame.draw.rect(screen, "green", hacker_bar.move(j * self.cell_size, i * self.cell_size), width=1)
                pygame.draw.rect(screen, "green", encrypted_bar.move(j * self.cell_size, i * self.cell_size),
                                 width=1)
                pygame.draw.rect(screen, "red", hp_bar.move(j * self.cell_size, i * self.cell_size))
                if self.board.nodeList[i][j].phase_node == 1:
                    image = self.load_image("node_protect.png")
                    image_rect = image.get_rect(
                        bottomright=((j + 1) * self.cell_size - 15, (i + 1) * self.cell_size - 20))
                    screen.blit(image, image_rect)
                elif self.board.nodeList[i][j].phase_node == 2:
                    image = self.load_image("node_hacked.png")
                    image_rect = image.get_rect(
                        bottomright=((j + 1) * self.cell_size - 15, (i + 1) * self.cell_size - 20))
                    screen.blit(image, image_rect)
                    pygame.draw.rect(screen, "green", hacker_bar.move(j * self.cell_size, i * self.cell_size))
                elif self.board.nodeList[i][j].phase_node == 3:
                    image = self.load_image("encrypted.png")
                    image_rect = image.get_rect(
                        bottomright=((j + 1) * self.cell_size - 15, (i + 1) * self.cell_size - 20))
                    screen.blit(image, image_rect)
                    pygame.draw.rect(screen, "green", hacker_bar.move(j * self.cell_size, i * self.cell_size))
                    pygame.draw.rect(screen, "green",
                                     encrypted_bar.move(j * self.cell_size, i * self.cell_size))

    def phase_change(self, node, x, y):
        phase = node.phase_node
        if phase == 3:
            return 3
        if phase == 1:

            pygame.time.set_timer(PROGRESS_HACK, 1000)
            return node
        elif phase == 2:
            progress = 0
            clock = pygame.time.Clock()
            while progress <= 10:
                progress_encrypted_bar = pygame.Rect(88, 12, 20, progress * 5)
                pygame.draw.rect(screen, "green", progress_encrypted_bar.move(y * self.cell_size, x * self.cell_size))
                progress += 10 * clock.tick() / 1000
                pygame.display.flip()
            phase += 1
            return phase

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        i, j = (y - self.top) // self.cell_size, \
               (x - self.left) // self.cell_size
        return i, j

    def on_click(self, cell_coords):
        if cell_coords is not None:
            i, j = cell_coords
            self.board.nodeList[i][j] = self.phase_change(self.board.nodeList[i][j], i, j)

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

    def initializing_the_node_phase(self, i, j, node):
        if node == 3:
            return
        self.board[i][j] = node + 1


fps = 20
clock = pygame.time.Clock()
init_param = {"rows": 10, "cols": 10, "mode_coeff": 1.5, "HP": 60}
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
        if event.type == PROGRESS_HACK:
            print("работает")

    screen.fill((255, 255, 255))
    field.render(screen)
    pygame.display.flip()
    clock.tick(fps)
