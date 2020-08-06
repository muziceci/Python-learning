from tkinter import *
from tkinter.filedialog import askopenfilename
from josephus.interface.realise_joseph import RealiseJoseph
import tkinter


class TkJoseph(Tk):
    def __init__(self):
        super().__init__()
        self.text = Text()
        self.file = Entry()
        self.start = Entry()
        self.step = Entry()
        self.title("约瑟夫环问题")
        #  屏幕居中
        width = 600
        height = 400
        x = (self.winfo_screenwidth()-width)/2
        y = (self.winfo_screenheight()-height)/2
        self.geometry("%dx%d+%d+%d" % (width, height, x, y))
        #  占位
        Label(self, width=10).grid(row=0, column=0)

        Label(self, text="保存信息的文件地址：").grid(row=1, column=1)
        Label(self, text="开始报数的位置：").grid(row=2, column=1)
        Label(self, text="出约瑟夫环的报数：").grid(row=3, column=1)

        self.file = Entry(self, textvariable=StringVar)
        self.file.grid(row=1, column=2, padx=10, pady=5)
        self.start = Entry(self, textvariable=StringVar)
        self.start.grid(row=2, column=2, padx=10, pady=5)
        self.step = Entry(self, textvariable=StringVar)
        self.step.grid(row=3, column=2, padx=10, pady=5)

        self.text = Text(self, width=50, height=15)
        self.text.place(x=100, y=150)

        Button(self, text="选择文件", width=7, command=self.choose_file).place(x=365, y=22)
        Button(self, text="确认", width=10, command=self.show).place(x=470, y=40)
        Button(self, text="退出", width=10, command=self.quit).place(x=470, y=80)

        self.mainloop()

    def choose_file(self):
        # 显示文件路径到entry框
        path = askopenfilename()
        self.file.insert(0, path)

    def show(self):
        # 清楚text框内容
        self.text.delete(1.0, 'end')
        # 获取结果，并将结果显示到text框
        try:
            joseph = RealiseJoseph(self.file.get(), int(self.start.get()), int(self.step.get()))
            self.text.insert(INSERT, joseph.get_result())
        except FileNotFoundError:
            self.text.insert(INSERT, 'Please input correct path of file!')


