import sys
from PySide6.QtWidgets import QApplication

from logicNotebook import Win


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Win()
    window.show()
    sys.exit(app.exec())
