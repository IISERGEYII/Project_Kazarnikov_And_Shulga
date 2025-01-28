import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from field import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 481)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(510, 220, 481, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.cost_damage_level = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.cost_damage_level.setObjectName("cost_damage_level")
        self.gridLayout.addWidget(self.cost_damage_level, 4, 3, 1, 1)

        self.cost_XP_level = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.cost_XP_level.setObjectName("cost_XP_level")
        self.gridLayout.addWidget(self.cost_XP_level, 3, 3, 1, 1)

        self.buy_XP_level_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.buy_XP_level_button.setObjectName("buy_XP_level_button")
        self.gridLayout.addWidget(self.buy_XP_level_button, 3, 0, 1, 1)

        self.buy_stealth_en_level_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.buy_stealth_en_level_button.setObjectName("buy_stealth_en_level_button")
        self.gridLayout.addWidget(self.buy_stealth_en_level_button, 2, 0, 1, 1)

        self.cost_hk_speed_level = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.cost_hk_speed_level.setObjectName("cost_hk_speed_level")
        self.gridLayout.addWidget(self.cost_hk_speed_level, 1, 3, 1, 1)

        self.buy_damage_level_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.buy_damage_level_button.setObjectName("buy_damage_level_button")
        self.gridLayout.addWidget(self.buy_damage_level_button, 4, 0, 1, 1)

        self.buy_hk_speed_level_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.buy_hk_speed_level_button.setObjectName("buy_hk_speed_level_button")
        self.gridLayout.addWidget(self.buy_hk_speed_level_button, 1, 0, 1, 1)

        self.level_hk_speed = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.level_hk_speed.setObjectName("level_hk_speed")
        self.gridLayout.addWidget(self.level_hk_speed, 1, 2, 1, 1)

        self.level_XP = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.level_XP.setObjectName("level_XP")
        self.gridLayout.addWidget(self.level_XP, 3, 2, 1, 1)

        self.level_stealth_en = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.level_stealth_en.setObjectName("level_stealth_en")
        self.gridLayout.addWidget(self.level_stealth_en, 2, 2, 1, 1)

        self.level_damage = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.level_damage.setObjectName("level_damage")
        self.gridLayout.addWidget(self.level_damage, 4, 2, 1, 1)

        self.cost_stealth_en_level = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.cost_stealth_en_level.setObjectName("cost_stealth_en_level")
        self.gridLayout.addWidget(self.cost_stealth_en_level, 2, 3, 1, 1)

        self.label_14 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 1, 1, 1)

        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.label_10 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_12 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 1, 1, 1)

        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)

        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 111, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_9 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)

        self.easy_complexity_rb = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.easy_complexity_rb.setObjectName("easy_complexity_rb")
        self.easy_complexity_rb.click()
        self.verticalLayout.addWidget(self.easy_complexity_rb)

        self.medium_complexity_rb = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.medium_complexity_rb.setObjectName("medium_complexity_rb")
        self.verticalLayout.addWidget(self.medium_complexity_rb)

        self.heavy_complexity_rb = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.heavy_complexity_rb.setObjectName("heavy_complexity_rb")
        self.verticalLayout.addWidget(self.heavy_complexity_rb)

        self.generate_field_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.generate_field_button.setGeometry(QtCore.QRect(110, 80, 331, 101))
        self.generate_field_button.setObjectName("generate_field_button")

        self.save_progress_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_progress_button.setGeometry(QtCore.QRect(0, 10, 121, 21))
        self.save_progress_button.setObjectName("save_progress_button")

        self.loading_last_game_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loading_last_game_button.setGeometry(QtCore.QRect(120, 10, 151, 21))
        self.loading_last_game_button.setObjectName("loading_last_game_button")

        self.player_choise_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.player_choise_button.setGeometry(QtCore.QRect(920, 0, 101, 23))
        self.player_choise_button.setObjectName("player_choise_button")

        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(803, 190, 151, 23))
        self.lcdNumber.setObjectName("lcdNumber")

        self.label_22 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(686, 193, 91, 20))
        self.label_22.setObjectName("label_22")

        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 220, 501, 151))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.buy_reconstruction_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.buy_reconstruction_button.setObjectName("buy_reconstruction_button")
        self.gridLayout_3.addWidget(self.buy_reconstruction_button, 2, 1, 1, 1)

        self.buy_double_damage_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.buy_double_damage_button.setObjectName("buy_double_damage_button")
        self.gridLayout_3.addWidget(self.buy_double_damage_button, 3, 1, 1, 1)

        self.buy_shield_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.buy_shield_button.setObjectName("buy_shield_button")
        self.gridLayout_3.addWidget(self.buy_shield_button, 1, 1, 1, 1)

        self.label_24 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 0, 4, 1, 1)

        self.label_23 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 0, 3, 1, 1)

        self.label_15 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 2, 1, 1)

        self.buy_momentary_damage_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.buy_momentary_damage_button.setObjectName("buy_momentary_damage_button")
        self.gridLayout_3.addWidget(self.buy_momentary_damage_button, 4, 1, 1, 1)

        self.name_1 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.name_1.setObjectName("name_1")
        self.gridLayout_3.addWidget(self.name_1, 1, 2, 1, 1)

        self.name_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.name_2.setObjectName("name_2")
        self.gridLayout_3.addWidget(self.name_2, 2, 2, 1, 1)

        self.name_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.name_3.setObjectName("name_3")
        self.gridLayout_3.addWidget(self.name_3, 3, 2, 1, 1)

        self.name_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.name_4.setObjectName("name_4")
        self.gridLayout_3.addWidget(self.name_4, 4, 2, 1, 1)

        self.count_shield = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.count_shield.setObjectName("count_shield")
        self.gridLayout_3.addWidget(self.count_shield, 1, 3, 1, 1)

        self.count_reconstruction = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.count_reconstruction.setObjectName("count_reconstruction")
        self.gridLayout_3.addWidget(self.count_reconstruction, 2, 3, 1, 1)

        self.count_double_damage = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.count_double_damage.setObjectName("count_double_damage")
        self.gridLayout_3.addWidget(self.count_double_damage, 3, 3, 1, 1)

        self.count_momentary_damage = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.count_momentary_damage.setObjectName("count_momentary_damage")
        self.gridLayout_3.addWidget(self.count_momentary_damage, 4, 3, 1, 1)

        self.cost_shield = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.cost_shield.setObjectName("cost_shield")
        self.gridLayout_3.addWidget(self.cost_shield, 1, 4, 1, 1)

        self.cost_reconstruction = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.cost_reconstruction.setObjectName("cost_reconstruction")
        self.gridLayout_3.addWidget(self.cost_reconstruction, 2, 4, 1, 1)

        self.cost_double_damage = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.cost_double_damage.setObjectName("cost_double_damage")
        self.gridLayout_3.addWidget(self.cost_double_damage, 3, 4, 1, 1)

        self.cost_momentary_damage = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.cost_momentary_damage.setObjectName("cost_momentary_damage")
        self.gridLayout_3.addWidget(self.cost_momentary_damage, 4, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cost_damage_level.setText(_translate("MainWindow", "1000"))
        self.cost_XP_level.setText(_translate("MainWindow", "1000"))
        self.buy_XP_level_button.setText(_translate("MainWindow", "Купить"))
        self.buy_stealth_en_level_button.setText(_translate("MainWindow", "Купить"))
        self.cost_hk_speed_level.setText(_translate("MainWindow", "1000"))
        self.buy_damage_level_button.setText(_translate("MainWindow", "Купить"))
        self.buy_hk_speed_level_button.setText(_translate("MainWindow", "Купить"))
        self.level_hk_speed.setText(_translate("MainWindow", "1"))
        self.level_XP.setText(_translate("MainWindow", "1"))
        self.level_stealth_en.setText(_translate("MainWindow", "1"))
        self.level_damage.setText(_translate("MainWindow", "1"))
        self.cost_stealth_en_level.setText(_translate("MainWindow", "1000"))
        self.label_14.setText(_translate("MainWindow", "Урон вируса"))
        self.label.setText(_translate("MainWindow", "Скорость взлома"))
        self.label_10.setText(_translate("MainWindow", "Заметность шифровки"))
        self.label_12.setText(_translate("MainWindow", "Здоровье вируса"))
        self.label_4.setText(_translate("MainWindow", "Уровень (максимум 5)"))
        self.label_5.setText(_translate("MainWindow", "Стоимость в очках"))
        self.label_3.setText(_translate("MainWindow", "Улучшение"))
        self.label_9.setText(_translate("MainWindow", "Уровень сложности:"))
        self.easy_complexity_rb.setText(_translate("MainWindow", "Лёгкий"))
        self.medium_complexity_rb.setText(_translate("MainWindow", "Средний"))
        self.heavy_complexity_rb.setText(_translate("MainWindow", "Тяжёлый"))
        self.generate_field_button.setText(_translate("MainWindow", "Сгенерировать уровень"))
        self.save_progress_button.setText(_translate("MainWindow", "Сохранить прогресс"))
        self.loading_last_game_button.setText(_translate("MainWindow", "Загрузить последнию игру"))
        self.player_choise_button.setText(_translate("MainWindow", "Выбор игрока"))
        self.label_22.setText(_translate("MainWindow", "Очков сейчас:"))
        self.buy_reconstruction_button.setText(_translate("MainWindow", "Купить"))
        self.buy_double_damage_button.setText(_translate("MainWindow", "Купить"))
        self.buy_shield_button.setText(_translate("MainWindow", "Купить"))
        self.label_24.setText(_translate("MainWindow", "Стоимость в очках"))
        self.label_23.setText(_translate("MainWindow", "Количество снарежение (Максимум 5)"))
        self.label_15.setText(_translate("MainWindow", "Снарежение"))
        self.buy_momentary_damage_button.setText(_translate("MainWindow", "Купить"))
        self.name_1.setText(_translate("MainWindow", "Защитное поле"))
        self.name_2.setText(_translate("MainWindow", "Реконструкция"))
        self.name_3.setText(_translate("MainWindow", "Двйоной урон"))
        self.name_4.setText(_translate("MainWindow", "Моментальный урон"))
        self.count_shield.setText(_translate("MainWindow", "0"))
        self.count_reconstruction.setText(_translate("MainWindow", "0"))
        self.count_double_damage.setText(_translate("MainWindow", "0"))
        self.count_momentary_damage.setText(_translate("MainWindow", "0"))
        self.cost_shield.setText(_translate("MainWindow", "500"))
        self.cost_reconstruction.setText(_translate("MainWindow", "600"))
        self.cost_double_damage.setText(_translate("MainWindow", "1000"))
        self.cost_momentary_damage.setText(_translate("MainWindow", "1200"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.points = 0
        self.lcdNumber.display(self.points)
        self.init_param = {"rows": 5, "cols": 5, "mode_coeff": 0.5, "HP": 0}
        self.generate_field_button.clicked.connect(self.startGame)
        self.easy_complexity_rb.clicked.connect(self.easyMode)
        self.medium_complexity_rb.clicked.connect(self.mediumMode)
        self.heavy_complexity_rb.clicked.connect(self.heavyMode)

    def easyMode(self):
        self.init_param = {"rows": 5, "cols": 5, "mode_coeff": 0.5, "HP": 0}

    def mediumMode(self):
        self.init_param = {"rows": 8, "cols": 8, "mode_coeff": 1, "HP": 30}

    def heavyMode(self):
        self.init_param = {"rows": 10, "cols": 10, "mode_coeff": 1.5, "HP": 60}

    def startGame(self):
        self.boardWindow = The_playing_field(self, self.init_param)
        self.boardWindow.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        self.boardWindow.show()

    def setParam(self):
        return self.init_param

    def addPoints(self, points):
        self.points += points
        self.lcdNumber.display(self.points)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
