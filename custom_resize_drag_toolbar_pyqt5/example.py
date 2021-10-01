from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
import resizable_qwidget
import toolbar
import sys

class ExampleWindow(resizable_qwidget.TestWindow):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        layout.addWidget(toolbar.CustomToolbar(self, "Example"))
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

        self.move(300, 300)
        self.resize(300, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = ExampleWindow()
    mw.show()
    sys.exit(app.exec_())