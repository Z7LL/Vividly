from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 500))
        MainWindow.setIconSize(QtCore.QSize(512, 512))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/LOGO.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setMaximumSize(QtCore.QSize(1200, 500))
        MainWindow.setStyleSheet("border-radius:10px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.506, y2:0, stop:0 rgba(157, 163, 164, 255), stop:1 rgba(213, 197, 200, 255));")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Next_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Next_Button.setGeometry(QtCore.QRect(410, 400, 371, 61))
        self.Next_Button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(213, 197, 200);\n"
"    color: #9DA3A4;\n"
"    font: bold 20px \"Arial\";\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFDBDA;\n"
"    color: #DB7F8E;\n"
"}\n"
"")
        self.Next_Button.setObjectName("Next_Button")
        self.Image_Step1 = QtWidgets.QFrame(self.centralwidget)
        self.Image_Step1.setGeometry(QtCore.QRect(5, 110, 390, 175))
        self.Image_Step1.setStyleSheet("border-image: url(assets/Step_1.png);")
        self.Image_Step1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Image_Step1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Image_Step1.setObjectName("Image_Step1")
        self.Image_Step2 = QtWidgets.QFrame(self.centralwidget)
        self.Image_Step2.setGeometry(QtCore.QRect(405, 110, 390, 175))
        self.Image_Step2.setStyleSheet("border-image: url(assets/Step_2.png);")
        self.Image_Step2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Image_Step2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Image_Step2.setObjectName("Image_Step2")
        self.Image_Step3 = QtWidgets.QFrame(self.centralwidget)
        self.Image_Step3.setGeometry(QtCore.QRect(805, 110, 390, 175))
        self.Image_Step3.setStyleSheet("border-image: url(assets/Step_3.png);")
        self.Image_Step3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Image_Step3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Image_Step3.setObjectName("Image_Step3")
        self.Step1 = QtWidgets.QLabel(self.centralwidget)
        self.Step1.setGeometry(QtCore.QRect(10, 300, 381, 71))
        self.Step1.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.Step1.setTextFormat(QtCore.Qt.AutoText)
        self.Step1.setScaledContents(False)
        self.Step1.setWordWrap(True)
        self.Step1.setObjectName("Step1")
        self.Step2 = QtWidgets.QLabel(self.centralwidget)
        self.Step2.setGeometry(QtCore.QRect(410, 300, 381, 71))
        self.Step2.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.Step2.setTextFormat(QtCore.Qt.AutoText)
        self.Step2.setScaledContents(False)
        self.Step2.setWordWrap(True)
        self.Step2.setObjectName("Step2")
        self.Step3 = QtWidgets.QLabel(self.centralwidget)
        self.Step3.setGeometry(QtCore.QRect(810, 300, 381, 121))
        self.Step3.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.Step3.setTextFormat(QtCore.Qt.AutoText)
        self.Step3.setScaledContents(False)
        self.Step3.setWordWrap(True)
        self.Step3.setObjectName("Step3")
        self.creating_restorepoint_label = QtWidgets.QLabel(self.centralwidget)
        self.creating_restorepoint_label.setGeometry(QtCore.QRect(0, 10, 1191, 81))
        self.creating_restorepoint_label.setStyleSheet("font: 87 30pt \"Segoe UI Black\";\n"
"background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.creating_restorepoint_label.setAlignment(QtCore.Qt.AlignCenter)
        self.creating_restorepoint_label.setObjectName("creating_restorepoint_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vividly +"))
        self.Next_Button.setText(_translate("MainWindow", "Next"))
        self.Step1.setText(_translate("MainWindow", "Step 1:\n"
"🔍 Search for \"Environment Variables\" in the Windows search bar."))
        self.Step2.setText(_translate("MainWindow", "Step 2:\n"
"🖱 Click on \"Create a Restore Point\" from the search results."))
        self.Step3.setText(_translate("MainWindow", "Step 3:\n"
"In the System Properties window, go to the System Protection tab.\n"
"Click on \"Create\" under the \"Protection Settings\" section.\n"
"Enter a name for your restore point (e.g., \"Before Vividly\").\n"
"Click \"Create\" and wait for the process to complete."))
        self.creating_restorepoint_label.setText(_translate("MainWindow", "Creating a Restore point"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())