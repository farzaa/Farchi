import sys
from detective import Detective
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush


red = QColor(255, 0, 0);
green = QColor(0, 255, 0);

txt_color = QColor(255, 0, 0);
sleep_color = QColor(255, 0, 0);

class user_interface(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)

    
    def drawRectangles(self, qp):
      
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(txt_color)
        qp.drawRect(10, 15, 30, 30)

        qp.setBrush(green)
        qp.drawRect(130, 15, 30, 30)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 30, 30)

    def change_colors(self, txt, sleep):
        if txt:
            txt_color = QColor(0, 255, 0);
        else:
            txt_color = QColor(255, 0, 0);

        if sleep:
            sleep_color = QColor(0, 255, 0);
        else:
            sleep_color = QColor(255, 0, 0);

        self.repaint()
        print (sleep)
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ui = user_interface()
    d = Detective(ui)
    d.track_faces()
    sys.exit(app.exec_())