import sys
from main_window import Ui_DavidDevCalculator
from PyQt5 import QtCore, QtGui, QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    DavidDevCalculator = QtWidgets.QMainWindow()
    ui = Ui_DavidDevCalculator()
    ui.setupUi(DavidDevCalculator)
    DavidDevCalculator.show()
    sys.exit(app.exec_())
