"""
Metier: Module qui gere la partie calcul de ClassManager

"""
class Matiere(object):
    def __init__(self, name):
        self.name = name
        self.commentaire = ""
        self.listTest = []
        self.moyenne = -1
        
    def addTest(self, date, note, commentaire='No Comment'):
        """
        date au format 'jj/mm/yy'
        0<=note<=20
        """
        self.listTest.append((date,note,commentaire))
        self.calcMoyenne()

    def removeTestByDate(self,date):
        """
        remove elements of listTest
        using the date
        """
        self.listTest = [x for x in self.listTest if date != x[0]]
        self.calcMoyenne()

    def calcMoyenne(self):
        """
        calcule la moyenne des notes contenues
        dans listTest
        si listTest est vide, la moyenne vaut -1
        """
        if len(self.listTest) == 0:
            self.moyenne = -1
        tmp = [m[1] for m in self.listTest]
        moy = sum(tmp) / float(len(tmp))
        self.moyenne = moy

class CarnetDeNote(object):
    def __init__(self):
        self.moyenneGenerale = -1
        self.appreciationGenerale = "No Comment"
        self.initDictMatiere("../misc/matiere_config.txt")
    
    def initDictMatiere(self,filename):
        """
        lit un fichier filename de format key name_matiere
        pour creer toutes les matieres presentes dans le carnet de note
        """
        self.dictMatiere = {}
        with open(filename, 'r') as f:
            for line in f:
                l = line.split()
                #on cree un dictionnaire contenant
                #les matieres contenus dans filename
                self.dictMatiere[l[0]]=Matiere(l[1])
        

    def printMatiereName(self):
        for key in self.dictMatiere:
            print self.dictMatiere[key].name,
        print ""


class Eleve(object):
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.eleveId = -1
        self.classeId = -1
        self.cdn = CarnetDeNote()
    
    def setId(self,eleveId,classeId):
        self.eleveId = eleveId
        self.classeId = classeId
    
    def printEleve(self):
        print "name:", self.name
        print "surname:", self.surname
        print "id:", self.eleveId
        print "class:", self.classeId
        self.cdn.printMatiereName()

class Classe(object):
    def __init__(self,name):
        self.name = name
        self.listEleves = []
        self.classeId = -1
    
    def setId(self, classeId):
        self.classeId = classeId

    def addEleve(self,eleve):
        eleveId = len(self.listEleves)
        eleve.setId(eleveId,self.classeId)
        self.listEleves.append(eleve)
        
    def removeEleve(self,eleve):
        pass

    def printClasse(self):
        for elt in self.listEleves:
            elt.printEleve()

class ClassManager(object):

    def __init__(self):
        self.listClass = []
        
    def createClasse(self, name='ClassDefault'):
        new_Classe = Classe(name)
        classeId = len(self.listClass)
        new_Classe.setId(classeId)
        return new_Classe
    
    def addClasse(self, classe):
        pass
    
    def deleteClasse(self,classeToRemove):
        pass
    

