from PyQt5.QtWidgets import (QApplication,QWidget,QGridLayout)

class  Fenetre(QWidget):
    def __init__(self, parent=None):
        super(Fenetre,self).__init__(parent)
        self.initUi()
    
    def initUi(self):
       
        self.setWindowTitle("ClassManager")

    

if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    
    fenetre = Fenetre()
   

   
    fenetre.show()
    
    sys.exit(app.exec_())
