import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication



class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('My practice application')
        self.setWindowIcon(QIcon('icon.jpg'))

        # 창의 위치와 크기를 설정
        self.setGeometry(300,300,300,200)

        #### quit버튼 만들기 #####
        """푸시 버튼 만들기"""
        btn = QPushButton('Quit', self)
        btn.move(0,0)
        btn.resize(btn.sizeHint())
        """clicked라는 시그널을 만들어 quit()메서드에 연결, 인스턴스 반환"""
        btn.clicked.connect(QCoreApplication.instance().quit)

        #### 툴팁 나타내기 ####
        QToolTip.setFont((QFont('SansSerif', 10)))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btnt = QPushButton('Button', self)
        btnt.setToolTip('This is a <b>QPushButton</b> widget')
        btnt.move(100,0)
        btnt.resize(btnt.sizeHint())

        #### 상태바만들기 ####
        QMainWindow.statusBar().showMessage('Ready')
        QMainWindow.setWindowTitle('Statusbar')



        self.show()


if __name__ == '__main__':
       app = QApplication(sys.argv)
       ex = MyApp()
       sys.exit(app.exec_())