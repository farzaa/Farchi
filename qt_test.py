import sys
from detective import Detective
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush

class user_interface(QWidget):
    
    def __init__(self):
        super().__init__()
        self.red = QColor(255, 0, 0);
        self.green = QColor(0, 255, 0);

        self.txt_color = QColor(255, 0, 0);
        self.sleep_color = QColor(255, 0, 0);
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
        col.setNamedColor('#000')
        qp.setPen(col)

        qp.setBrush(self.sleep_color)
        qp.drawRect(10, 15, 30, 30)
        qp.drawText(0, 70, "Focused") 
              
        qp.setBrush(self.sleep_color)
        qp.drawRect(70, 15, 30, 30)
        qp.drawText(60, 70, "Sleeping")

        qp.setBrush(self.txt_color)
        qp.drawRect(130, 15, 30, 30)
        qp.drawText(120, 70, "Texting")

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 30, 30)

    def change_colors(self, txt, sleep):
        print (sleep)
        if txt:
            self.txt_color = QColor(0, 255, 0)
        else:
            self.txt_color = QColor(255, 0, 0)
        
        if sleep == None:
            return

        if sleep:
            self.sleep_color = QColor(0, 255, 0)
        else:
            self.sleep_color = QColor(255, 0, 0)


        self.update()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ui = user_interface()
    d = Detective(ui)
    d.track_faces()
    sys.exit(app.exec_())