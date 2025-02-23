from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QProgressBar  # Changed import
from PyQt5.QtCore import QThread, pyqtSignal
import subprocess
import json
import os


class Ui_RestorePoint(object):
    def setupUi(self, MainWindow):
        # Store MainWindow reference at the beginning
        self.MainWindow = MainWindow
        
        # Add mouse tracking
        self.MainWindow.setMouseTracking(True)
        self.dragging = False
        self.offset = None
        
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

        # Connect next button
        self.Next_Button.clicked.connect(self.on_next_clicked)
        
        # Store MainWindow reference
        self.MainWindow = MainWindow

    # Add mouse event handlers
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()
            self.MainWindow.setWindowOpacity(0.7)  # Set opacity when dragging starts

    def mouseMoveEvent(self, event):
        if self.dragging and self.offset:
            new_pos = self.MainWindow.mapToGlobal(event.pos() - self.offset)
            self.MainWindow.move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = False
            self.MainWindow.setWindowOpacity(1.0)  # Restore opacity when dragging ends

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

    def on_next_clicked(self):
        # Update JSON file
        with open('RestorePoint.json', 'w') as f:
            json.dump({'restore_point_created': True}, f)
        
        # Close current window and show main window
        self.MainWindow.close()
        self.show_main_window()

    def show_main_window(self):
        # Create main window using our MainWindow class instead of QMainWindow
        self.main_window = MainWindow()  # Use MainWindow class instead of QtWidgets.QMainWindow
        self.main_window.show()
        self.MainWindow.close()


class PowerShellWorker(QThread):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    
    def __init__(self, script, revert=False):
        super().__init__()
        self.script = script
        self.revert = revert
        
    def run(self):
        try:
            process = subprocess.Popen(
                ["powershell", "-Command", self.script],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True
            )
            process.wait()
            if process.returncode == 0:
                self.finished.emit()
            else:
                _, stderr = process.communicate()
                self.error.emit(stderr.decode())
        except Exception as e:
            self.error.emit(str(e))


class Ui_MainWindow(object):
    def __init__(self):
        self.settings_file = "Settings.json"
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                self.settings = json.load(f)
        else:
            self.settings = {"optimized": False, "last_optimization": None}
            self.save_settings()

    def save_settings(self):
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def setupUi(self, MainWindow):
        # Store MainWindow reference at the beginning
        self.MainWindow = MainWindow
        
        # Add mouse tracking
        self.MainWindow.setMouseTracking(True)
        self.dragging = False
        self.offset = None
        
        # Set window icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/LOGO.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        # Set custom cursor
        cursor = QtGui.QCursor(QtGui.QPixmap("assets/pointer.cur"))
        MainWindow.setCursor(cursor)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 630)
        MainWindow.setMinimumSize(QtCore.QSize(970, 630))
        MainWindow.setMaximumSize(QtCore.QSize(970, 630))
        MainWindow.setStyleSheet("background: transparent;")
        MainWindow.setIconSize(QtCore.QSize(512, 512))
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: transparent;")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMouseTracking(True)  # Add this line
        
        # Add background frame
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 970, 630))
        self.background.setStyleSheet("background-image: url(assets/Background.png);\n"
                                    "border-radius: 10px;")
        self.background.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background.setObjectName("background")
        
        self.Optimize = QtWidgets.QPushButton(self.centralwidget)
        self.Optimize.setGeometry(QtCore.QRect(280, 470, 411, 51))
        self.Optimize.setStyleSheet("QPushButton {\n"
"    background-color: rgb(219, 127, 142);\n"
"    color: #FFDBDA;\n"
"    font: bold 20px \"Arial\";\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"    border-image: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9DA3A4;\n"
"    color: #FFDBDA;\n"
"    border-image: none;\n"
"}\n"
"")
        self.Optimize.setObjectName("Optimize")
        
        # Set initial button text based on optimization status
        if self.settings["optimized"]:
            self.Optimize.setText("Revert Optimization")
        else:
            self.Optimize.setText("Optimize")
        
        self.Flower = QtWidgets.QFrame(self.centralwidget)
        self.Flower.setGeometry(QtCore.QRect(640, 430, 91, 91))
        self.Flower.setStyleSheet("image: url(assets/Flower.png);")
        self.Flower.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Flower.setObjectName("Flower")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(930, 10, 31, 31))
        self.exit.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    color: #DB7F8E;\n"
"    font: bold 20px \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    color: #9DA3A4;\n"
"    font: bold 20px \"Arial\";\n"
"}\n"
"")
        self.exit.setObjectName("exit")
        self.minimize = QtWidgets.QPushButton(self.centralwidget)
        self.minimize.setGeometry(QtCore.QRect(900, 10, 31, 31))
        self.minimize.setStyleSheet("QPushButton {\n"
"    background: transparent;\n"
"    color: #DB7F8E;\n"
"    font: bold 20px \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    color: #9DA3A4;\n"
"    font: bold 20px \"Arial\";\n"
"}\n"
"")
        self.minimize.setObjectName("minimize")
        
        # Add progress bar to main window
        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(230, 582, 511, 21))
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #DB7F8E;
                border-radius: 5px;
                text-align: center;
                background-color: #D5C5C8;
            }
            QProgressBar::chunk {
                background-color: #9DA3A4;
                border-radius: 3px;
            }
        """)
        self.progress_bar.hide()  # Hide initially
        
        MainWindow.setCentralWidget(self.centralwidget)

        # Store MainWindow reference
        self.MainWindow = MainWindow
        
        # Connect buttons to their functions
        self.exit.clicked.connect(self.exit_application)
        self.minimize.clicked.connect(self.minimize_window)

        # Connect Optimize button
        self.Optimize.clicked.connect(self.show_warning_dialog)

        # Update Optimize button text based on settings
        self.update_optimize_button()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Add mouse event handlers
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()
            self.MainWindow.setWindowOpacity(0.7)

    def mouseMoveEvent(self, event):
        if self.dragging and self.offset:
            new_pos = self.MainWindow.mapToGlobal(event.pos() - self.offset)
            self.MainWindow.move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = False
            self.MainWindow.setWindowOpacity(1.0)

    def exit_application(self):
        self.MainWindow.close()
        
    def minimize_window(self):
        self.MainWindow.showMinimized()

    def run_powershell_script(self, revert=False):
        script = '''
        Get-AppxPackage | Where-Object {$_.NonRemovable -eq $false} | ForEach-Object {Disable-AppBackgroundTask -PackageFamilyName $_.PackageFamilyName}

        $services = @(
            "SysMain",
            "DiagTrack",
            "XblGameSave",
            "dmwappushservice"
        )

        ForEach ($service in $services) {
            Stop-Service -Name $service -Force -ErrorAction SilentlyContinue
            Set-Service -Name $service -StartupType Disabled
        }

        Remove-Item -Path "C:\\Windows\\Temp\\*" -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item -Path "$env:TEMP\\*" -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item -Path "C:\\Windows\\Prefetch\\*" -Recurse -Force -ErrorAction SilentlyContinue

        New-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" -Name "MaxConnectionsPer1_0Server" -Value 10 -PropertyType DWord -Force
        New-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" -Name "MaxConnectionsPerServer" -Value 10 -PropertyType DWord -Force

        powercfg -attributes SUB_PROCESSOR 75b0ae3f-bce0-45a7-8c89-c9611c25e100 -ATTRIB_HIDE
        powercfg -setacvalueindex SCHEME_CURRENT SUB_PROCESSOR 75b0ae3f-bce0-45a7-8c89-c9611c25e100 0
        powercfg -setactive SCHEME_CURRENT

        Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name 'UserPreferencesMask' -Value ([byte[]](0x90,0x12,0x03,0x80,0x10,0x00,0x00,0x00)) -Force
        Stop-Process -Name explorer -Force
        Start-Process explorer

        New-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Serialize" -Name "StartupDelayInMSec" -Value 0 -PropertyType DWord -Force

        Stop-Service -Name "WSearch" -Force
        Set-Service -Name "WSearch" -StartupType Disabled

        reg add "HKCU\\Software\\Microsoft\\GameBar" /v AllowAutoGameMode /t REG_DWORD /d 0 /f
        reg add "HKCU\\Software\\Microsoft\\GameBar" /v AutoGameModeEnabled /t REG_DWORD /d 0 /f

        reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\DriverSearching" /v SearchOrderConfig /t REG_DWORD /d 0 /f

        reg add "HKEY_CURRENT_USER\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f
        reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\PolicyManager\\default\\ApplicationManagement\\AllowGameDVR" /v value /t REG_DWORD /d 0 /f
        ''' if not revert else '''
        # Revert changes
        $services = @("SysMain", "DiagTrack", "XblGameSave", "dmwappushservice", "WSearch")
        ForEach ($service in $services) {
            Set-Service -Name $service -StartupType Automatic
            Start-Service -Name $service
        }

        # Revert Internet Settings
        Remove-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" -Name "MaxConnectionsPer1_0Server" -ErrorAction SilentlyContinue
        Remove-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" -Name "MaxConnectionsPerServer" -ErrorAction SilentlyContinue

        # Revert Power Settings
        powercfg -attributes SUB_PROCESSOR 75b0ae3f-bce0-45a7-8c89-c9611c25e100 +ATTRIB_HIDE
        powercfg -setacvalueindex SCHEME_CURRENT SUB_PROCESSOR 75b0ae3f-bce0-45a7-8c89-c9611c25e100 1

        # Revert Explorer Settings
        Remove-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Serialize" -Name "StartupDelayInMSec" -ErrorAction SilentlyContinue
        Stop-Process -Name explorer -Force
        Start-Process explorer

        # Revert GameBar Settings
        reg add "HKCU\\Software\\Microsoft\\GameBar" /v AllowAutoGameMode /t REG_DWORD /d 1 /f
        reg add "HKCU\\Software\\Microsoft\\GameBar" /v AutoGameModeEnabled /t REG_DWORD /d 1 /f

        # Re-enable App Background Tasks
        Get-AppxPackage | ForEach-Object {Enable-AppBackgroundTask -PackageFamilyName $_.PackageFamilyName}

        # Revert Driver Searching
        reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\DriverSearching" /v SearchOrderConfig /t REG_DWORD /d 1 /f

        # Revert GameDVR Settings
        reg add "HKEY_CURRENT_USER\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 1 /f
        reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\PolicyManager\\default\\ApplicationManagement\\AllowGameDVR" /v value /t REG_DWORD /d 1 /f
        '''

        # Configure and show progress bar
        self.progress_bar.setValue(0)
        self.progress_bar.show()
        
        # Create and configure worker thread
        self.worker = PowerShellWorker(script, revert)
        self.worker.finished.connect(self.on_optimization_complete)
        self.worker.error.connect(self.on_optimization_error)
        
        # Setup progress update timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        
        # Start worker and progress
        self.worker.start()
        self.timer.start(100)  # Update every 100ms

    def update_progress(self):
        if self.progress_value < 95:  # Keep under 100% until actually complete
            self.progress_value += 1
            self.progress_bar.setValue(self.progress_value)

    def on_optimization_complete(self):
        self.timer.stop()
        self.progress_bar.setValue(100)
        
        # Update settings
        self.settings["optimized"] = not self.worker.revert
        self.settings["last_optimization"] = QtCore.QDateTime.currentDateTime().toString()
        self.save_settings()
        self.update_optimize_button()
        
        QMessageBox.information(None, "Success", 
                              "Optimization completed!" if not self.worker.revert else "Changes reverted!")
        self.progress_bar.hide()

    def on_optimization_error(self, error_message):
        self.timer.stop()
        self.progress_bar.hide()
        QMessageBox.critical(None, "Error", f"An error occurred: {error_message}")

    def show_warning_dialog(self):
        if self.settings["optimized"]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Revert Optimization?")
            msg.setInformativeText("Do you want to revert the previous optimization?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            if msg.exec_() == QMessageBox.Yes:
                self.run_powershell_script(revert=True)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("System Restore Point Recommended")
            msg.setInformativeText("It's recommended to create a System Restore Point before proceeding. Do you want to continue anyway?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                }
                QPushButton {
                    background-color: rgb(219, 127, 142);
                    color: #FFDBDA;
                    font: bold 12px "Arial";
                    padding: 5px 15px;
                    border-radius: 4px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #9DA3A4;
                }
            """)
            
            if msg.exec_() == QMessageBox.Yes:
                self.run_powershell_script()

    def update_optimize_button(self):
        if self.settings["optimized"]:
            self.Optimize.setText("Revert Optimization")
        else:
            self.Optimize.setText("Optimize")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vivdly +"))
        self.exit.setText(_translate("MainWindow", "X"))
        self.minimize.setText(_translate("MainWindow", "-"))


class RestorePointWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Set window icon before setting up UI
        icon = QtGui.QIcon("assets/LOGO.ico")
        self.setWindowIcon(icon)
        self.ui = Ui_RestorePoint()
        self.ui.setupUi(self)
        
        # Add direct mouse tracking
        self.setMouseTracking(True)
        self.centralWidget().setMouseTracking(True)
        
        # Set window flags and attributes
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()
            self.setWindowOpacity(0.7)

    def mouseMoveEvent(self, event):
        if hasattr(self, 'dragging') and self.dragging and hasattr(self, 'offset'):
            new_pos = event.globalPos() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = False
            self.setWindowOpacity(1.0)

    def check_restore_point(self):
        try:
            with open('RestorePoint.json', 'r') as f:
                data = json.load(f)
                return data.get('restore_point_created', False)
        except:
            return False


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Add direct mouse tracking
        self.setMouseTracking(True)
        self.centralWidget().setMouseTracking(True)
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()
            self.setWindowOpacity(0.7)

    def mouseMoveEvent(self, event):
        if hasattr(self, 'dragging') and self.dragging and hasattr(self, 'offset'):
            new_pos = event.globalPos() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = False
            self.setWindowOpacity(1.0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("assets/LOGO.ico"))
    
    # Check restore point status
    restore_window = RestorePointWindow()
    if not restore_window.check_restore_point():
        restore_window.show()
    else:
        main_window = MainWindow()
        main_window.show()
    
    sys.exit(app.exec_())
