import random


class AntiVirus:

    def __init__(self, HP, AP):
        self.HP = HP
        self.AP = AP
        self.radius = 1
        self.effect = 0
        self.repair = 0
        self.active = False
        self.destroyed = False

    def isActive(self):
        return self.active

    def isDestroyed(self):
        return self.destroyed

    def setActive(self):
        if not self.isDestroyed():
            self.active = True

    def getHP(self):
        return self.HP

    def attack(self, AP):
        self.HP -= AP
        if self.HP <= 0:
            self.HP = 0
            self.destroyed = True
            self.active = False

    def counterattack(self, virus):
        AP = (self.AP - virus.shield)

        if virus.shield > 0:
            if virus.shield - self.AP > 0:
                virus.shield -= self.AP
            else:
                virus.shield = 0

        virus.setHP(virus.getHP() - AP)


class AV_Kaspersky(AntiVirus):
    def __init__(self, mode_coeff, HP):
        self.basicHP = int(90 + HP)
        self.basicAP = 20
        super().__init__(self.basicHP, self.basicAP)
        self.type = 1
        self.radius = 2 * mode_coeff


class AV_Bitdefender(AntiVirus):
    def __init__(self, mode_coeff, HP):
        self.basicHP = int(60 + HP)
        self.basicAP = 40
        AP = int(self.basicAP * mode_coeff)
        super().__init__(self.basicHP, AP)
        self.type = 2


class AV_Norton(AntiVirus):
    def __init__(self, mode_coeff, HP):
        self.basicHP = int(80 + HP)
        self.basicAP = 10
        super().__init__(self.basicHP, self.basicAP)
        self.type = 3
        self.repair = int(5 * mode_coeff)


class AV_Mcafee(AntiVirus):
    def __init__(self, mode_coeff, HP):
        self.basicHP = int(60 + HP)
        self.basicAP = 15
        super().__init__(self.basicHP, self.basicAP)
        self.type = 4
        self.effect = int(5 * mode_coeff)


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

    def hackStart(self, timer):
        if not self.hacked:
            timer.start(200)

    def hackEnd(self, timer, board):
        timer.stop()
        accessibleNodes = board.accessibleNodes(self)
        for node in accessibleNodes:
            node.setAccess()
        self.setHacked()

    def moveHackProgress(self, timer, board):
        if self.isBlocked():
            timer.stop()
        else:
            self.hackProgress += 10

        if self.hackProgress == 100:
            self.hackEnd(timer, board)
        else:
            if not self.av.isDestroyed():
                avActivateChance = random.random()
                if avActivateChance >= 0.92:
                    timer.stop()
                    self.av.setActive()
                    accessibleNodes = board.accessibleNodes(self)
                    for node in accessibleNodes:
                        self.blockedList.append(node)
                        node.setBlock(True, self.av)
                    board.virus.setAP(board.virus.getAP() - self.av.effect)
                    board.activeAV.append(self.av)
                    if self.av.type == 3:
                        board.activeRepairs.append(self.av)

    def encryptedStart(self, timer):
        if not self.encrypted:
            timer.start(400)

    def encryptedEnd(self, timer, board):
        timer.stop()
        self.setEncrypted()
        if board.alarmTimerActive is False:
            avActivateChance = random.random()
            if avActivateChance >= 0.9:
                board.setAlarmTimerActive()

    def moveEncryptedProgress(self, timer, board):
        self.encryptedProgress += 5
        if self.encryptedProgress == 100:
            self.encryptedEnd(timer, board)


class Script:
    def __init__(self):
        self.usages = 1
        self.AP = 0
        self.DC = 1
        self.shield = 0
        self.RP = 0

    def setUsage(self, virus):
        if self.usages - 1 > 0:
            self.usages -= 1
        else:
            virus.activescript[self.__class__] = None

    def addActiveScript(self, virus):
        virus.activeScripts[self.__class__] = self


class WormScript(Script):
    def __init__(self):
        super().__init__()
        self.shield = 40


class TrojanScript(Script):
    def __init__(self):
        super().__init__()
        self.usages = 3
        self.RP = 20


class LogicBombScript(Script):
    def __init__(self):
        super().__init__()
        self.DC = 2


class ExploitScript(Script):
    def __init__(self):
        super().__init__()
        self.usages = 3
        self.AP = 15


class Virus:
    def __init__(self):
        self.script = Script()
        self.hp = 150
        self.ap = 30 * self.script.DC
        self.shield = 0
        self.activeScripts = {
            WormScript: None,
            TrojanScript: None,
            LogicBombScript: None,
            ExploitScript: None
        }

    def getHP(self):
        return self.hp

    def setHP(self, hp):
        self.hp = hp

    def getAP(self):
        return self.ap

    def setAP(self, ap):
        self.AP = ap

    def setActiveWormScript(self):
        if self.activeScripts.get(WormScript) is None:
            self.activeScripts[WormScript] = 1
        else:
            self.activeScripts[WormScript] += 1

    def setActiveTrojanScript(self):
        if self.activeScripts.get(TrojanScript) is None:
            self.activeScripts[TrojanScript] = 1
        else:
            self.activeScripts[TrojanScript] += 1

    def setActiveLogicBombScript(self):
        if self.activeScripts.get(LogicBombScript) is None:
            self.activeScripts[LogicBombScript] = 1
        else:
            self.activeScripts[LogicBombScript] += 1

    def setActiveExploitScript(self):
        if self.activeScripts.get(ExploitScript) is None:
            self.activeScripts[ExploitScript] = 1
        else:
            self.activeScripts[ExploitScript] += 1

    def attackNode(self, node, board):
        attackBonus = 0
        for script in self.activeScripts.values():
            if script is None:
                continue
            attackBonus += (node.av.getHP() // int(script.DC)) + script.AP
            self.hp += script.RP
            self.shield = script.shield
            script.setUsage(self)
        av = node.getAV()
        av.attack(self.ap + attackBonus)
        if av.isDestroyed():
            self.ap += av.effect
            for blockedNode in node.blockedList:
                blockedNode.setBlock(False, av)
            node.blockedList.clear()
            if av in board.activeAV:
                board.activeAV.remove(av)
            if av in board.activeRepairs:
                board.activeRepairs.remove(av)
        else:
            av.counterattack(self)
            for rep in board.activeRepairs:
                for av in board.activeAV:
                    if av.getHP() < av.basicHP * 2:
                        av.HP = min(rep.repair + av.HP, av.basicHP * 2)
