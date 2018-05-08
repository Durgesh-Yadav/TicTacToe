from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
def call(s):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("CONGRATULATIONS!")
    if s=='X':
        str ="AS per the game rules Player 1 has won."
        s = "Player 1 WINS!"
        msg.setIconPixmap(QPixmap('win.png'))
    elif s=='0':
        str ="AS per the game rules Player 2 has won."
        s = "Player 2 WINS!"
        msg.setIconPixmap(QPixmap('win.png'))
    else:
        str = "Both of you played well!"
        s = "It's a DRAW."
        msg.setWindowTitle("Oop'S")
        msg.setIcon(QMessageBox.Information)
    msg.setText(s)
    msg.setWindowIcon(QtGui.QIcon('icon.png'))
    msg.setDetailedText(str)
    msg.setStandardButtons(QtWidgets.QMessageBox.Close)
    msg.exec_()