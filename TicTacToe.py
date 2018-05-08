from PyQt5 import QtWidgets, QtGui, QtCore

import Application
class App:
    li =[]
    def appMain(self):
        app = QtWidgets.QApplication([])
        window = QtWidgets.QMainWindow()
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.darkBlue)
        window.setPalette(palette)
        window.setGeometry(650,200,650,650)
        window.setWindowTitle("Tic Tac Toe")
        window.setWindowIcon(QtGui.QIcon('icon.png'))
        window.show()
        x = y = 100
        for i in range(1, 4):
            x = 100
            for j in range(1, 4):
                b=App.button0(window, x, y)
                self.li.append(b)
                b.show()
                x += 150
            y += 150
        App.clicked(self.li)
        app.exec_()

    def clicked(li):
        li[0].clicked.connect(lambda: App.on_click(li[0], 0))
        li[1].clicked.connect(lambda: App.on_click(li[1], 1))
        li[2].clicked.connect(lambda: App.on_click(li[2], 2))
        li[3].clicked.connect(lambda: App.on_click(li[3], 3))
        li[4].clicked.connect(lambda: App.on_click(li[4], 4))
        li[5].clicked.connect(lambda: App.on_click(li[5], 5))
        li[6].clicked.connect(lambda: App.on_click(li[6], 6))
        li[7].clicked.connect(lambda: App.on_click(li[7], 7))
        li[8].clicked.connect(lambda: App.on_click(li[8], 8))
    a = 0
    cl = []
    lix = []
    li0 = []
    def on_click(li,d):
        z=App()
        li.setStyleSheet('QPushButton {font-size: 20pt}')
        if d not in z.cl:
            z.cl.append(d)
            if App.a == 0:
                App.a = 1
                App.lix.append(d)
                li.setText("X")
                App.check(z.lix,z.li0)
            else:
                App.a = 0
                App.li0.append(d)
                li.setText("0")
                App.check(z.lix,z.li0)


    def button0(str,x,y):
        b1 = QtWidgets.QPushButton(str)
        b1.resize(150,150)
        b1.move(x,y)
        return b1

    def en(self):
        print("here")
        bb= QtWidgets.QMessageBox.information(self, "Button Clicked", "You Clicked Wrong Button ")
        bb.show()

    def restart(self):
        for i in range(9):
            self.li[i].setText("")
    def check(lx, l0):
        lx = set(lx)
        l0 = set(l0)
        c1 = set([0,1,2])
        c2 = set([3,4,5])
        c3 = set([6,7,8])
        c4 = set([0,3,6])
        c5 = set([1,4,7])
        c6 = set([2,5,8])
        c7 = set([0,4,8])
        c8 = set([2,4,6])
        if len(lx)>2 :
            if (lx&c1)==c1 or (lx&c2)==c2 or (lx&c3)==c3 or (lx&c4)==c4 or (lx&c5)==c5 or (lx&c6)==c6 or (lx&c7)==c7 or (lx&c8)==c8:
                quit(Application.call('X'))
            elif (l0&c1)==c1 or (l0&c2)==c2 or (l0&c3)==c3 or (l0&c4)==c4 or (l0&c5)==c5 or (l0&c6)==c6 or (l0&c7)==c7 or (l0&c8)==c8:
                quit(Application.call('0'))
            elif len(lx)==5:
                quit(Application.call("Draw"))
q=App()
q.appMain()