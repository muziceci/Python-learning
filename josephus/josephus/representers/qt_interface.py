import os
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication
from josephus.realise.realise_joseph import RealiseJoseph


class QtJoseph:
    def __init__(self):
        #  从文件中加载ui
        self.ui = uic.loadUi("../josephus/josephus/representers/Qt_Ui/joseph.ui")
        #  当前文件位置
        self.cwd = os.getcwd()
        #  按钮添加事件
        self.ui.chooseButton.clicked.connect(self.choose_file)
        self.ui.confirmButton.clicked.connect(self.show)
        self.ui.quitButton.clicked.connect(QCoreApplication.instance().quit)

    def choose_file(self):
        choose_filename, file_type = QFileDialog.getOpenFileName(None,
                                                                 "选取文件",
                                                                 self.cwd,
                                                                 "All File(*);;Text Files(*.txt)")
        self.ui.fileText.setText(choose_filename)

    def show(self):
        file = self.ui.fileText.text()
        start = self.ui.startText.text()
        step = self.ui.stepText.text()
        joseph = RealiseJoseph(file, int(start), int(step))
        self.ui.showText.insertPlainText(joseph.get_str_result())
