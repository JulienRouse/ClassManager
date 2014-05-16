from PyQt5.QtWidgets import (QDialog,QApplication,QWidget,QGridLayout,
                             QLineEdit,QHBoxLayout,QVBoxLayout,QMainWindow,
                             QAction,QTabWidget,QLabel,QPushButton)
from PyQt5.QtGui import QIcon, QKeySequence
#from PyQt5.QtCore import QString



class FenetreCentrale(QDialog):
    def __init__(self, parent=None):
        super(FenetreCentrale,
              self).__init__(parent)

        tabWidget = QTabWidget()
        tabWidget.addTab(ModaliteEvaluation(),"Modalite d'evaluation")
        #tabWidget.addTab(Essai(),"Lolilol")

        layout = QVBoxLayout()
        layout.addWidget(tabWidget)
        
        self.setLayout(layout)

class ModaliteEvaluation(QWidget):
    """
    classe qui servira a definir les periodes devaluations
    le systeme de note etc
    """
    def __init__(self,parent=None):
        super(ModaliteEvaluation,self).__init__(parent)
        
        ##########################
        #premiere ligne, le titre#
        ##########################
        self.labelTitre = QLabel(self)
        self.labelTitre.setText("Liste des periodes d'evaluation".upper())
        #############################
        #seconde ligne, les colonnes#
        #############################
        self.labelDebut = QLabel(self)
        self.labelDebut.setText("Debut".upper())
        
        self.labelFin = QLabel(self)
        self.labelFin.setText("Fin".upper())
        ##########################
        #3-n lignes, les periodes#
        ##########################
        self.labelPeriode1 = QLabel(self)
        self.labelPeriode1.setText("Periode 1")

        self.leDate1Debut = QLineEdit(self)
        self.leDate1Debut.setInputMask("99/99/99")
        self.leDate1Debut.setMaxLength(8)
        
        self.leDate1Fin = QLineEdit(self)
        self.leDate1Fin.setInputMask("99/99/99")
        self.leDate1Fin.setMaxLength(8)
        
        self.labelPeriode2 = QLabel(self)
        self.labelPeriode2.setText("Periode 2")

        self.leDate2Debut = QLineEdit(self)
        self.leDate2Debut.setInputMask("99/99/99")
        self.leDate2Debut.setMaxLength(8)
        
        self.leDate2Fin = QLineEdit(self)
        self.leDate2Fin.setInputMask("99/99/99")
        self.leDate2Fin.setMaxLength(8)

        self.labelPeriode3 = QLabel(self)
        self.labelPeriode3.setText("Periode 3")

        self.leDate3Debut = QLineEdit(self)
        self.leDate3Debut.setInputMask("99/99/99")
        self.leDate3Debut.setMaxLength(8)
        
        self.leDate3Fin = QLineEdit(self)
        self.leDate3Fin.setInputMask("99/99/99")
        self.leDate3Fin.setMaxLength(8)
        ######################
        #bouton de sauvegarde#
        ######################
        self.boutonValidateDate = QPushButton("save",self)
        self.boutonValidateDate.clicked.connect(self.onValidation)
        
        layout = QGridLayout()
        layout.addWidget(self.labelTitre,1,0,1,4)
        layout.addWidget(self.labelDebut,2,2)
        layout.addWidget(self.labelFin,2,3)
        #1ere periode
        layout.addWidget(self.labelPeriode1,3,0)
        layout.addWidget(self.leDate1Debut,3,2)
        layout.addWidget(self.leDate1Fin,3,3)
        #2eme periode
        layout.addWidget(self.labelPeriode2,4,0)
        layout.addWidget(self.leDate2Debut,4,2)
        layout.addWidget(self.leDate2Fin,4,3)
        #3eme periode
        layout.addWidget(self.labelPeriode3,5,0)
        layout.addWidget(self.leDate3Debut,5,2)
        layout.addWidget(self.leDate3Fin,5,3)
        #button
        layout.addWidget(self.boutonValidateDate,6,4)
        self.setLayout(layout)

    def onValidation(self):
        pass

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
        self.show()
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
