from PyQt5 import QtWidgets
from sys import argv
from grillz_calculator.grillz_app import GrillzApp


def main():
    app = QtWidgets.QApplication(argv)
    window = GrillzApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
