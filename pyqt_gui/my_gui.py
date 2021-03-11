import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('my app')
        self.setWindowIcon(QIcon('python.ico'))
        self.resize(500, 350)  # x, y

        layout = QVBoxLayout()
        self.setLayout(layout)

        # widgets
        self.inputField = QLineEdit()
        button = QPushButton('&say hello')
        button.clicked.connect(self.say_hello)

        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def say_hello(self):
        input_text = self.inputField.text()
        self.output.setText(f'Hello {input_text}')


app = QApplication(sys.argv)

app.setStyleSheet("""
    QWidget {
        font-size: 25px;
    }
    
    QPushButton {
        font_size: 20px;
    }
""")

window = MyApp()
window.show()

app.exec()
