from PyQt5.QtWidgets import (QDialog,QApplication,QWidget,QGridLayout,
                             QLineEdit,QHBoxLayout,QVBoxLayout,QMainWindow,
                             QAction,QTabWidget,QLabel,QPushButton,
                             QComboBox)
from PyQt5.QtGui import QIcon, QKeySequence, QPalette, QColor

class GestionEleve(QWidget):
    def __init__(self,parent=None):
        super(GestionEleve,self).__init__(parent)
        
        #charge la classe en cour
        self.initClass()

        palette = QPalette()
        palette.setColor(QPalette.Text,QColor(128,128,128))    

        self.leNom = QLineEdit(self)
        self.leNom.setText("NOM..")
        self.leNom.setPalette(palette)
        
        self.lePrenom = QLineEdit(self)
        self.lePrenom.setText("PRENOM..")
        self.lePrenom.setPalette(palette)
        
        self.comboSex = QComboBox(self)
        self.comboSex.addItem("sexe..")
        self.comboSex.addItem("M")
        self.comboSex.addItem("F")
        
        self.comboClasse =  self.initComboClasse(["CE1","CE2"])
        
        self.buttonSave = QPushButton("Save")
        self.buttonSave.clicked.connect(self.saveEleve)

        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(self.leNom)
        layout.addWidget(self.lePrenom)
        layout.addWidget(self.comboSex)
        layout.addWidget(self.comboClasse)
        layout.addWidget(self.buttonSave)
        layout.addStretch()
        self.setLayout(layout)
    
    def initComboClasse(self,list):
        res = QComboBox()
        res.addItem("classe..")
        for elt in list:
            res.addItem(elt)
        return res
        
    def saveEleve(self):
        if (self.leNom.text == "NOM.."
            or self.lePrenom.text == "PRENOM.."
            or str(self.comboSex.currentText()) == "sexe.."
            or str(self.comboClasse.currentText()) == "classe.."
        ):
            pass
            #on enregistre pas
        else :
            pass
            #on enregistre
            
        
    def initClass(self):
        pass
