from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from screeninfo import get_monitors
from SoPNv_Farm_bot import *
import pygetwindow
from ShanerBot import AutoAttack as Autos
from ShanerBot import Check_if_Killed as CiK
from ShanerBot import Move, Target, PickUp, Heal, Back, Check_if_CP, Check_if_Boss, Check_if_Pet
from MultiClient import open_Nostale

WIDTH = int((get_monitors()[0].width-650)/2)
HEIGHT = int((get_monitors()[0].height-500)/2)

def Check_if_in_game():
    x = pygetwindow.getActiveWindow()
    if x is None:
        x = "xxx"
        return x
    else:
        return x.title

class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setWindowTitle("AutoNos")
        self.setGeometry(WIDTH,HEIGHT,650,500)
        self.setFixedSize(self.size())
        self.UiComponents()

    def UiComponents(self):
        self.SoPNv = QPushButton("SoP Nsvl Farm",self)
        self.SoPNv.setGeometry(75,50,200,50)
        self.ShanerBot = QPushButton("Shaner Bot",self)
        self.ShanerBot.setGeometry(75,100,200,50)
        self.Shaner_config()
        self.IC_Bot = QPushButton("IC Bot",self)
        self.IC_Bot.setGeometry(75,150,200,50)
        self.IC_config()
        self.SoPNv.clicked.connect(self.SoPNv_clicked)
        self.ShanerBot.clicked.connect(self.Shaner_config_show)
        self.IC_Bot.clicked.connect(self.IC_config_show)

    def ShanerBot_clicked(self):
        self.hide()
        cnt = 0
        time.sleep(2)
        dir = "up"
        while True:
            if Check_if_in_game() == "NosTale":
                Target()
                if keyboard.is_pressed('q'):
                    break
                elif CiK() == 3352:
                    Autos()
                    cnt = 0
                elif CiK() != 3352:
                    Heal(self.Heal_Bind)
                    dir, cnt = Back(cnt, dir, self.Back_Bind)
                    cnt += 1
                    dir = Move(dir)
                if Check_if_Boss() == 17666:
                    pyautogui.press('esc')
                    time.sleep(0.2)
                if Check_if_CP() == 2555:
                    for i in range(3):
                        pyautogui.press('esc')
                if Check_if_Pet() == 13734:
                    pyautogui.press('esc')
                    pyautogui.press('d')
                    time.sleep(0.3)
            elif keyboard.is_pressed('q'):
                break
        self.show()

    def SoPNv_clicked(self):
        self.hide()
        time.sleep(2)
        pyautogui.press('esc')
        while(True):
            if Check_if_in_game() == "NosTale":
                if keyboard.is_pressed('q'):
                    break
                elif Check_if_low_hp() != 10838:
                    time.sleep(35)
                else:
                    Auto_Attack_and_Pick_up()
            elif keyboard.is_pressed('q'):
                break
        self.show()

    def IC_clicked(self):
        self.IC_slot.append(self.IC_slot1.currentIndex())
        self.IC_slot.append(self.IC_slot2.currentIndex())
        for slot in set(self.IC_slot):
            try:
                if slot != "  ":
                    open_Nostale(slot)
            except:
                continue
        self.IC_slot.clear()

    def Config_Label(self, title = "Info"):
        title = str(title)
        BotConfig = QLabel(title,self)
        BotConfig.setGeometry(350,20,260,440)
        BotConfig.setStyleSheet("background-image: url(background_by_pikisuperstar.jpg); color: black; font: bold 18px; border: 1px solid black;")
        BotConfig.setAlignment(Qt.AlignHCenter)
        BotConfig.hide()
        return BotConfig
    
    def IC_config(self):
        self.IC_slot = []
        self.IC_label = self.Config_Label("IC Bot")
        self.IC_label1 = QLabel("Number of accounts:",self)
        self.IC_label1.setGeometry(370,50,120,20)
        self.IC_label2 = QLabel("GF slots:",self)
        self.IC_label2.setGeometry(370,100,120,20)

        ###ACC_NUMBER###
        self.IC_acc_number = QComboBox(self)
        for i in range(3):
            self.IC_acc_number.addItem(str(i))
        self.IC_acc_number.setGeometry(370,70,40,20)
        ################

        ###GF SLOTS###
        self.IC_slot1 = QComboBox(self)
        self.IC_slot1.addItem("  ")
        for i in range(1,5):
            self.IC_slot1.addItem(str(i))
        self.IC_slot1.setGeometry(370,120,40,20)
        self.IC_slot2 = QComboBox(self)
        self.IC_slot2.addItem("  ")
        for i in range(1,5):
            self.IC_slot2.addItem(str(i))
        self.IC_slot2.setGeometry(370,140,40,20)
        ############

        ###IMG###
        self.IC_tut = QLabel(self)
        pixmap = QPixmap("Tut1.png")
        pixmap2 = pixmap.scaled(180,100)
        self.IC_tut.setPixmap(pixmap2)
        self.IC_tut.setGeometry(425,100,180,100)
        #########

        ###START###
        self.IC_Start = QPushButton("Start",self)
        self.IC_Start.setGeometry(440,200,80,40)
        self.IC_Start.clicked.connect(self.IC_clicked)
        ###########

        ###HIDES###
        self.IC_tut.hide()
        self.IC_Start.hide()
        self.IC_label2.hide()
        self.IC_label1.hide()
        self.IC_acc_number.hide()
        self.IC_slot1.hide()
        self.IC_slot2.hide()
        ###########

        self.IC_acc_number.activated.connect(self.Acc_number_choose)

    def Acc_number_choose(self,index):
        if index == 0:
            self.IC_slot.clear()
            self.IC_tut.hide()
            self.IC_label2.hide()
            self.IC_slot1.hide()
            self.IC_slot2.hide()
        elif index == 1:
            self.IC_slot.clear()
            self.IC_tut.show()
            self.IC_slot1.setCurrentText("  ")
            self.IC_label2.show()
            self.IC_slot1.show()
            self.IC_slot2.hide()
        elif index == 2:
            self.IC_slot.clear()
            self.IC_slot1.setCurrentText("  ")
            self.IC_slot2.setCurrentText("  ")
            self.IC_tut.show()
            self.IC_label2.show()
            self.IC_slot1.show()
            self.IC_slot2.show()

    def IC_slot_choose(self,index):
        self.IC_slot.append(index)


        #### Shaner Bot settings window####
    def Shaner_config(self):
        self.Shaner_label = self.Config_Label("Shaner Bot")

        ###SP CHOOSE###
        self.label = QLabel("SP:",self)
        self.label.setGeometry(370,50,20,20)
        self.SP_List = QComboBox(self)
        self.SP_List.setGeometry(370,70,50,50)
        self.SP_List.addItem("   ")
        self.SP_List.addItem(QIcon("cruss.png"),"Cruss") ###Cruss - index:1
        self.SP_List.addItem("WK") ###WK - index:2
        self.SP_List.adjustSize()
        #########
    
        ###Img###
        self.AoR = QLabel(self)
        pixmap = QPixmap("AoR.png")
        pixmap2 = pixmap.scaled(20,20)
        self.AoR.setPixmap(pixmap2)
        self.AoR.setGeometry(440,115,30,30)       
        ###Img###

        ###BACK BIND CHOOSE###
        self.label1 = QLabel("Amulet of Return bind:",self)
        self.label1.setGeometry(370,100,130,20)
        self.Back_Bind_List = QComboBox(self)
        self.Back_Bind_List.setGeometry(370,120,50,20)
        self.Back_Bind_List.currentTextChanged.connect(self.get_back_bind)
        ######################

        ###IMG###
        self.Shinning_Effect = QLabel(self)
        self.pixmap = QPixmap("SE.png")
        pixmap2 = self.pixmap.scaled(20,20)
        self.Shinning_Effect.setPixmap(pixmap2)
        self.Shinning_Effect.setGeometry(440,165,30,30)
        #########

        ###HEAL BIND CHOOSE###
        self.label2 = QLabel("Shining Effect(Heal) bind:",self)
        self.label2.setGeometry(370,150,150,20)
        self.Heal_Bind_List = QComboBox(self)
        self.Heal_Bind_List.setGeometry(370,170,50,20)
        self.Heal_Bind_List.currentTextChanged.connect(self.get_heal_bind)
        ######################

        ###AVAILABLE BINDS###
        binds = ["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t"]
        for item in binds:
            self.Back_Bind_List.addItem(item)
            self.Heal_Bind_List.addItem(item)
        #####################

        ###START BUTTON###
        self.StartButton = QPushButton("START",self)
        self.StartButton.setGeometry(440,200,80,40)
        self.StartButton.clicked.connect(self.ShanerBot_clicked)
        ##################
        
        ###HIDES###
        self.SP_List.hide()
        self.StartButton.hide()
        self.label.hide()
        self.label1.hide()
        self.label2.hide()
        self.AoR.hide()
        self.Shinning_Effect.hide()
        self.Back_Bind_List.hide()
        self.Heal_Bind_List.hide()
        ###########
        self.SP_List.activated.connect(self.Shaner_SP_choose)
        
    def Shaner_SP_choose(self,index):
        if index == 0: ###None
            self.label1.hide()
            self.label2.hide()
            self.AoR.hide()
            self.Shinning_Effect.hide()
            self.Back_Bind_List.hide()
            self.Heal_Bind_List.hide()
            self.StartButton.hide()
        if index == 1: ###Cruss
            self.label1.show()
            self.label2.show()
            self.AoR.show()
            self.Shinning_Effect.show()
            self.Back_Bind_List.show()
            self.Heal_Bind_List.show()
            self.StartButton.show()

    def Shaner_config_show(self):
        ###IC###
        self.IC_slot1.hide()
        self.IC_label.hide()
        self.IC_Start.hide()
        self.IC_label1.hide()
        self.IC_label2.hide()
        self.IC_acc_number.hide()
        ########
        self.SP_List.show()
        self.Shaner_label.show()
        self.label.show()

    def IC_config_show(self):
        self.IC_label.show()
        self.IC_Start.show()
        self.IC_label1.show()
        self.IC_acc_number.show()

    def get_heal_bind(self,text):
        self.Heal_Bind = str(text)

    def get_back_bind(self,text):
        self.Back_Bind = str(text)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec())
