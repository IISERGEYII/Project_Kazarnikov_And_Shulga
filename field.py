from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QProgressBar, QHBoxLayout, QLCDNumber, \
    QDialog, QVBoxLayout, QApplication
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QPixmap, QIcon
from board import *
import sys


class The_playing_field(QWidget):

    def __init__(self):
        super().__init__()
        self.init_param = {"rows": 10, "cols": 10, "mode_coeff": 1.5, "HP": 60}
        self.board = Board(self.init_param)
        self.nodes = {}
        self.timers = {}
        self.icons = {}
        self.btns = {}
        self.mainGroup = QVBoxLayout(self)
        self.initIcons()
        self.timerLayout()
        self.initUI()
        self.equipment_layout()
        self.victory = False

    def initUI(self):
        self.setGeometry(100, 50, 500, 500)
        self.setStyleSheet("""
        QProgressBar {
            border-style: solid;
            border-color: grey;
            border-radius: 4px;
            border-width: 2px;
            text-align: center;
        }
        """)
        self.setWindowTitle("Игровое поле")
        boardGroup = QGridLayout(self)
        nodes = self.board.nodeList
        for i in range(self.board.rows):
            for j in range(self.board.cols):
                node = nodes[i][j]
                if node is None:
                    continue
                fields_layout = self.create_node_layout(node)
                boardGroup.addLayout(fields_layout, i, j)

                btn = self.get_widget(boardGroup.itemAtPosition(i, j), 0, 1)
                self.btns[btn] = node
                timer_hk = QTimer()
                timer_hk.timeout.connect(self.timeoutHack)
                self.timers[timer_hk] = node
                timer_en = QTimer()
                timer_en.timeout.connect(self.timeoutEncrypted)
                self.timers[timer_en] = node

                dict_node = {"hackBar": self.get_widget(boardGroup.itemAtPosition(i, j), 0, 0),
                             "encryptionBar": self.get_widget(boardGroup.itemAtPosition(i, j), 0, 2),
                             "hpBar": self.get_widget(boardGroup.itemAtPosition(i, j), 1, 0),
                             "timer_hk": timer_hk, "btn": btn, "timer_en": timer_en}
                self.nodes[node] = dict_node
        self.setIcons()
        self.mainGroup.addLayout(boardGroup)

    def timerLayout(self):
        timerGroup = QHBoxLayout(self)
        self.lcd_number = QLCDNumber(self)
        self.lcd_number.setFixedSize(1000, 50)
        self.end_timer = QTimer(self)
        self.end_timer.timeout.connect(self.timeout_end)
        self.end_time = int(60 * (2 - self.init_param.get("mode_coeff")))
        self.lcd_number.display(self.end_time)
        timerGroup.addWidget(self.lcd_number)
        self.mainGroup.addLayout(timerGroup)

    def initIcons(self):
        icon_node_pr = QIcon()
        icon_node_pr.addPixmap(QPixmap("./res/icons/node_protect.png"))
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

    def equipment_layout(self):
        equipment = QHBoxLayout(self)

        self.virusHPLCD = QLCDNumber()
        equipment.addWidget(self.virusHPLCD)

        self.virusAPLCD = QLCDNumber()
        equipment.addWidget(self.virusAPLCD)

        icon_button_shield = QIcon()
        icon_button_shield.addPixmap(QPixmap("./res/icons/mcaffee.png"))
        self.worm_script = QPushButton(self)
        self.worm_script.setVisible(False)
        self.worm_script.setIcon(icon_button_shield)
        self.worm_script.clicked.connect(self.board.virus.setActiveWormScript)
        equipment.addWidget(self.worm_script)
        self.trojan_script = QPushButton(self)
        self.trojan_script.setVisible(False)
        self.trojan_script.setIcon(icon_button_shield)
        self.trojan_script.clicked.connect(self.board.virus.setActiveTrojanScript)
        equipment.addWidget(self.trojan_script)
        self.logic_bomb_script = QPushButton(self)
        self.logic_bomb_script.setVisible(False)
        self.logic_bomb_script.setIcon(icon_button_shield)
        self.logic_bomb_script.clicked.connect(self.board.virus.setActiveLogicBombScript)
        equipment.addWidget(self.logic_bomb_script)
        self.exploit_script = QPushButton(self)
        self.exploit_script.setVisible(False)
        self.exploit_script.setIcon(icon_button_shield)
        self.exploit_script.clicked.connect(self.board.virus.setActiveExploitScript)
        equipment.addWidget(self.exploit_script)
        self.mainGroup.addLayout(equipment)
        self.updateIndicators()

    def updateIndicators(self):
        self.virusHPLCD.display(self.board.virus.getHP())
        self.virusAPLCD.display(self.board.virus.getAP())

    def updateHProgressBar(self, node=None):

        if node is None:
            for node, nodeUI in self.nodes.items():
                if not node.avActive():
                    continue
                hpBar = nodeUI.get("hpBar")
                hpBar.setValue(node.av.getHP())

        else:
            hpBar = self.nodes.get(node).get("hpBar")
            hpBar.setValue(node.av.getHP())

    def setIcons(self):
        for btn, node in self.btns.items():
            if node.isAccess():
                if node.isHacked():
                    if node.isEncrypted():
                        icon = self.icons.get(6)
                    else:
                        if node.isMain():
                            icon = self.icons.get(4)
                        else:
                            icon = self.icons.get(2)
                else:
                    if node.avActive():
                        icon = self.getAvIcon(node)
                    else:
                        if node.isBlocked():
                            icon = self.icons.get(5)
                        else:
                            if node.isMain():
                                icon = self.icons.get(3)
                            else:
                                icon = self.icons.get(1)
            else:
                icon = self.icons.get(11)

            if icon is None:
                icon = self.icons.get(12)

            btn.setIcon(icon)

    def create_btn(self):
        btn = QPushButton(self)
        btn.setFixedSize(50, 50)
        iconsize = QSize(50, 50)
        btn.setIconSize(iconsize)
        btn.clicked.connect(self.clicked_btn)

        return btn

    def create_vprogres_bar(self):
        bar = QProgressBar(self)
        bar.setFixedSize(20, 50)
        bar.setOrientation(Qt.Orientation.Vertical)
        return bar

    def create_hprogres_bar(self, node):
        bar = QProgressBar(self)
        bar.setFormat("%v")
        bar.setMaximum(node.av.getHP() * 2)
        bar.setFixedSize(100, 20)
        return bar

    def create_node_layout(self, node):
        grid_layout = QGridLayout(self)

        btn = self.create_btn()
        progres_hacking_bar = self.create_vprogres_bar()
        progres_encryption_bar = self.create_vprogres_bar()
        hp_bar = self.create_hprogres_bar(node)
        grid_layout.addWidget(progres_hacking_bar, 0, 0)

        grid_layout.addWidget(btn, 0, 1)
        grid_layout.addWidget(progres_encryption_bar, 0, 2)
        grid_layout.addWidget(hp_bar, 1, 0, 1, -1)

        return grid_layout

    def get_widget(self, layout, x, y):
        return layout.itemAtPosition(x, y).widget()

    def timeoutHack(self):
        timer = self.sender()
        node = self.timers.get(timer)
        node.moveHackProgress(timer, self.board)
        hackBar = self.nodes.get(node).get('hackBar')
        hackBar.setValue(node.hackProgress)

        if not timer.isActive():
            self.setIcons()
            self.updateHProgressBar(node)

    def timeoutEncrypted(self):
        timer = self.sender()
        node = self.timers.get(timer)
        node.moveEncryptedProgress(timer, self.board)
        encryptedBar = self.nodes.get(node).get('encryptionBar')
        encryptedBar.setValue(node.encryptedProgress)

        if not timer.isActive():
            self.setIcons()
            if node.isMain() is True:
                self.end_game()
            if self.board.alarmTimerActive:
                self.startEndTimer()

    def timeout_end(self):
        self.progressEnd()

    def clicked_btn(self):
        btn = self.sender()
        node = self.btns.get(btn)

        if not node.isAccess():
            return

        if node.isEncrypted():
                return

        if node.isBlocked():
            return

        if node.isHacked():
            self.startEncrypt(node)

        if node.avActive():
            self.attackAV(node)
            if self.board.virus.getHP() <= 0:
                self.end_game()
        else:
            self.startHack(node)
        self.setIcons()

    def getAvIcon(self, node):
        type_AV = node.av.type
        if type_AV == 1:
            return self.icons.get(7)
        if type_AV == 2:
            return self.icons.get(8)
        if type_AV == 3:
            return self.icons.get(9)
        if type_AV == 4:
            return self.icons.get(10)

    def attackAV(self, node):
        self.board.attackNode(node)
        self.updateIndicators()
        self.updateHProgressBar()

    def startHack(self, node):
        timer = self.nodes[node].get("timer_hk")
        node.hackStart(timer)

    def startEncrypt(self, node):
        timer = self.nodes[node].get("timer_en")
        node.encryptedStart(timer)

    def startEndTimer(self):
        self.end_timer.start(1000)
        self.timeout_end()

    def end_game(self):
        if self.end_timer.isActive():
            self.end_timer.stop()
        self.close()

    def closeEvent(self, a0):
        self.main_widget.addPoints(self.board.getScores())
    def progressEnd(self):
        self.end_time -= 1
        self.lcd_number.display(self.end_time)
        if self.end_time == 0:
            self.end_game()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = The_playing_field()
    ex.show()
    sys.exit(app.exec())
