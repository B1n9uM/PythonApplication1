from PySide6.QtWidgets import QMainWindow, QTextEdit, QWidget, QFileDialog, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QMenu
from PySide6.QtGui import QAction, QKeySequence
import webbrowser

from graph import themeWhite, themeDark, beautifulStyle_White, beautifilStyle_Dark


class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.path = None
        self.input = QTextEdit()

        #Settings window
        self.setWindowTitle("BnumsPad")
        self.setGeometry(100,100,800,600)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1440, 960)

        #Settings notepad 
        self.setCentralWidget(self.input)
        


        # self.switch_window = {f"list{i}" : None  for i in range(7)}
        self.createMenu()

        self.setStyleSheet(themeWhite()) #Style

    def createMenu(self):
        #File
        menuBar = self.menuBar()
        self.filemenu = QMenu("Файл", self)
        menuBar.addMenu(self.filemenu)

        #Help
        helps = QAction("Помощь", self)
        helps.triggered.connect(self.buttonHelp)
        menuBar.addAction(helps)
        #Files / Open
        openAction = QAction("Открыть", self)
        openAction.setShortcut(QKeySequence("Ctrl+O"))
        openAction.triggered.connect(self.oFile)

        #Files / Save
        saveAction = QAction("Сохранить", self)
        saveAction.setShortcut(QKeySequence("Ctrl+S"))
        saveAction.triggered.connect(self.sFile)

        #Themes 
        self.themes = QMenu("Темы", self)
        menuBar.addMenu(self.themes)

        #Themes / Dark
        dark = QAction("Dark", self)
        dark.triggered.connect(self.buttonDark)

        #Themes / White
        white = QAction("White", self)
        white.triggered.connect(self.buttonWhite)

        #Themes / coolDark
        coolWhite = QAction("White+", self)
        coolWhite.triggered.connect(self.cool_buttonWhite)

        #Themes / coolWhite
        coolDark = QAction("Dark+", self)
        coolDark.triggered.connect(self.cool_buttonDark)
        
        #Files / file Action
        self.filemenu.addAction(openAction)
        self.filemenu.addAction(saveAction)

        #Themes / theme Action
        self.themes.addAction(dark)
        self.themes.addAction(white)
        self.themes.addAction(coolDark)
        self.themes.addAction(coolWhite)

    #Open file
    def oFile(self):
        file_path, _ =  QFileDialog.getOpenFileName(
            self, "Открыть файл", "", "Text Files (*.txt *.md *.ini *.json *.log *.csv *.yaml *.xml);;All Files (*)"

            )
        try:
            with open(file_path, "r", encoding= "utf-8") as file:
                 self.text = file.read()

                 self.input.setText(self.text)
                 #We take the main variable
                 self.path = file_path
        except:
            pass        

    #Save file
    def sFile(self):

        if not self.path:
            file_path, _ = QFileDialog.getSaveFileName(
                self, "Сохранить файл", "", "Text Files (*.txt);;All Files (*)" )
            if not file_path:
                return

            self.path = file_path
            print("file dialog the save")

        try:
            with open(self.path, "w", encoding = "utf-8") as file:
                file.write(self.input.toPlainText())
                print("pass file save")

        except Exception as critical_errror:
            QMessageBox.critical(self, "Файл не сохранён. Ошибка:", critical_errror)
           
    #def button help 
    def buttonHelp(self):
        webbrowser.open("https://github.com/B1n9uM/PythonApplication1")


    #Themes def _theme_ 
    def buttonWhite(self):
        self.setStyleSheet(themeWhite())

    def buttonDark(self):
        self.setStyleSheet(themeDark())

    def cool_buttonWhite(self):
        self.setStyleSheet(beautifulStyle_White())

    def cool_buttonDark(self):
        self.setStyleSheet(beautifilStyle_Dark())