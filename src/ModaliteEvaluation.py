from PyQt5.QtWidgets import (QDialog,QApplication,QWidget,QGridLayout,
                             QLineEdit,QHBoxLayout,QVBoxLayout,QMainWindow,
                             QAction,QTabWidget,QLabel,QPushButton)
from PyQt5.QtGui import QIcon, QKeySequence

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
        ############
        #label vide#
        ############
        self.labelVide = QLabel(self)
        self.labelVide.setText("        ")
        layout = QGridLayout()
        layout.addWidget(self.labelTitre,1,0,1,5)
        layout.addWidget(self.labelDebut,2,2)
        layout.addWidget(self.labelFin,2,4)
        #1ere periode
        layout.addWidget(self.labelPeriode1,3,0)
        layout.addWidget(self.labelVide,3,1)
        layout.addWidget(self.leDate1Debut,3,2)
        layout.addWidget(self.labelVide,3,3)
        layout.addWidget(self.leDate1Fin,3,4)
        layout.addWidget(self.labelVide,3,5)
        #2eme periode
        layout.addWidget(self.labelPeriode2,4,0)
        layout.addWidget(self.labelVide,4,1)
        layout.addWidget(self.leDate2Debut,4,2)
        layout.addWidget(self.labelVide,4,3)
        layout.addWidget(self.leDate2Fin,4,4)
        layout.addWidget(self.labelVide,4,5)
        #3eme periode
        layout.addWidget(self.labelPeriode3,5,0)
        layout.addWidget(self.labelVide,5,1)
        layout.addWidget(self.leDate3Debut,5,2)
        layout.addWidget(self.labelVide,5,3)
        layout.addWidget(self.leDate3Fin,5,4)
        layout.addWidget(self.labelVide,5,5)
        #button
        layout.addWidget(self.boutonValidateDate,6,5)
        
        layout2 = QVBoxLayout()
        layout2.addLayout(layout)
        layout2.addStretch()
        self.setLayout(layout2)

    def onValidation(self):
        pass
