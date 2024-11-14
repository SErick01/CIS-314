import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit,
                             QMainWindow, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My GUI Application")
        self.setGeometry(200, 200, 500, 300)

        self.label = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()
        self.label4 = QLabel()
        self.label5 = QLabel()
        self.label6 = QLabel()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter your text here and taste the rainbow")
        self.input.setStyleSheet("color: white; font-size: 18px")

        self.input.textChanged.connect(self.label.setText)
        self.input.textChanged.connect(self.label2.setText)
        self.input.textChanged.connect(self.label3.setText)
        self.input.textChanged.connect(self.label4.setText)
        self.input.textChanged.connect(self.label5.setText)
        self.input.textChanged.connect(self.label6.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)

        layout.addWidget(self.label)
        self.label.setStyleSheet("color: red; font-size: 12px")
        layout.addWidget(self.label2)
        self.label2.setStyleSheet("color: orange; font-size: 12px")
        layout.addWidget(self.label3)
        self.label3.setStyleSheet("color: yellow; font-size: 12px")
        layout.addWidget(self.label4)
        self.label4.setStyleSheet("color: green; font-size: 12px")
        layout.addWidget(self.label5)
        self.label5.setStyleSheet("color: blue; font-size: 12px")
        layout.addWidget(self.label6)
        self.label6.setStyleSheet("color: purple; font-size: 12px")

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
