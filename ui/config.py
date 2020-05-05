from PyQt5.QtGui import QFont


class Font(QFont):
    def __init__(self, size=12):
        super().__init__()
        self.setFamily('Arial')
        self.setPointSize(size)
        self.setBold(False)
        self.setWeight(75)
        self.setStyleStrategy(QFont.PreferDefault)


bigfont = Font(14)
mainfont = Font()
littlefont = Font(11)
