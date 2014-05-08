from PyQt5.QtWidgets import (QDialog,QApplication,QWidget,QGridLayout,QLineEdit,QVBoxLayout,QMainWindow,QAction)
from PyQt5.QtGui import QIcon, QKeySequence

class FenetreCentrale(QDialog):
    def __init__(self, parent=None):
        super(FenetreCentrale,
              self).__init__(parent)
        lineEdit = QLineEdit()
        lineEdit2 = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(lineEdit)
        layout.addWidget(lineEdit2)
        self.setLayout(layout)

class  Fenetre(QMainWindow):
    def __init__(self, parent=None):
        super(Fenetre,self).__init__(parent)
        self.initUi()
    
    def initUi(self):
       
        self.setWindowTitle("ClassManager")
        
        
        self.dialog = FenetreCentrale()
        self.setCentralWidget(self.dialog)
        

        self.createActions()
        self.createMenus()
        self.resize(360,145)
        self.show()
    

        
        
    
    def blabla(self):
        pass

    def createActions(self):
        self.newAct = QAction("&New", self,
            shortcut=QKeySequence.New, statusTip="Create a new file",
                              triggered=self.blabla)
        
        self.openAct = QAction( "&Open...", self,
                shortcut=QKeySequence.Open, statusTip="Open an existing file",
                               triggered=self.blabla)

        self.saveAct = QAction( "&Save", self,
                shortcut=QKeySequence.Save,
                               statusTip="Save the document to disk", triggered=self.blabla)

        self.saveAsAct = QAction("Save &As...", self,
                shortcut=QKeySequence.SaveAs,
                statusTip="Save the document under a new name",
                                 triggered=self.blabla)

        self.exitAct = QAction("&Exit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.close)

    def createToolBars(self):
        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.addAction(self.newAct)
        self.fileToolBar.addAction(self.openAct)
        self.fileToolBar.addAction(self.saveAct)

    def createMenus(self):
        """ self.fileMenu = self.menuBar()
        self.fileMenu.addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        """

        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)






if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    
    fenetre = Fenetre()
   

   
    
    
    sys.exit(app.exec_())
