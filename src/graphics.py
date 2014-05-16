from PyQt5.QtWidgets import (QDialog,QApplication,QWidget,QGridLayout,
                             QLineEdit,QHBoxLayout,QVBoxLayout,QMainWindow,
                             QAction,QTabWidget,QLabel,QPushButton)
from PyQt5.QtGui import QIcon, QKeySequence


from ModaliteEvaluation import *
from GestionEleve import *


class FenetreCentrale(QDialog):
    def __init__(self, parent=None):
        super(FenetreCentrale,
              self).__init__(parent)

        tabWidget = QTabWidget()
        tabWidget.addTab(ModaliteEvaluation(),"Modalite d'evaluation")
        tabWidget.addTab(GestionEleve(),"Gestion des eleves")
        #tabWidget.addTab(Essai(),"Lolilol")

        layout = QVBoxLayout()
        layout.addWidget(tabWidget)
        
        self.setLayout(layout)


class  Fenetre(QMainWindow):
    def __init__(self, parent=None):
        super(Fenetre,self).__init__(parent)
        self.initUi()
    
    def initUi(self):
       
        self.setWindowTitle("ClassManager")

        self.fenetreOnFocus = FenetreCentrale()
        self.setCentralWidget(self.fenetreOnFocus)
        
        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.resize(360,145)
        self.showMaximized()
        self.statusBar()

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
        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)






if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    
    fenetre = Fenetre()
   

   
    
    
    sys.exit(app.exec_())
