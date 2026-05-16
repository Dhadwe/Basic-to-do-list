from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,QVBoxLayout, QWidget, QLineEdit, QListWidget)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        layout = QVBoxLayout()
        central = QWidget()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter a task here")

        self.button = QPushButton("Add task")
        self.button.clicked.connect(self.add_to_list)

        self.to_do_list = QListWidget() 

        self.delete_button = QPushButton("Mark as done")
        self.delete_button.clicked.connect(self.mark_as_done)

        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.to_do_list) 
        layout.addWidget(self.delete_button)

        central.setLayout(layout)
        self.setCentralWidget(central)
        self.setStyleSheet("""
    QMainWindow, QWidget {
        background-color: #1e1e2e;
        color: #cdd6f4;
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 13px;
    }

    QLineEdit {
        background-color: #313244;
        color: #cdd6f4;
        border: 2px solid #6c7086;
        border-radius: 8px;
        padding: 8px 12px;
        selection-background-color: #cba6f7;
        selection-color: #1e1e2e;
    }
    QLineEdit:focus {
        border: 2px solid #cba6f7;
    }

    QPushButton {
        background-color: #cba6f7;
        color: #1e1e2e;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #b4befe;
    }
    QPushButton:pressed {
        background-color: #7287fd;
    }

    QPushButton#danger {
        background-color: #313244;
        color: #cba6f7;
        border: 2px solid #cba6f7;
    }
    QPushButton#danger:hover {
        background-color: #45475a;
        color: #f38ba8;
        border-color: #f38ba8;
    }
    QPushButton#danger:pressed {
        background-color: #f38ba8;
        color: #1e1e2e;
    }

    QListWidget {
        background-color: #181825;
        color: #cdd6f4;
        border: 2px solid #6c7086;
        border-radius: 8px;
        padding: 4px;
        outline: none;
    }
    QListWidget::item {
        padding: 8px 12px;
        border-radius: 6px;
        margin: 2px 0px;
    }
    QListWidget::item:selected {
        background-color: #45475a;
        color: #cba6f7;
        border-left: 3px solid #cba6f7;
    }
    QListWidget::item:hover:!selected {
        background-color: #2a273f;
    }

    QScrollBar:vertical {
        background: #181825;
        width: 8px;
        border-radius: 4px;
    }
    QScrollBar::handle:vertical {
        background: #6c7086;
        border-radius: 4px;
        min-height: 20px;
    }
    QScrollBar::handle:vertical:hover {
        background: #cba6f7;
    }
    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical {
        height: 0px;
    }        
""")

    def add_to_list(self):
        task = self.input.text()        # get text FROM the input
        if task:                        # don't add empty tasks
            self.to_do_list.addItem(task)  # add it TO the list widget
            self.input.clear()          # clear the input box after adding

    def mark_as_done(self):
        selected = self.to_do_list.currentRow()  # get selected item index
        if selected >= 0:                         # -1 means nothing selected
            self.to_do_list.takeItem(selected)    # remove it

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())