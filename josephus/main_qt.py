from PyQt5.QtWidgets import QApplication
from josephus.adapter.qt_interface import QtJoseph


if __name__ == "__main__":
    app = QApplication([])
    qt_joseph = QtJoseph()
    qt_joseph.ui.show()
    app.exec_()
    