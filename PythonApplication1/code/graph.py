
def themeWhite():
    """Простая белая тема: только цвета фона и текста."""
    return """
    QMainWindow { background: #ffffff; }
    QMenuBar    { background: #ffffff; color: #000000; }
    QMenu       { background: #ffffff; color: #000000; }
    QToolBar    { background: #ffffff; }
    QTextEdit   { background: #ffffff; color: #000000; }
    """


def themeDark():
    """Простая тёмная тема: цвета фона и текста + видимый hover у кнопок и меню."""
    return """
    QMainWindow { background: #202020; }
    QMenuBar    { background: #303030; color: #eeeeee; }
    QMenu       { background: #303030; color: #eeeeee; }
    QToolBar    { background: #303030; }
    QTextEdit   { background: #1e1e1e; color: #eeeeee; }

    QPushButton, QToolButton { color: #eeeeee; }
    QPushButton:hover, QToolButton:hover { background: #454545; color: #ffffff; }
    QPushButton:pressed, QToolButton:pressed { background: #2b2b2b; color: #ffffff; }

    QMenuBar::item:hover { background: #3d3d3d; color: #ffffff; }
    QMenuBar::item:selected { background: #454545; color: #ffffff; }
    QMenu::item:hover { background: #3a3a3a; color: #ffffff; }
    QMenu::item:selected { background: #4a4a4a; color: #ffffff; }
    """


def beautifulStyle_White():
    """Красивая светлая тема: мягкие серые тона, без резких акцентов."""
    return """
    QMainWindow {
        background: #f4f5f7;
    }

    QMenuBar {
        background: #fafafa;
        color: #33363b;
        border-bottom: 1px solid #e1e3e7;
        padding: 3px 6px;
    }
    QMenuBar::item {
        padding: 5px 10px;
        border-radius: 4px;
    }
    QMenuBar::item:selected {
        background: #e9ecf1;
    }

    QMenu {
        background: #ffffff;
        color: #33363b;
        border: 1px solid #dfe2e7;
        border-radius: 5px;
    }
    QMenu::item {
        padding: 6px 26px 6px 14px;
    }
    QMenu::item:selected {
        background: #e8eef8;
        color: #2b4f83;
    }
    QMenu::separator {
        height: 1px;
        background: #e6e8ec;
        margin: 4px 8px;
    }

    QTextEdit {
        background: #ffffff;
        color: #2f3237;
        border: 1px solid #dfe2e7;
        border-radius: 5px;
        padding: 8px;
        font-family: "Segoe UI", "Consolas", sans-serif;
        font-size: 13px;
        selection-background-color: #d7e3f4;
        selection-color: #233248;
    }

    QToolBar {
        background: #fafafa;
        border: none;
        border-bottom: 1px solid #e1e3e7;
        spacing: 3px;
        padding: 4px;
    }

    QPushButton, QToolButton {
        background: #ffffff;
        color: #33363b;
        border: 1px solid #d7dae0;
        border-radius: 4px;
        padding: 5px 12px;
    }
    QPushButton:hover, QToolButton:hover {
        background: #f1f3f6;
    }
    QPushButton:pressed, QToolButton:pressed {
        background: #e6e9ee;
    }
    QToolButton {
        border: none;
        padding: 6px;
    }

    QLineEdit {
        background: #ffffff;
        color: #2f3237;
        border: 1px solid #dfe2e7;
        border-radius: 4px;
        padding: 4px 8px;
        selection-background-color: #d7e3f4;
    }
    QLabel {
        color: #555a61;
    }

    QScrollBar:vertical {
        background: transparent;
        width: 10px;
        margin: 0;
    }
    QScrollBar::handle:vertical {
        background: #c9ccd2;
        border-radius: 5px;
        min-height: 24px;
    }
    QScrollBar::handle:vertical:hover {
        background: #b9bdc4;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0;
    }
    QScrollBar:horizontal {
        background: transparent;
        height: 10px;
        margin: 0;
    }
    QScrollBar::handle:horizontal {
        background: #c9ccd2;
        border-radius: 5px;
        min-width: 24px;
    }
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        width: 0;
    }

    QStatusBar {
        background: #fafafa;
        color: #6a6f77;
    }
    """


def beautifilStyle_Dark():
    """Красивая тёмная тема: угольный фон, приглушённый сине-серый акцент."""
    return """
    QMainWindow {
        background: #232529;
    }

    QMenuBar {
        background: #2c2f34;
        color: #d7d9dd;
        border-bottom: 1px solid #3a3e45;
        padding: 3px 6px;
    }
    QMenuBar::item {
        padding: 5px 10px;
        border-radius: 4px;
    }
    QMenuBar::item:selected {
        background: #3a3e45;
    }

    QMenu {
        background: #2c2f34;
        color: #d7d9dd;
        border: 1px solid #40444b;
        border-radius: 5px;
    }
    QMenu::item {
        padding: 6px 26px 6px 14px;
    }
    QMenu::item:selected {
        background: #3c4a5e;
        color: #eaf0f8;
    }
    QMenu::separator {
        height: 1px;
        background: #41454c;
        margin: 4px 8px;
    }

    QTextEdit {
        background: #1e2023;
        color: #d7d9dd;
        border: 1px solid #3a3e45;
        border-radius: 5px;
        padding: 8px;
        font-family: "Consolas", "Segoe UI", monospace;
        font-size: 13px;
        selection-background-color: #405372;
        selection-color: #ffffff;
    }

    QToolBar {
        background: #2c2f34;
        border: none;
        border-bottom: 1px solid #3a3e45;
        spacing: 3px;
        padding: 4px;
    }

    QPushButton, QToolButton {
        background: #33363c;
        color: #d7d9dd;
        border: 1px solid #454a52;
        border-radius: 4px;
        padding: 5px 12px;
    }
    QPushButton:hover, QToolButton:hover {
        background: #3c4047;
    }
    QPushButton:pressed, QToolButton:pressed {
        background: #2a2d32;
    }
    QToolButton {
        border: none;
        padding: 6px;
    }

    QLineEdit {
        background: #1e2023;
        color: #d7d9dd;
        border: 1px solid #3a3e45;
        border-radius: 4px;
        padding: 4px 8px;
        selection-background-color: #405372;
    }
    QLabel {
        color: #a9adb4;
    }

    QScrollBar:vertical {
        background: transparent;
        width: 10px;
        margin: 0;
    }
    QScrollBar::handle:vertical {
        background: #565b63;
        border-radius: 5px;
        min-height: 24px;
    }
    QScrollBar::handle:vertical:hover {
        background: #666c75;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0;
    }
    QScrollBar:horizontal {
        background: transparent;
        height: 10px;
        margin: 0;
    }
    QScrollBar::handle:horizontal {
        background: #565b63;
        border-radius: 5px;
        min-width: 24px;
    }
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        width: 0;
    }

    QStatusBar {
        background: #2c2f34;
        color: #9aa0a8;
    }
    """
