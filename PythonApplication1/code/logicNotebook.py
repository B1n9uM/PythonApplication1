from PySide6.QtWidgets import QMainWindow, QTextEdit, QWidget, QFileDialog, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QMenu
from PySide6.QtGui import QAction, QKeySequence
import webbrowser


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
        
        #Settings menubar

        # self.switch_window = {f"list{i}" : None  for i in range(7)}


        self.createM()


    def createM(self):
        #File
        menuBar = self.menuBar()
        self.filemenu = QMenu("Файл", self)
        menuBar.addMenu(self.filemenu)

        #Help
        helps = QAction("Помощь", self)
        helps.triggered.connect(self.buttonHelp)
        menuBar.addAction(helps)
        #Open / Files
        menuAction = QAction("Открыть", self)
        menuAction.setShortcut(QKeySequence("Ctrl+O"))
        menuAction.triggered.connect(self.oFile)

        #Save / Files
        fileAction = QAction("Сохронить", self)
        fileAction.setShortcut(QKeySequence("Ctrl+S"))
        fileAction.triggered.connect(self.sFile)
        
        #Add Action / Files
        
        self.filemenu.addAction(menuAction)
        self.filemenu.addAction(fileAction)

    def oFile(self):
        file_path, _ =  QFileDialog.getOpenFileName(
            self, "Открыть файл", "", "Text Files (*.txt *.md *.ini *.json *.log *.csv *.xml *.yaml *.xml);;All Files (*)"

            )
        try:
            with open(file_path, "r", encoding= "utf-8") as file:
                 self.text = file.read()
                 self.input.setText(self.text)
                 self.path = file_path
        except:
            pass        

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
            QMessageBox.critical(self, "Файл не сохронён. Ошибка:", critical_errror)
           

    def buttonHelp(self):
        webbrowser.open("https://github.com/B1n9uM/PythonApplication1")
