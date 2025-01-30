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
        self.__initAV(mode_coeff, HP)

    def __initAV(self, mode_coeff, HP):
        random.seed()
        avType = random.randrange(1, 5)
        if avType == 1:
            self.av = AV_Kaspersky(mode_coeff, HP)
        elif avType == 2:
            self.av = AV_Bitdefender(mode_coeff, HP)
        elif avType == 3:
            self.av = AV_Norton(mode_coeff, HP)
        elif avType == 4:
            self.av = AV_Mcafee(mode_coeff, HP)

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
        self.av.hp = 0

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
        self.virus = Virus()
        self.alarmTimerActive = False
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
