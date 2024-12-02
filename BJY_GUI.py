from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:/Python/PYTHONPROJECTS/BJY_ver_with_pyQT/hasb.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.btn_loss = QtWidgets.QPushButton(self.centralwidget)
        self.btn_loss.setGeometry(QtCore.QRect(0, 190, 121, 41))
        self.btn_loss.setStyleSheet("background-color: rgb(255, 194, 227);")
        self.btn_loss.setObjectName("btn_loss")
        self.btn_result = QtWidgets.QPushButton(self.centralwidget)
        self.btn_result.setGeometry(QtCore.QRect(165, 230, 75, 23))
        self.btn_result.setStyleSheet("background-color: rgb(255, 0, 4);")
        self.btn_result.setObjectName("bnt_result")
        self.text_title = QtWidgets.QLabel(self.centralwidget)
        self.btn_gain = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gain.setGeometry(QtCore.QRect(280, 190, 121, 41))
        self.btn_gain.setStyleSheet("background-color: rgb(255, 194, 227);")
        self.btn_gain.setObjectName("btn_gain")

        self.text_title.setGeometry(QtCore.QRect(90, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.text_title.setFont(font)
        #self.text_title.setStyleSheet("background-color: green;")
        self.text_title.setTextFormat(QtCore.Qt.AutoText)
        self.text_title.setObjectName("text_title")
        self.age = QtWidgets.QLineEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(150, 50, 130, 30))
        self.age.setObjectName("age")
        self.weight = QtWidgets.QLineEdit(self.centralwidget)
        self.weight.setGeometry(QtCore.QRect(150, 100, 130, 30))
        self.weight.setObjectName("weight")
        self.height = QtWidgets.QLineEdit(self.centralwidget)
        self.height.setGeometry(QtCore.QRect(150, 150, 130, 30))
        self.height.setObjectName("height")
        self.text_age = QtWidgets.QLabel(self.centralwidget)
        self.text_age.setGeometry(QtCore.QRect(90, 60, 45, 15))
        self.text_age.setObjectName("text_age")
        self.text_weight = QtWidgets.QLabel(self.centralwidget)
        self.text_weight.setGeometry(QtCore.QRect(90, 110, 45, 15))
        self.text_weight.setObjectName("text_weight")
        self.text_height = QtWidgets.QLabel(self.centralwidget)
        self.text_height.setGeometry(QtCore.QRect(90, 160, 45, 15))
        self.text_height.setObjectName("text_height")

        self.BJUK = QtWidgets.QLabel(self.centralwidget)
        self.BJUK.setGeometry(QtCore.QRect(310, 250, 300, 300))
        self.BJUK.setFixedWidth(310)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(10)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.BJUK.setStyleSheet("color: black")
        self.BJUK.setFont(font)
        self.BJUK.setObjectName("BJUK")

        self.cartman = QtWidgets.QLabel(self.centralwidget)
        self.cartman.setGeometry(QtCore.QRect(400, 265, 150, 70))
        self.BJUK.setObjectName("cartman")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()
        self.is_equal = False


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор каллорий"))
        self.btn_loss.setText(_translate("MainWindow", "Похудеть"))
        self.text_title.setText(_translate("MainWindow", "Введите данные:"))
        self.text_age.setText(_translate("MainWindow", "Возраст:"))
        self.text_weight.setText(_translate("MainWindow", "Вес:"))
        self.text_height.setText(_translate("MainWindow", "Рост:"))
        self.btn_gain.setText(_translate("MainWindow", "Набрать"))
        self.btn_result.setText(_translate("MainWindow", "Подсчёт"))


    def add_functions(self):

        self.btn_loss.clicked.connect(lambda: self.weight_loss_or_gain(self.btn_loss.text()))
        self.btn_gain.clicked.connect(lambda: self.weight_loss_or_gain(self.btn_gain.text()))
        self.btn_result.clicked.connect(self.result)

    def result(self):
        if self.is_equal == False:
            self.BJUK.setText("Введите число!\n(если число с десятымы,\n то введите его через символ «.»)")
        else:
            self.BOV = 447.593 + (9.247 * self.w) + (3.098 * self.h) - (
                        4.330 * self.a)  # Формула Харисса-Бенедикта базового обмена веществ
            self.CH_low_activity = round(self.BOV * 1.2)  # Суточная каллорийность при низкой активности
            self.CH_middle_activity = round(self.BOV * 1.375)  # Суточная каллорийность при средней активности
            self.CH_high_activity = round(self.BOV * 1.55)  # Суточная каллорийность при высокой активности
            self.CH_low_activity *= self.x
            self.CH_middle_activity *= self.x
            self.CH_high_activity *= self.x
            res = (f"Норма каллорийности:  \nПри низкой активности {round(self.CH_low_activity)} \n"
                   f"Б:{round((self.CH_low_activity / 4) * 0.25)} Ж:{round((self.CH_low_activity / 9) * 0.35)} У:{round((self.CH_low_activity / 4) * 0.4)} "

                   f"\nПри средней активности {round(self.CH_middle_activity)} \n"
                   f"Б:{round((self.CH_middle_activity / 4) * 0.25)} Ж:{round((self.CH_middle_activity / 9) * 0.35)} У:{round((self.CH_middle_activity / 4) * 0.4)}"

                   f"\nПри высокой активности {round(self.CH_high_activity)} \n"
                   f"Б:{round((self.CH_high_activity / 4) * 0.25)} Ж:{round((self.CH_high_activity / 9) * 0.35)} У:{round((self.CH_high_activity / 4) * 0.4)}")
            if self.w > 95:
                self.cartman.setPixmap(QtGui.QPixmap("E:/Python/PYTHONPROJECTS/BJY_ver_with_pyQT/cartman.png"))
                self.BJUK.setText(res)
            else:
                self.cartman.clear()
                self.BJUK.setText(res)

    def weight_loss_or_gain(self, x):
        if x == 'Набрать':
            self.x = 1.2
        else:
            self.x = 0.8

        try:
            self.a = float(self.age.text())
            self.w = float(self.weight.text())
            self.h = float(self.height.text())
            self.is_equal = True
            return self.a, self.w, self.h
        except ValueError:
            self.is_equal = False
            self.BJUK.setText("Введите число!\n(если число с десятымы,\n то введите его через символ «.»)")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

