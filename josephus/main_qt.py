from PyQt5.QtWidgets import QApplication
from josephus.representers.qt_interface import QtJoseph


app = QApplication([])
qt_joseph = QtJoseph()
qt_joseph.ui.show()
app.exec_()

